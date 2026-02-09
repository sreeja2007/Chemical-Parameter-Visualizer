# Chemical Equipment Parameter Visualizer

Enterprise-grade Hybrid Web + Desktop Data Visualization Platform for analyzing chemical equipment parameters.

## 🏗 Architecture

- **Backend**: Django REST Framework with JWT authentication
- **Web Frontend**: React with Material-UI and Chart.js
- **Desktop Frontend**: PyQt5 with Matplotlib
- **Database**: SQLite
- **API**: RESTful with JWT token-based authentication

## 📊 Features

### Backend
- CSV file upload and validation
- Automated data processing with Pandas
- Statistical analysis (averages, distributions)
- JWT authentication (register/login)
- Auto-retention of last 5 datasets
- Professional PDF report generation with charts
- RESTful API endpoints

### Web Frontend
- Responsive Material-UI design
- Interactive Chart.js visualizations
- Protected routes with JWT
- CSV upload interface
- Real-time dashboard with KPI cards
- Upload history viewer
- PDF report download

### Desktop Application
- Native PyQt5 interface
- Matplotlib chart integration
- CSV upload functionality
- Dataset history dropdown
- PDF report download
- Cross-platform compatibility

## 🚀 Installation & Setup

### Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Backend runs at: `http://localhost:8000`

### Web Frontend Setup

```bash
cd frontend
npm install
npm start
```

Web app runs at: `http://localhost:3000`

### Desktop Application Setup

```bash
cd desktop
python -m venv venv

 # Windows
pip install -r requirements.txt
python main.py
```

## 📡 API Endpoints

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/api/auth/register` | No | User registration |
| POST | `/api/auth/login` | No | User login |
| POST | `/api/upload` | Yes | Upload CSV file |
| GET | `/api/summary/latest` | Yes | Get latest dataset summary |
| GET | `/api/history` | Yes | Get all dataset history |
| GET | `/api/history/<id>` | Yes | Get specific dataset |
| GET | `/api/report/pdf` | Yes | Download PDF report |

## 📋 CSV Format

Required columns:
- Equipment Name
- Type
- Flowrate
- Pressure
- Temperature

Example: See `sample_data.csv`

## 🔐 Authentication

- JWT token-based authentication
- Access token lifetime: 5 hours
- Refresh token lifetime: 1 day
- Tokens stored in localStorage (Web) / memory (Desktop)

## 📈 Analytics Computed

- Total record count
- Average Flowrate
- Average Pressure
- Average Temperature
- Equipment Type Distribution (count per type)

## 🎨 Visualizations

### Web (Chart.js)
- Pie Chart: Equipment Type Distribution
- Bar Chart: Average Flowrate by Type
- Line Chart: Pressure vs Temperature

### Desktop (Matplotlib)
- Pie Chart: Equipment Type Distribution
- Bar Chart: Average Flowrate
- Line Chart: Pressure & Temperature Comparison

## 📄 PDF Report Features

- Professional header branding
- Dataset metadata (filename, upload date, record count)
- Summary statistics table
- Equipment type distribution pie chart
- Timestamp and footer
- Downloadable via API endpoint

## 🗄 Database Schema

### EquipmentDataset Model
- `id`: Primary key
- `uploaded_at`: Timestamp
- `original_filename`: String
- `total_records`: Integer
- `avg_flowrate`: Float
- `avg_pressure`: Float
- `avg_temperature`: Float
- `type_distribution`: JSON
- `user`: Foreign key to User

## 🔧 Configuration

### Backend Settings
- `MAX_DATASETS = 5`: Auto-cleanup to keep only last 5 uploads
- CORS enabled for frontend communication
- JWT token configuration in `settings.py`

### Frontend Configuration
- API base URL: `http://localhost:8000/api`
- Axios interceptors for JWT token injection

## 🧪 Testing

1. Start backend server
2. Register a new user via web or desktop app
3. Login with credentials
4. Upload `sample_data.csv`
5. View dashboard with charts
6. Check history page
7. Download PDF report

## 📦 Project Structure

```
Fossee/
├── backend/
│   ├── core/           # Django settings
│   ├── equipment/      # Equipment data app
│   ├── users/          # Authentication app
│   ├── reports/        # PDF generation app
│   └── manage.py
├── frontend/
│   ├── src/
│   │   ├── components/ # Reusable components
│   │   ├── pages/      # Page components
│   │   └── services/   # API service
│   └── package.json
├── desktop/
│   ├── ui/             # PyQt5 windows
│   ├── services/       # API service
│   ├── charts/         # Chart generators
│   └── main.py
└── sample_data.csv
```

## 🛡 Security Features

- Password hashing with Django's built-in system
- JWT token authentication
- CORS configuration
- Protected API endpoints
- Input validation and sanitization

## 🌐 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## 💻 System Requirements

- Python 3.8+
- Node.js 16+
- 4GB RAM minimum
- Windows/Linux/macOS

## 📝 License

Enterprise Edition - All Rights Reserved

## 👥 Support

For issues and questions, contact the development team.

---

**Chemical Equipment Parameter Visualizer** | Enterprise Edition | v1.0.0
