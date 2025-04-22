document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const saveButton = document.getElementById("saveButton");

    function checkFormValidity() {
        if (form.checkValidity()) {
            saveButton.removeAttribute("disabled");  // ✅ เปิดปุ่ม
        } else {
            
            saveButton.setAttribute("disabled", "true");  // ❌ ปิดปุ่ม
        }
    }

    form.addEventListener("input", checkFormValidity);
});