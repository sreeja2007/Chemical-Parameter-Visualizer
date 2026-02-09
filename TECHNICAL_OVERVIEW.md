# Chemical Equipment Parameter Visualizer - Technical Overview

## System Architecture

### Three-Tier Architecture
1. **Backend Layer**: Django REST API with JWT authentication
2. **Web Client Layer**: React SPA with Material-UI
3. **Desktop Client Layer**: PyQt5 native application

### Data Flow
```
CSV Upload → Backend Processing (Pandas) → Database Storage → API Response → Client Visualization
```

## Technology Stack Justification

### Backend: Django + DRF
- **Django**: Robust ORM, built-in admin, security features
- **DRF**: Powerful serialization, authentication, browsable API
- **Pandas**: Efficient CSV processing and statistical analysis
- **ReportLab**: Professional PDF generation with charts
- **JWT**: Stateless authentication for scalability

### Web Frontend: React
- **React**: Component-based architecture, virtual DOM performance
- **Material-UI**: Enterprise-grade UI components
- **Chart.js**: Lightweight, responsive charts
- **Axios**: Promise-based HTTP client with interceptors

### Desktop: PyQt5
- **PyQt5**: Native cross-platform GUI framework
- **Matplotlib**: Publication-quality charts
- **Requests**: Simple HTTP library for API calls

## Key Features Implementation

### 1. Auto-Cleanup (Last 5 Datasets)
Implemented in `EquipmentDataset.save()` method:
```python
def save(self, *args, **kwargs):
    super().save(*args, **kwargs)
    datasets = EquipmentDataset.objects.all()
    if datasets.count() > settings.MAX_DATASETS:
        datasets[settings.MAX_DATASETS:].delete()
```

### 2. JWT Authentication Flow
1. User registers/logs in
2. Backend returns access + refresh tokens
3. Client stores tokens (localStorage/memory)
4. Axios/Requests interceptor adds token to headers
5. Backend validates token on protected endpoints

### 3. CSV Processing Pipeline
1. Validate file extension
2. Parse CSV with Pandas
3. Validate required columns
4. Drop null values
5. Calculate statistics (mean, count, distribution)
6. Store in database
7. Return serialized response

### 4. Chart Data Consistency
Both web and desktop use same API response format:
```json
{
  "avg_flowrate": 150.5,
  "avg_pressure": 45.2,
  "avg_temperature": 85.3,
  "type_distribution": {"Pump": 5, "Valve": 3}
}
```

### 5. PDF Report Generation
- ReportLab SimpleDocTemplate for layout
- Custom styles for branding
- Table for statistics
- Pie chart for type distribution
- Timestamp and metadata

## Security Considerations

1. **Authentication**: JWT tokens with expiration
2. **Authorization**: Protected endpoints require valid token
3. **Input Validation**: CSV schema validation, file type checking
4. **CORS**: Configured for frontend origin
5. **Password Hashing**: Django's PBKDF2 algorithm
6. **SQL Injection**: Django ORM prevents SQL injection

## Scalability Considerations

1. **Stateless API**: JWT enables horizontal scaling
2. **Database**: SQLite for prototype, easily migrated to PostgreSQL
3. **File Storage**: Currently in-memory, can move to S3/cloud storage
4. **Caching**: Can add Redis for frequently accessed data
5. **Load Balancing**: Stateless design supports load balancers

## Performance Optimizations

1. **Pandas**: Vectorized operations for fast CSV processing
2. **React**: Virtual DOM minimizes re-renders
3. **Chart.js**: Canvas-based rendering for performance
4. **Database Indexing**: Auto-indexed primary keys and foreign keys
5. **API Response**: Only essential data serialized

## Testing Strategy

### Backend Testing
- Unit tests for models, serializers, views
- Integration tests for API endpoints
- CSV processing edge cases

### Frontend Testing
- Component unit tests with Jest
- Integration tests with React Testing Library
- E2E tests with Cypress

### Desktop Testing
- PyQt widget testing
- API integration tests
- Chart rendering validation

## Deployment Considerations

### Backend
- Use Gunicorn/uWSGI for production
- Configure PostgreSQL database
- Set up static file serving (Nginx)
- Environment variables for secrets
- SSL/TLS certificates

### Web Frontend
- Build optimized production bundle
- Deploy to CDN (Cloudflare, AWS CloudFront)
- Configure environment-specific API URLs

### Desktop
- Package with PyInstaller
- Create installers for Windows/Mac/Linux
- Code signing for security

## Future Enhancements

1. **Real-time Updates**: WebSocket integration
2. **Advanced Analytics**: Machine learning predictions
3. **Multi-user Collaboration**: Shared datasets
4. **Export Options**: Excel, JSON, XML
5. **Scheduled Reports**: Email PDF reports
6. **Data Versioning**: Track dataset changes
7. **Role-Based Access**: Admin, viewer, editor roles
8. **Audit Logging**: Track all user actions
9. **API Rate Limiting**: Prevent abuse
10. **Internationalization**: Multi-language support

## Maintenance Guidelines

1. **Dependencies**: Regular security updates
2. **Database Backups**: Automated daily backups
3. **Monitoring**: Application performance monitoring (APM)
4. **Logging**: Centralized logging (ELK stack)
5. **Documentation**: Keep API docs updated

## Code Quality Standards

1. **PEP 8**: Python style guide compliance
2. **ESLint**: JavaScript linting
3. **Type Hints**: Python type annotations
4. **PropTypes**: React component prop validation
5. **Code Reviews**: Mandatory peer reviews
6. **CI/CD**: Automated testing and deployment

---

**Document Version**: 1.0.0  
**Last Updated**: 2024  
**Author**: Principal Full-Stack Engineer
