# 🚀 Complete Setup & Usage Guide

## Chemical Equipment Parameter Visualizer
### Enterprise-Grade Hybrid Web + Desktop Data Visualization Platform

---

## 📋 Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Running the Application](#running-the-application)
4. [Usage Guide](#usage-guide)
5. [API Documentation](#api-documentation)
6. [Troubleshooting](#troubleshooting)
7. [Architecture](#architecture)

---

## Prerequisites

### Required Software
- **Python 3.8+** - [Download](https://www.python.org/downloads/)
- **Node.js 16+** - [Download](https://nodejs.org/)
- **Git** - [Download](https://git-scm.com/)

### Verify Installation
```bash
python --version    # Should show 3.8 or higher
node --version      # Should show 16 or higher
npm --version       # Should show 8 or higher
```

---

## Installation

### Method 1: Automated Setup (Recommended)

#### Windows
Simply double-click the batch files:
1. `start_backend.bat` - Sets up and starts Django
2. `start_frontend.bat` - Sets up and starts React
3. `start_desktop.bat` - Sets up and starts PyQt5

### Method 2: Manual Setup

#### Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional, for admin panel)
python manage.py createsuperuser

# Start server
python manage.py runserver
```

**Backend runs at**: http://localhost:8000

#### Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

**Frontend runs at**: http://localhost:3000

#### Desktop App Setup
```bash
# Navigate to desktop directory
cd desktop

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
python main.py
```

---

## Running the Application

### Start All Services

**Terminal 1 - Backend:**
```bash
cd backend
venv\Scripts\activate
python manage.py runserver
```

**Terminal 2 - Web Frontend:**
```bash
cd frontend
npm start
```

**Terminal 3 - Desktop App:**
```bash
cd desktop
venv\Scripts\activate
python main.py
```

### Verify Services
- Backend API: http://localhost:8000/admin
- Web App: http://localhost:3000
- Desktop App: Should open automatically

---

## Usage Guide

### 1. User Registration & Login

#### Web Application
1. Open browser to http://localhost:3000
2. Click "Need an account? Register"
3. Enter username, email, password
4. Click "Register"
5. You'll be automatically logged in

#### Desktop Application
1. Launch desktop app
2. Enter username and password
3. Click "Register" for new account or "Login" for existing

### 2. Upload CSV Data

#### Required CSV Format
```csv
Equipment Name,Type,Flowrate,Pressure,Temperature
Pump-A1,Pump,150.5,45.2,85.3
Valve-B2,Valve,120.3,38.7,72.1
```

**Required Columns:**
- Equipment Name (string)
- Type (string)
- Flowrate (numeric)
- Pressure (numeric)
- Temperature (numeric)

#### Web Upload
1. Click "Upload CSV" button on dashboard
2. Select your CSV file
3. Wait for success message
4. Dashboard updates automatically

#### Desktop Upload
1. Click "Upload CSV" button
2. Browse and select CSV file
3. Click "Open"
4. Dashboard refreshes with new data

### 3. View Analytics

#### Dashboard Features

**KPI Cards:**
- Total Records: Count of equipment entries
- Average Flowrate: Mean flowrate across all equipment
- Average Pressure: Mean pressure value
- Average Temperature: Mean temperature value

**Charts:**
1. **Pie Chart**: Equipment Type Distribution
   - Shows percentage breakdown by equipment type
   
2. **Bar Chart**: Average Flowrate Analysis
   - Displays flowrate metrics by equipment type
   
3. **Line Chart**: Pressure vs Temperature
   - Compares average pressure and temperature values

### 4. View History

#### Web Application
1. Click "History" in navigation bar
2. View table of all uploaded datasets
3. See filename, upload date, and statistics

#### Desktop Application
- History dropdown shows recent uploads
- Select to view specific dataset

### 5. Download PDF Report

#### Web Application
1. Click "Download PDF Report" button
2. PDF downloads automatically
3. Open to view professional report

#### Desktop Application
1. Click "Download PDF Report"
2. Choose save location
3. PDF saved to selected location

**PDF Report Contents:**
- Report header with branding
- Dataset metadata (filename, date, record count)
- Summary statistics table
- Equipment type distribution pie chart
- Timestamp and footer

---

## API Documentation

### Base URL
```
http://localhost:8000/api
```

### Authentication Endpoints

#### Register User
```http
POST /api/auth/register
Content-Type: application/json

{
  "username": "testuser",
  "email": "test@example.com",
  "password": "securepass123"
}

Response: 201 Created
{
  "user": {
    "id": 1,
    "username": "testuser",
    "email": "test@example.com"
  },
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

#### Login
```http
POST /api/auth/login
Content-Type: application/json

{
  "username": "testuser",
  "password": "securepass123"
}

Response: 200 OK
{
  "user": {
    "id": 1,
    "username": "testuser",
    "email": "test@example.com"
  },
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Data Endpoints (Require JWT Token)

#### Upload CSV
```http
POST /api/upload
Authorization: Bearer <access_token>
Content-Type: multipart/form-data

file: <csv_file>

Response: 201 Created
{
  "id": 1,
  "uploaded_at": "2024-01-15T10:30:00Z",
  "original_filename": "equipment_data.csv",
  "total_records": 15,
  "avg_flowrate": 152.34,
  "avg_pressure": 46.78,
  "avg_temperature": 85.92,
  "type_distribution": {
    "Pump": 5,
    "Valve": 4,
    "Reactor": 3,
    "Compressor": 2,
    "Heat Exchanger": 1
  }
}
```

#### Get Latest Summary
```http
GET /api/summary/latest
Authorization: Bearer <access_token>

Response: 200 OK
{
  "id": 1,
  "uploaded_at": "2024-01-15T10:30:00Z",
  "original_filename": "equipment_data.csv",
  "total_records": 15,
  "avg_flowrate": 152.34,
  "avg_pressure": 46.78,
  "avg_temperature": 85.92,
  "type_distribution": {
    "Pump": 5,
    "Valve": 4
  }
}
```

#### Get History
```http
GET /api/history
Authorization: Bearer <access_token>

Response: 200 OK
[
  {
    "id": 1,
    "uploaded_at": "2024-01-15T10:30:00Z",
    "original_filename": "equipment_data.csv",
    "total_records": 15,
    ...
  },
  ...
]
```

#### Get Specific Dataset
```http
GET /api/history/1
Authorization: Bearer <access_token>

Response: 200 OK
{
  "id": 1,
  "uploaded_at": "2024-01-15T10:30:00Z",
  ...
}
```

#### Download PDF Report
```http
GET /api/report/pdf
Authorization: Bearer <access_token>

Response: 200 OK
Content-Type: application/pdf
Content-Disposition: attachment; filename="equipment_report_20240115_103000.pdf"

<binary PDF data>
```

---

## Troubleshooting

### Backend Issues

**Problem**: Port 8000 already in use
```bash
# Solution: Use different port
python manage.py runserver 8001
# Update API_BASE_URL in frontend and desktop
```

**Problem**: Database errors
```bash
# Solution: Reset database
del db.sqlite3
python manage.py makemigrations
python manage.py migrate
```

**Problem**: Module not found
```bash
# Solution: Reinstall dependencies
pip install -r requirements.txt
```

### Frontend Issues

**Problem**: Port 3000 in use
```
# Solution: React will prompt to use different port
# Press 'Y' to accept
```

**Problem**: Module not found
```bash
# Solution: Clear and reinstall
rm -rf node_modules package-lock.json
npm install
```

**Problem**: CORS errors
```
# Solution: Verify backend CORS settings in settings.py
CORS_ALLOW_ALL_ORIGINS = True
```

### Desktop Issues

**Problem**: PyQt5 import error
```bash
# Solution: Ensure virtual environment is activated
venv\Scripts\activate
pip install PyQt5
```

**Problem**: API connection refused
```
# Solution: Verify backend is running
# Check http://localhost:8000/admin
```

**Problem**: Chart not displaying
```bash
# Solution: Reinstall matplotlib
pip uninstall matplotlib
pip install matplotlib
```

### Common Issues

**Problem**: JWT token expired
```
# Solution: Login again to get new token
```

**Problem**: CSV upload fails
```
# Solution: Verify CSV format
# Must have: Equipment Name, Type, Flowrate, Pressure, Temperature
```

---

## Architecture

### System Components

```
┌─────────────────────────────────────────────────────────┐
│                     Client Layer                         │
├──────────────────────────┬──────────────────────────────┤
│   React Web App          │   PyQt5 Desktop App          │
│   - Material-UI          │   - Native GUI               │
│   - Chart.js             │   - Matplotlib               │
│   - Axios                │   - Requests                 │
└──────────────────────────┴──────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│                    API Layer (REST)                      │
│                  Django REST Framework                   │
│                    JWT Authentication                    │
└─────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│                   Business Logic                         │
│   ┌──────────┬──────────┬──────────┬──────────┐        │
│   │Equipment │  Users   │ Reports  │   Core   │        │
│   │   App    │   App    │   App    │  Config  │        │
│   └──────────┴──────────┴──────────┴──────────┘        │
└─────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│                    Data Layer                            │
│                  SQLite Database                         │
│              (Production: PostgreSQL)                    │
└─────────────────────────────────────────────────────────┘
```

### Data Flow

```
CSV Upload → Validation → Pandas Processing → Statistics Calculation
     ↓
Database Storage → Auto-Cleanup (Last 5) → API Response
     ↓
Client Rendering → Charts Display → User Interaction
```

---

## 📚 Additional Resources

- **README.md**: Main project documentation
- **TECHNICAL_OVERVIEW.md**: Detailed technical architecture
- **PROJECT_SUMMARY.md**: Complete project summary
- **sample_data.csv**: Sample CSV for testing

---

## 🎯 Quick Test Checklist

- [ ] Backend running on port 8000
- [ ] Frontend running on port 3000
- [ ] Desktop app launches successfully
- [ ] User registration works
- [ ] User login works
- [ ] CSV upload successful
- [ ] Dashboard displays charts
- [ ] KPI cards show correct values
- [ ] History page shows uploads
- [ ] PDF download works
- [ ] Desktop app shows same data as web

---

## 🔒 Security Notes

- JWT tokens expire after 5 hours
- Passwords are hashed using PBKDF2
- CORS is configured for development
- For production: Set DEBUG=False, use HTTPS, configure proper CORS

---

## 📞 Support

For issues or questions:
1. Check this guide
2. Review README.md
3. Check TECHNICAL_OVERVIEW.md
4. Review code comments

---

**Version**: 1.0.0  
**Last Updated**: 2024  
**Status**: Production Ready ✅
