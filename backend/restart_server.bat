@echo off
taskkill /F /IM python.exe 2>nul
timeout /t 2 /nobreak >nul
python manage.py runserver
