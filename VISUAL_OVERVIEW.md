# 🎨 Chemical Equipment Parameter Visualizer
## Visual Project Overview

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║              CHEMICAL EQUIPMENT PARAMETER VISUALIZER                         ║
║                    Enterprise-Grade Platform                                 ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## 🏗 System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            CLIENT LAYER                                      │
├────────────────────────────────────┬────────────────────────────────────────┤
│                                    │                                        │
│         WEB APPLICATION            │       DESKTOP APPLICATION              │
│                                    │                                        │
│  ┌──────────────────────────┐     │    ┌──────────────────────────┐       │
│  │   React 18.2.0           │     │    │   PyQt5 5.15.10          │       │
│  │   Material-UI 5.14.18    │     │    │   Matplotlib 3.8.2       │       │
│  │   Chart.js 4.4.0         │     │    │   Requests 2.31.0        │       │
│  │   Axios 1.6.2            │     │    │                          │       │
│  └──────────────────────────┘     │    └──────────────────────────┘       │
│                                    │                                        │
│  Features:                         │    Features:                           │
│  • Login/Register                  │    • Login Window                      │
│  • Dashboard with Charts           │    • Dashboard with Charts             │
│  • CSV Upload                      │    • CSV Upload Dialog                 │
│  • History Viewer                  │    • Dataset History                   │
│  • PDF Download                    │    • PDF Download                      │
│  • Protected Routes                │    • Native GUI                        │
│                                    │                                        │
└────────────────────────────────────┴────────────────────────────────────────┘
                                     │
                                     │ HTTP/REST
                                     │ JWT Authentication
                                     ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              API LAYER                                       │
│                                                                              │
│                    Django REST Framework 3.14.0                              │
│                    djangorestframework-simplejwt 5.3.0                       │
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │  Endpoints:                                                         │    │
│  │  • POST /api/auth/register      - User registration                │    │
│  │  • POST /api/auth/login         - User login                       │    │
│  │  • POST /api/upload             - CSV upload (Protected)           │    │
│  │  • GET  /api/summary/latest     - Latest dataset (Protected)       │    │
│  │  • GET  /api/history            - All datasets (Protected)         │    │
│  │  • GET  /api/history/<id>       - Specific dataset (Protected)     │    │
│  │  • GET  /api/report/pdf         - PDF report (Protected)           │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                          BUSINESS LOGIC LAYER                                │
│                                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │  Equipment   │  │    Users     │  │   Reports    │  │     Core     │   │
│  │     App      │  │     App      │  │     App      │  │    Config    │   │
│  ├──────────────┤  ├──────────────┤  ├──────────────┤  ├──────────────┤   │
│  │ • Models     │  │ • Auth       │  │ • PDF Gen    │  │ • Settings   │   │
│  │ • Serializer │  │ • Register   │  │ • ReportLab  │  │ • URLs       │   │
│  │ • Views      │  │ • Login      │  │ • Charts     │  │ • CORS       │   │
│  │ • CSV Logic  │  │ • JWT        │  │              │  │ • JWT Config │   │
│  │ • Pandas     │  │              │  │              │  │              │   │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                            DATA LAYER                                        │
│                                                                              │
│                          SQLite Database                                     │
│                    (Production: PostgreSQL)                                  │
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │  EquipmentDataset Model:                                            │    │
│  │  • id (PK)                                                          │    │
│  │  • uploaded_at (DateTime)                                           │    │
│  │  • original_filename (String)                                       │    │
│  │  • total_records (Integer)                                          │    │
│  │  • avg_flowrate (Float)                                             │    │
│  │  • avg_pressure (Float)                                             │    │
│  │  • avg_temperature (Float)                                          │    │
│  │  • type_distribution (JSON)                                         │    │
│  │  • user (FK to User)                                                │    │
│  │                                                                      │    │
│  │  Auto-Cleanup: Retains only last 5 datasets                         │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## 📊 Data Flow Diagram

```
┌─────────────┐
│   User      │
│  Uploads    │
│   CSV       │
└──────┬──────┘
       │
       ▼
┌─────────────────────────────────────────────────────────────┐
│                    CSV Processing Pipeline                   │
│                                                              │
│  1. File Validation                                          │
│     └─→ Check .csv extension                                │
│                                                              │
│  2. Pandas DataFrame Creation                                │
│     └─→ pd.read_csv(file)                                   │
│                                                              │
│  3. Schema Validation                                        │
│     └─→ Verify 5 required columns                           │
│                                                              │
│  4. Data Cleaning                                            │
│     └─→ df.dropna() - Remove null values                    │
│                                                              │
│  5. Statistical Analysis                                     │
│     ├─→ Total Records: len(df)                              │
│     ├─→ Avg Flowrate: df['Flowrate'].mean()                 │
│     ├─→ Avg Pressure: df['Pressure'].mean()                 │
│     ├─→ Avg Temperature: df['Temperature'].mean()           │
│     └─→ Type Distribution: df['Type'].value_counts()        │
│                                                              │
│  6. Database Persistence                                     │
│     └─→ EquipmentDataset.objects.create(...)                │
│                                                              │
│  7. Auto-Cleanup                                             │
│     └─→ Keep only last 5 datasets                           │
│                                                              │
│  8. API Response                                             │
│     └─→ Return serialized JSON                              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────────────────────────────┐
│                    Client Visualization                      │
│                                                              │
│  Web (Chart.js)              Desktop (Matplotlib)            │
│  ├─ Pie Chart                ├─ Pie Chart                   │
│  ├─ Bar Chart                ├─ Bar Chart                   │
│  └─ Line Chart               └─ Line Chart                  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## 🔐 Authentication Flow

```
┌──────────┐
│  Client  │
└────┬─────┘
     │
     │ 1. POST /api/auth/register or /api/auth/login
     │    { username, password }
     ▼
┌─────────────────┐
│  Django Backend │
└────┬────────────┘
     │
     │ 2. Validate credentials
     │    • Check username/password
     │    • Hash password (PBKDF2)
     ▼
┌─────────────────┐
│  JWT Generator  │
└────┬────────────┘
     │
     │ 3. Generate tokens
     │    • Access token (5 hours)
     │    • Refresh token (1 day)
     ▼
┌──────────┐
│  Client  │
└────┬─────┘
     │
     │ 4. Store tokens
     │    • Web: localStorage
     │    • Desktop: memory
     ▼
┌──────────────────┐
│  Protected API   │
│  Request         │
└────┬─────────────┘
     │
     │ 5. Include token in header
     │    Authorization: Bearer <token>
     ▼
┌─────────────────┐
│  JWT Validator  │
└────┬────────────┘
     │
     │ 6. Validate token
     │    • Check signature
     │    • Check expiration
     ▼
┌──────────────┐
│  API Response│
└──────────────┘
```

## 📈 Chart Visualization

```
┌─────────────────────────────────────────────────────────────────────┐
│                         DASHBOARD                                    │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐           │
│  │  Total   │  │   Avg    │  │   Avg    │  │   Avg    │           │
│  │ Records  │  │ Flowrate │  │ Pressure │  │   Temp   │           │
│  │   15     │  │  152.34  │  │  46.78   │  │  85.92   │           │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘           │
│                                                                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐             │
│  │              │  │              │  │              │             │
│  │  Pie Chart   │  │  Bar Chart   │  │  Line Chart  │             │
│  │              │  │              │  │              │             │
│  │   Type       │  │   Flowrate   │  │  Pressure &  │             │
│  │ Distribution │  │   Analysis   │  │  Temperature │             │
│  │              │  │              │  │              │             │
│  │   🥧        │  │   📊        │  │   📈        │             │
│  │              │  │              │  │              │             │
│  └──────────────┘  └──────────────┘  └──────────────┘             │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

## 🗂 Project Structure

```
Fossee/
│
├── 📁 backend/                    Django REST API
│   ├── 📁 core/                   Settings & Configuration
│   ├── 📁 equipment/              Data Management
│   ├── 📁 users/                  Authentication
│   ├── 📁 reports/                PDF Generation
│   └── 📄 manage.py               Django CLI
│
├── 📁 frontend/                   React Web App
│   ├── 📁 src/
│   │   ├── 📁 components/         Reusable Components
│   │   ├── 📁 pages/              Page Components
│   │   └── 📁 services/           API Client
│   └── 📄 package.json            Dependencies
│
├── 📁 desktop/                    PyQt5 Desktop App
│   ├── 📁 ui/                     GUI Windows
│   ├── 📁 services/               API Client
│   ├── 📁 charts/                 Chart Generation
│   └── 📄 main.py                 Entry Point
│
├── 📄 sample_data.csv             Test Data
├── 📄 README.md                   Main Documentation
├── 📄 QUICKSTART.md               Quick Setup
├── 📄 SETUP_GUIDE.md              Detailed Guide
├── 📄 TECHNICAL_OVERVIEW.md       Architecture
├── 📄 PROJECT_SUMMARY.md          Complete Summary
├── 📄 INDEX.md                    Documentation Index
│
└── 🚀 Startup Scripts
    ├── start_backend.bat
    ├── start_frontend.bat
    └── start_desktop.bat
```

## 🎯 Feature Matrix

```
┌─────────────────────────┬──────────┬──────────┬──────────┐
│       Feature           │  Backend │    Web   │  Desktop │
├─────────────────────────┼──────────┼──────────┼──────────┤
│ User Registration       │    ✅    │    ✅    │    ✅    │
│ User Login              │    ✅    │    ✅    │    ✅    │
│ JWT Authentication      │    ✅    │    ✅    │    ✅    │
│ CSV Upload              │    ✅    │    ✅    │    ✅    │
│ Data Validation         │    ✅    │    ✅    │    ✅    │
│ Statistical Analysis    │    ✅    │    ✅    │    ✅    │
│ Pie Chart               │    N/A   │    ✅    │    ✅    │
│ Bar Chart               │    N/A   │    ✅    │    ✅    │
│ Line Chart              │    N/A   │    ✅    │    ✅    │
│ KPI Cards               │    N/A   │    ✅    │    ✅    │
│ Upload History          │    ✅    │    ✅    │    ✅    │
│ PDF Report              │    ✅    │    ✅    │    ✅    │
│ Auto-Cleanup (Last 5)   │    ✅    │    N/A   │    N/A   │
│ Responsive Design       │    N/A   │    ✅    │    N/A   │
│ Native GUI              │    N/A   │    N/A   │    ✅    │
└─────────────────────────┴──────────┴──────────┴──────────┘
```

## 🚀 Quick Start Commands

```bash
# Backend
cd backend && python manage.py runserver

# Frontend
cd frontend && npm start

# Desktop
cd desktop && python main.py
```

## 📊 Technology Stack

```
Backend:
  ├─ Django 4.2.7
  ├─ Django REST Framework 3.14.0
  ├─ JWT Authentication
  ├─ Pandas 2.1.3
  └─ ReportLab 4.0.7

Frontend:
  ├─ React 18.2.0
  ├─ Material-UI 5.14.18
  ├─ Chart.js 4.4.0
  └─ Axios 1.6.2

Desktop:
  ├─ PyQt5 5.15.10
  ├─ Matplotlib 3.8.2
  └─ Requests 2.31.0
```

---

**Chemical Equipment Parameter Visualizer v1.0.0**  
**Enterprise Edition | Production Ready ✅**
