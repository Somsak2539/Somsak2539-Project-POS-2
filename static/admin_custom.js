document.addEventListener("DOMContentLoaded", function() {
    // ค้นหาเมนู "AUTHENTICATION AND AUTHORIZATION" และเปลี่ยนชื่อ
    let authMenu = document.querySelector('div.module caption');
    if (authMenu && authMenu.innerText.includes("AUTHENTICATION AND AUTHORIZATION")) {
        authMenu.innerText = "จัดการบัญชีและสิทธิ์";  // ✅ เปลี่ยนชื่อที่ต้องการ
    }
});
