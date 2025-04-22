document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const saveButton = document.getElementById("saveButton");

    if (!saveButton) {
        console.error("Save button not found!");
        return;
    }

    function checkFormValidity() {
        if (form.checkValidity()) {
            saveButton.removeAttribute("disabled");
        } else {
            saveButton.setAttribute("disabled", "true");
        }
    }

    form.addEventListener("input", checkFormValidity);
});
