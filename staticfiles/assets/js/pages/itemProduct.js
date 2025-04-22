
function formatDateInput(dateInputId) {
    const input = document.getElementById(dateInputId);
    if (input) {
        input.addEventListener('change', function () {
            const date = new Date(this.value);
            if (!isNaN(date)) {
                const day = String(date.getDate()).padStart(2, '0');
                const month = String(date.getMonth() + 1).padStart(2, '0');
                const year = date.getFullYear();
                this.value = `${year}-${month}-${day}`; // เปลี่ยนเป็น YYYY-MM-DD เพื่อให้ Django ใช้ได้
            }
        });
    }
}

formatDateInput('start_date');
formatDateInput('end_date');
