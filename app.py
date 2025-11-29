from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

# Load your trained pipeline
model = joblib.load("laptop_price_pipeline.joblib")


@app.route("/", methods=["GET", "POST"])
def index():
    predicted_price = None
    error = None

    if request.method == "POST":
        try:
            # --------- Get form values ----------
            company = request.form.get("Company")
            typename = request.form.get("TypeName")
            inches = float(request.form.get("Inches"))

            # Screen features
            is_ips = 1 if request.form.get("is_ips") == "on" else 0
            is_retina = 1 if request.form.get("is_retina") == "on" else 0
            is_touchscreen = 1 if request.form.get("is_touchscreen") == "on" else 0

            res_w = float(request.form.get("res_w"))
            res_h = float(request.form.get("res_h"))

            # ppi (same formula as training)
            ppi = ((res_w ** 2 + res_h ** 2) ** 0.5) / inches

            # CPU related
            cpu_brand = request.form.get("cpu_brand")
            cpu_series = request.form.get("cpu_series")
            cpu_clock_speed = float(request.form.get("cpu_clock_speed"))
            # 1 = low power (U/Y), 0 = high power (H)
            is_low_power_cpu_val = request.form.get("is_low_power_cpu", "1")
            is_low_power_cpu = int(is_low_power_cpu_val)


            # RAM & storage
            ram_gb = int(request.form.get("ram_gb"))
            ssd_gb = float(request.form.get("ssd_gb"))
            hdd_gb_raw = float(request.form.get("hdd_gb"))
            flash_gb_raw = float(request.form.get("flash_gb"))

            # total storage (same as training)
            total_storage = ssd_gb + hdd_gb_raw + flash_gb_raw

            # log transform like in notebook
            hdd_gb = np.log1p(hdd_gb_raw)
            flash_gb = np.log1p(flash_gb_raw)

            # GPU
            gpu_brand = request.form.get("gpu_brand")
            gpu_type = request.form.get("gpu_type")  # Integrated / Dedicated

            # OS
            opsys = request.form.get("OpSys")

            # Weight
            weight_kg = float(request.form.get("weight_kg"))

            # --------- Build input row (must match training columns) ----------
            input_data = {
                "Company": company,
                "TypeName": typename,
                "Inches": inches,
                "is_ips": is_ips,
                "is_retina": is_retina,
                "is_touchscreen": is_touchscreen,
                "res_w": res_w,
                "res_h": res_h,
                "ppi": ppi,
                "cpu_brand": cpu_brand,
                "cpu_series": cpu_series,
                "cpu_clock_speed": cpu_clock_speed,
                "is_low_power_cpu": is_low_power_cpu,
                "ram_gb": ram_gb,
                "ssd_gb": ssd_gb,
                "hdd_gb": hdd_gb,
                "flash_gb": flash_gb,
                "total_storage": total_storage,
                "gpu_brand": gpu_brand,
                "gpu_type": gpu_type,
                "OpSys": opsys,
                "weight_kg": weight_kg,
            }

            input_df = pd.DataFrame([input_data])

            # --------- Predict (model outputs log(price)) ----------
            log_price_pred = model.predict(input_df)[0]
            price_pred = np.expm1(log_price_pred)  # back to original ₹

            predicted_price = round(float(price_pred), 2)

        except Exception as e:
            error = str(e)
            print("Error:", e)

    return render_template(
        "index.html",
        predicted_price=predicted_price,
        error=error
    )


if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)
