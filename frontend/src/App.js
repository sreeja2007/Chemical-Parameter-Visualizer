import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate, useLocation } from 'react-router-dom';
import { AppBar, Toolbar, Typography, Button, Box, Container } from '@mui/material';
import { Dashboard as DashboardIcon, History as HistoryIcon, Logout, Science } from '@mui/icons-material';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import History from './pages/History';
import ProtectedRoute from './components/ProtectedRoute';

function AppContent() {
  const [isAuthenticated, setIsAuthenticated] = useState(!!localStorage.getItem('access_token'));
  const location = useLocation();

  useEffect(() => {
    setIsAuthenticated(!!localStorage.getItem('access_token'));
  }, [location]);

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    setIsAuthenticated(false);
    window.location.href = '/login';
  };

  return (
    <Box sx={{ flexGrow: 1, minHeight: '100vh' }}>
      {isAuthenticated && location.pathname !== '/login' && (
        <AppBar 
          position="static" 
          elevation={0}
          sx={{ 
            background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
            borderBottom: '3px solid rgba(255,255,255,0.1)'
          }}
        >
          <Container maxWidth="lg">
            <Toolbar sx={{ px: 0 }}>
              <Science sx={{ mr: 2, fontSize: 32 }} />
              <Typography variant="h6" component="div" sx={{ flexGrow: 1, fontWeight: 'bold' }}>
                Chemical Equipment Visualizer
              </Typography>
              <Button 
                color="inherit" 
                href="/dashboard"
                startIcon={<DashboardIcon />}
                sx={{ 
                  mx: 1,
                  fontWeight: 'bold',
                  '&:hover': { background: 'rgba(255,255,255,0.1)' }
                }}
              >
                Dashboard
              </Button>
              <Button 
                color="inherit" 
                href="/history"
                startIcon={<HistoryIcon />}
                sx={{ 
                  mx: 1,
                  fontWeight: 'bold',
                  '&:hover': { background: 'rgba(255,255,255,0.1)' }
                }}
              >
                History
              </Button>
              <Button 
                color="inherit" 
                onClick={handleLogout}
                startIcon={<Logout />}
                sx={{ 
                  mx: 1,
                  fontWeight: 'bold',
                  '&:hover': { background: 'rgba(255,255,255,0.1)' }
                }}
              >
                Logout
              </Button>
            </Toolbar>
          </Container>
        </AppBar>
      )}

      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/dashboard" element={<ProtectedRoute><Dashboard /></ProtectedRoute>} />
        <Route path="/history" element={<ProtectedRoute><History /></ProtectedRoute>} />
        <Route path="/" element={<Navigate to="/login" />} />
      </Routes>
    </Box>
  );
}

function App() {
  return (
    <Router>
      <AppContent />
    </Router>
  );
}

export default App;
