import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Container, Paper, TextField, Button, Typography, Box, Alert, Fade, Slide, keyframes } from '@mui/material';
import { Science, Login as LoginIcon, PersonAdd } from '@mui/icons-material';
import { authAPI } from '../services/api';

const float = keyframes`
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(5deg); }
`;

const bubble = keyframes`
  0% { transform: translateY(0) scale(0); opacity: 0; }
  50% { opacity: 0.8; }
  100% { transform: translateY(-100vh) scale(1); opacity: 0; }
`;

function Login() {
  const [isLogin, setIsLogin] = useState(true);
  const [formData, setFormData] = useState({ username: '', email: '', password: '' });
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    
    try {
      const response = isLogin 
        ? await authAPI.login({ username: formData.username, password: formData.password })
        : await authAPI.register(formData);
      
      localStorage.setItem('access_token', response.data.access);
      localStorage.setItem('refresh_token', response.data.refresh);
      navigate('/dashboard');
    } catch (err) {
      console.error('Auth error:', err.response);
      const errorMsg = err.response?.data?.error 
        || err.response?.data?.detail 
        || err.response?.data?.message
        || JSON.stringify(err.response?.data)
        || 'Authentication failed';
      setError(errorMsg);
    }
  };

  return (
    <Box sx={{ 
      minHeight: '100vh',
      background: 'linear-gradient(135deg, #dfe4db 0%, #d4ea66 100%)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      py: 4,
      position: 'relative',
      overflow: 'hidden'
    }}>
      {/* Floating chemical molecules */}
      {[...Array(8)].map((_, i) => (
        <Box
          key={i}
          sx={{
            position: 'absolute',
            fontSize: { xs: '30px', md: '50px' },
            opacity: 0.45,
            animation: `${float} ${3 + i * 0.5}s ease-in-out infinite`,
            animationDelay: `${i * 0.3}s`,
            left: `${10 + i * 12}%`,
            top: `${20 + (i % 3) * 25}%`
          }}
        >
          {['⚗️', '🧪', '🔬', '⚛️', '🧬', '💊', '🌡️', '⚗️'][i]}
        </Box>
      ))}
      
      {/* Bubbles animation */}
      {[...Array(15)].map((_, i) => (
        <Box
          key={`bubble-${i}`}
          sx={{
            position: 'absolute',
            width: { xs: '10px', md: '20px' },
            height: { xs: '10px', md: '20px' },
            borderRadius: '50%',
            background: 'rgba(37, 50, 147, 0.3)',
            bottom: '-50px',
            left: `${Math.random() * 100}%`,
            animation: `${bubble} ${5 + Math.random() * 5}s linear infinite`,
            animationDelay: `${Math.random() * 5}s`
          }}
        />
      ))}

      <Container maxWidth="sm" sx={{ position: 'relative', zIndex: 1 }}>
        <Fade in timeout={800}>
          <Paper elevation={24} sx={{ 
            p: 5,
            borderRadius: 4,
            background: 'rgb(251, 253, 254)',
            backdropFilter: 'blur(10px)'
          }}>
            <Box sx={{ textAlign: 'center', mb: 4 }}>
              <Box sx={{ animation: `${float} 3s ease-in-out infinite` }}>
                <Science sx={{ fontSize: 60, color: '#f57396', mb: 2 }} />
              </Box>
              <Typography variant="h4" fontWeight="bold" color="#1f3180" gutterBottom>
                Chemical Equipment
              </Typography>
              <Typography variant="h5" color="#3b6971" gutterBottom>
                Parameter Visualizer
              </Typography>
            </Box>
            
            <Slide direction="up" in timeout={600}>
              <Box>
                <Box sx={{ 
                  display: 'flex', 
                  justifyContent: 'center', 
                  mb: 3,
                  borderBottom: '2px solid #f0f0f0',
                  pb: 1
                }}>
                  <Button 
                    startIcon={<LoginIcon />}
                    onClick={() => setIsLogin(true)}
                    sx={{ 
                      mr: 2,
                      fontWeight: isLogin ? 'bold' : 'normal',
                      color: isLogin ? '#65953b' : 'text.secondary',
                      borderBottom: isLogin ? '3px solid #c4cced' : 'none'
                    }}
                  >
                    Login
                  </Button>
                  <Button 
                    startIcon={<PersonAdd />}
                    onClick={() => setIsLogin(false)}
                    sx={{ 
                      fontWeight: !isLogin ? 'bold' : 'normal',
                      color: !isLogin ? '#bd92e9' : 'text.secondary',
                      borderBottom: !isLogin ? '3px solid #acc768' : 'none'
                    }}
                  >
                    Register
                  </Button>
                </Box>
                
                {error && <Alert severity="error" sx={{ mb: 3, borderRadius: 2 }}>{error}</Alert>}
                
                <Box component="form" onSubmit={handleSubmit}>
                  <TextField
                    fullWidth
                    label="Username"
                    margin="normal"
                    value={formData.username}
                    onChange={(e) => setFormData({ ...formData, username: e.target.value })}
                    required
                    sx={{ mb: 2 }}
                  />
                  
                  {!isLogin && (
                    <TextField
                      fullWidth
                      label="Email"
                      type="email"
                      margin="normal"
                      value={formData.email}
                      onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                      sx={{ mb: 2 }}
                    />
                  )}
                  
                  <TextField
                    fullWidth
                    label="Password"
                    type="password"
                    margin="normal"
                    value={formData.password}
                    onChange={(e) => setFormData({ ...formData, password: e.target.value })}
                    required
                    sx={{ mb: 3 }}
                  />
                  
                  <Button 
                    type="submit" 
                    fullWidth 
                    variant="contained" 
                    size="large"
                    sx={{ 
                      mt: 2,
                      py: 1.5,
                      background: 'linear-gradient(135deg, #219c8e 0%, #adc872 100%)',
                      borderRadius: 2,
                      fontWeight: 'bold',
                      fontSize: '1.1rem',
                      '&:hover': {
                        background: 'linear-gradient(135deg, #5eaa3b 0%, #95df7c 100%)',
                        transform: 'translateY(-2px)',
                        boxShadow: '0 8px 20px rgba(102, 126, 234, 0.4)'
                      },
                      transition: 'all 0.3s ease'
                    }}
                  >
                    {isLogin ? 'Login' : 'Create Account'}
                  </Button>
                </Box>
              </Box>
            </Slide>
          </Paper>
        </Fade>
      </Container>
    </Box>
  );
}

export default Login;
