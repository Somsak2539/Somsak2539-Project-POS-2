/*
Template Name: StarCode & Dashboard Template
Author: StarCode Kh
Version: 1.1.0
Website: https://StarCode Kh.in/
Contact: StarCode Kh@gmail.com
File: auth login init Js File
*/

document.getElementById('signInForm').addEventListener('submit', function (event) {
    event.preventDefault(); // ป้องกันการ submit ทันที

    // ดึงค่าจาก input
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();

    // Regular Expressions
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;  // ตรวจสอบ email
    const strongPasswordRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;  // รหัสผ่านต้องมีตัวเลขและตัวอักษร 8 ตัวขึ้นไป

    // Element สำหรับแสดง error และ success
    const usernameError = document.getElementById('username-error');
    const passwordError = document.getElementById('password-error');
    const successAlert = document.getElementById('successAlert');
    const rememberMeCheckbox = document.getElementById('checkboxDefault1');
    const rememberError = document.getElementById('remember-error');

    // ซ่อนข้อความแจ้งเตือนทั้งหมดก่อน
    usernameError.classList.add('hidden');
    passwordError.classList.add('hidden');
    rememberError.classList.add('hidden');
    successAlert.classList.add('hidden');

    let isValid = true;

    // ✅ ตรวจสอบ Username (สามารถเป็นอีเมลหรือชื่อผู้ใช้ที่มีความยาว > 3)
    if (!(emailRegex.test(username) || username.length >= 3)) {
        usernameError.classList.remove('hidden');
        isValid = false;
    }

    // ✅ ตรวจสอบ Password (ต้องมีตัวเลขและตัวอักษร 8 ตัวขึ้นไป)
    if (!strongPasswordRegex.test(password)) {
        passwordError.classList.remove('hidden');
        isValid = false;
    }

    // ✅ ตรวจสอบ Remember Me (ไม่จำเป็นต้องเลือก)
    if (!rememberMeCheckbox.checked) {
        rememberError.classList.remove('hidden');
        isValid = false;
    }

    // ✅ ถ้าทุกอย่างถูกต้องให้ submit form
    if (isValid) {
        successAlert.classList.remove('hidden'); // แสดงข้อความสำเร็จ
        setTimeout(() => {
            document.getElementById('signInForm').submit(); // Submit ฟอร์ม
        }, 1000); // รอ 1 วินาทีเพื่อให้ผู้ใช้เห็นข้อความ success
    }
});
