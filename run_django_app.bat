@echo off
cd /d "C:\Users\Asus\Desktop\POS For Sale\projectPOS-main"
call venv\Scripts\activate
start cmd /k "python manage.py runserver 0.0.0.0:8080"
timeout /t 8 > nul
start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" "http://localhost:8080/Dashboard/"
