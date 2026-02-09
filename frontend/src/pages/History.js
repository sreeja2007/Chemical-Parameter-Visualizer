import React, { useState, useEffect } from 'react';
import { Container, Typography, Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, CircularProgress, Box, Chip, Fade, Alert } from '@mui/material';
import { CheckCircle, Schedule, Inbox } from '@mui/icons-material';
import { equipmentAPI } from '../services/api';

function History() {
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchHistory = async () => {
      try {
        const response = await equipmentAPI.getHistory();
        setHistory(response.data);
      } catch (error) {
        console.error('Error fetching history:', error);
        setError('Failed to load history');
      } finally {
        setLoading(false);
      }
    };
    fetchHistory();
  }, []);

  if (loading) return (
    <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '80vh' }}>
      <CircularProgress size={60} />
    </Box>
  );

  return (
    <Box sx={{ background: 'linear-gradient(to bottom, #f8f9fa 0%, #e9ecef 100%)', minHeight: '100vh', py: 4 }}>
      <Container maxWidth="lg">
        <Fade in timeout={600}>
          <Box>
            <Box sx={{ mb: 4, display: 'flex', alignItems: 'center' }}>
              <Schedule sx={{ fontSize: 40, color: '#667eea', mr: 2 }} />
              <Typography variant="h3" fontWeight="bold" sx={{ 
                background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
                WebkitBackgroundClip: 'text',
                WebkitTextFillColor: 'transparent'
              }}>
                Upload History
              </Typography>
            </Box>
            
            {error && <Alert severity="error" sx={{ mb: 3 }}>{error}</Alert>}
            
            {history.length === 0 ? (
              <Paper sx={{ p: 6, textAlign: 'center', borderRadius: 3 }}>
                <Inbox sx={{ fontSize: 80, color: '#ccc', mb: 2 }} />
                <Typography variant="h5" color="text.secondary" gutterBottom>
                  No upload history yet
                </Typography>
                <Typography variant="body1" color="text.secondary">
                  Upload a CSV file from the Dashboard to see your history here
                </Typography>
              </Paper>
            ) : (
              <TableContainer component={Paper} sx={{ borderRadius: 3, boxShadow: '0 8px 24px rgba(0,0,0,0.12)' }}>
                <Table>
                  <TableHead>
                    <TableRow sx={{ background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)' }}>
                      <TableCell sx={{ color: 'white', fontWeight: 'bold', fontSize: '1rem' }}>Filename</TableCell>
                      <TableCell sx={{ color: 'white', fontWeight: 'bold', fontSize: '1rem' }}>Upload Date</TableCell>
                      <TableCell sx={{ color: 'white', fontWeight: 'bold', fontSize: '1rem' }}>Records</TableCell>
                      <TableCell sx={{ color: 'white', fontWeight: 'bold', fontSize: '1rem' }}>Avg Flowrate</TableCell>
                      <TableCell sx={{ color: 'white', fontWeight: 'bold', fontSize: '1rem' }}>Avg Pressure</TableCell>
                      <TableCell sx={{ color: 'white', fontWeight: 'bold', fontSize: '1rem' }}>Avg Temperature</TableCell>
                    </TableRow>
                  </TableHead>
                  <TableBody>
                    {history.map((item) => (
                      <TableRow 
                        key={item.id}
                        sx={{ 
                          '&:nth-of-type(odd)': { background: '#f8f9fa' },
                          '&:hover': { background: 'rgba(102, 126, 234, 0.05)' },
                          transition: 'background 0.3s ease'
                        }}
                      >
                        <TableCell>
                          <Box sx={{ display: 'flex', alignItems: 'center' }}>
                            <CheckCircle sx={{ color: '#43e97b', mr: 1, fontSize: 20 }} />
                            <Typography fontWeight="500">{item.original_filename}</Typography>
                          </Box>
                        </TableCell>
                        <TableCell>{new Date(item.uploaded_at).toLocaleString()}</TableCell>
                        <TableCell>
                          <Chip 
                            label={item.total_records} 
                            size="small" 
                            sx={{ 
                              background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
                              color: 'white',
                              fontWeight: 'bold'
                            }} 
                          />
                        </TableCell>
                        <TableCell>{item.avg_flowrate.toFixed(2)}</TableCell>
                        <TableCell>{item.avg_pressure.toFixed(2)}</TableCell>
                        <TableCell>{item.avg_temperature.toFixed(2)}</TableCell>
                      </TableRow>
                    ))}
                  </TableBody>
                </Table>
              </TableContainer>
            )}
          </Box>
        </Fade>
      </Container>
    </Box>
  );
}

export default History;
