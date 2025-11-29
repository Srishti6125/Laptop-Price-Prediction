document.addEventListener("DOMContentLoaded", function () {
    const gpuBrand = document.getElementById("gpu_brand");
    const gpuType = document.getElementById("gpu_type");
    const form = document.getElementById("prediction-form");
    const submitBtn = document.getElementById("submit-btn");

    // Auto-set GPU type when Intel is selected
    if (gpuBrand && gpuType) {
        gpuBrand.addEventListener("change", () => {
            if (gpuBrand.value === "Intel") {
                gpuType.value = "Integrated";
            }
        });
    }

    // Simple loading state on submit
    if (form && submitBtn) {
        form.addEventListener("submit", () => {
            submitBtn.classList.add("loading");
            submitBtn.disabled = true;
        });
    }
});
