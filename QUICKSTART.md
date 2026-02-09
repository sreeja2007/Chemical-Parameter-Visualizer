# Quick Start Guide

## Prerequisites
- Python 3.8+
- Node.js 16+
- Git

## Setup Instructions

### 1. Backend Setup (5 minutes)

Open Terminal 1:
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Backend will run at: http://localhost:8000

### 2. Web Frontend Setup (3 minutes)

Open Terminal 2:
```bash
cd frontend
npm install
npm start
```

Web app will run at: http://localhost:3000

### 3. Desktop App Setup (2 minutes)

Open Terminal 3:
```bash
cd desktop
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Quick Test

1. Open web browser to http://localhost:3000
2. Click "Register" and create account
3. Login with credentials
4. Click "Upload CSV" and select `sample_data.csv`
5. View dashboard with charts
6. Click "Download PDF Report"
7. Check "History" page

## Desktop App Test

1. Run desktop app
2. Login with same credentials
3. Click "Upload CSV" and select `sample_data.csv`
4. View charts in dashboard
5. Click "Download PDF Report"

## Troubleshooting

### Backend Issues
- Port 8000 already in use: Change port in `python manage.py runserver 8001`
- Database errors: Delete `db.sqlite3` and run migrations again

### Frontend Issues
- Port 3000 in use: React will prompt to use different port
- Module not found: Run `npm install` again

### Desktop Issues
- PyQt5 import error: Ensure virtual environment is activated
- API connection error: Verify backend is running on port 8000

## API Testing with Postman

Import these endpoints:

1. Register: POST http://localhost:8000/api/auth/register
   ```json
   {
     "username": "testuser",
     "email": "test@example.com",
     "password": "testpass123"
   }
   ```

2. Login: POST http://localhost:8000/api/auth/login
   ```json
   {
     "username": "testuser",
     "password": "testpass123"
   }
   ```

3. Upload CSV: POST http://localhost:8000/api/upload
   - Headers: Authorization: Bearer <token>
   - Body: form-data, key="file", value=<csv file>

4. Get Summary: GET http://localhost:8000/api/summary/latest
   - Headers: Authorization: Bearer <token>

## Windows Batch Scripts

Double-click these files:
- `start_backend.bat` - Starts Django server
- `start_frontend.bat` - Starts React app
- `start_desktop.bat` - Starts PyQt5 app

## Next Steps

1. Explore the codebase
2. Customize charts and styling
3. Add more analytics features
4. Deploy to production

## Support

Check `README.md` and `TECHNICAL_OVERVIEW.md` for detailed documentation.
