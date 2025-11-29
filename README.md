# 💻 Laptop Price Predictor — ML + Flask Web App

> Predict laptop prices using a machine-learning regression pipeline, deployed with a modern neon-themed Flask web interface.

🌐 **Live App**: [Try it here!]((https://laptop-price-prediction-a0et.onrender.com/))  

---

## 🎯 Problem Statement

The goal of this project is to build a **machine-learning based price prediction system** for laptops using their technical specifications.

Users can input details like:

- Brand and laptop type  
- Screen size and resolution  
- CPU brand, series, and clock speed  
- RAM, SSD, HDD, and flash storage  
- GPU brand and type  
- Operating system and weight  

The app then predicts an estimated **price in INR (₹)** based on a trained regression model.

---

## 📦 Dataset

- **Source**: Laptop price dataset  
- **Target Variable**: `Price` (log-transformed during training)  
- **Key Features Used**:
  - `Company`, `TypeName`
  - `Inches`, `res_w`, `res_h`, `ppi`
  - `cpu_brand`, `cpu_series`, `cpu_clock_speed`, `is_low_power_cpu`
  - `ram_gb`, `ssd_gb`, `hdd_gb`, `flash_gb`, `total_storage`
  - `gpu_brand`, `gpu_type`
  - `OpSys`
  - `weight_kg`

Additional engineered features like **PPI (pixels per inch)** and **log-transformed storage values** help the model capture non-linear relationships.

---

## 🔧 Tech Stack

| Segment          | Tools / Libraries |
|------------------|-------------------|
| Data Handling    | `pandas`, `numpy` |
| Modeling         | `scikit-learn`, `XGBoost` |
| Serialization    | `joblib` |
| Web Framework    | `Flask` |
| Frontend         | HTML5, CSS3, JavaScript, Font Awesome, Google Fonts |
| Deployment       | Render, Gunicorn |

---

## 🔄 Project Workflow

```text
📁 Load dataset
🧼 Clean data and handle missing values
🧬 Feature engineering (PPI, CPU flags, log transforms)
🎛 Define preprocessing pipelines (numeric + categorical)
🤖 Train multiple regression models
📊 Compare performance (MAE, RMSE, R²)
🏆 Select best model (XGBoost Regressor)
💾 Save final pipeline using joblib
🌐 Build Flask API + UI around the pipeline
🎨 Design a neon-themed, responsive UI
☁️ Deploy app to Render using Gunicorn
```

---

## 📊 Model Performance (Example)

Multiple models were trained and evaluated:
- Linear Regression
- Random Forest Regressor
- Support Vector Regressor (SVR)
- XGBoost Regressor ✅

The XGBoost Regressor achieved the best overall performance with:
✅ Low MAE (Mean Absolute Error)
✅ Low RMSE (Root Mean Squared Error)
✅ High R² score (explained variance)

This model was selected as the final production model and exported as a pipeline.

---

## 🎨 UI & UX

The web app is designed with a modern neon dark-blue theme featuring:
- Gradient background with soft glow effects
- Card-based form layout with clear section titles
- Responsive two-column grid for inputs
- Highlighted section headings (Basic Details, Display, Processor, etc.)
- Styled dropdowns and inputs with subtle blue borders and focus shadows
- A prominent result card showing the predicted price
- Automatic scrolling to the result section after prediction
- “Sticky” form values so user inputs stay visible after prediction

---

## 🌐 Flask Web App

The app flow:
1. User fills in laptop specs through the web form.
2. Flask backend reads the form data and constructs a single-row DataFrame.
3. Engineered features (like PPI, log-transformed storage) are computed to match the training pipeline.
4. The saved joblib pipeline is used to generate a price prediction.
5. Since the model was trained on log-transformed prices, the prediction is converted back using expm1.
6. The final predicted price in ₹ is displayed in a styled result card.

---

## 🚀 Deployment (Render)

This project is deployed on Render as a web service.

Typical configuration:
- Build command: install dependencies from requirements.txt
- Start command: gunicorn app:app
- Environment: Python 3.x

---

💡 Key Learnings

- Feature engineering (like PPI and storage transformations) can significantly improve regression model performance.
- XGBoost is highly effective for structured tabular data with mixed feature types.
- Combining ML + Flask + modern UI makes models truly usable, not just notebook experiments.

---

❤️ Acknowledgements

This project was built to practice:
- End-to-end machine learning workflows
- Model deployment with Flask and Render
- Frontend design for data-driven applications

  ---
