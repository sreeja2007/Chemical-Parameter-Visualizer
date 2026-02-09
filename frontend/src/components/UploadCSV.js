import React, { useState } from 'react';
import { Button, Alert, Box, Snackbar } from '@mui/material';
import { CloudUpload } from '@mui/icons-material';
import { equipmentAPI } from '../services/api';

function UploadCSV({ onUploadSuccess }) {
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  const handleFileUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    setError('');
    setSuccess('');

    try {
      await equipmentAPI.uploadCSV(file);
      setSuccess('File uploaded successfully!');
      if (onUploadSuccess) onUploadSuccess();
    } catch (err) {
      setError(err.response?.data?.error || 'Upload failed');
    }
  };

  return (
    <Box sx={{ display: 'inline-block' }}>
      <Button 
        variant="contained" 
        component="label"
        startIcon={<CloudUpload />}
        sx={{
          background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
          fontWeight: 'bold',
          px: 3,
          '&:hover': {
            background: 'linear-gradient(135deg, #764ba2 0%, #667eea 100%)',
            transform: 'translateY(-2px)',
            boxShadow: '0 8px 20px rgba(102, 126, 234, 0.4)'
          },
          transition: 'all 0.3s ease'
        }}
      >
        Upload CSV
        <input type="file" accept=".csv" hidden onChange={handleFileUpload} />
      </Button>
      
      <Snackbar open={!!error} autoHideDuration={6000} onClose={() => setError('')}>
        <Alert severity="error" onClose={() => setError('')}>{error}</Alert>
      </Snackbar>
      
      <Snackbar open={!!success} autoHideDuration={3000} onClose={() => setSuccess('')}>
        <Alert severity="success" onClose={() => setSuccess('')}>{success}</Alert>
      </Snackbar>
    </Box>
  );
}

export default UploadCSV;
