import React, { useState, useEffect } from 'react';
import { Container, Grid, Paper, Typography, Box, Button, CircularProgress, Divider } from '@mui/material';
import { CloudUpload } from '@mui/icons-material';
import { Chart as ChartJS, ArcElement, CategoryScale, LinearScale, BarElement, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js';
import { Pie, Bar, Line } from 'react-chartjs-2';
import { equipmentAPI, reportAPI } from '../services/api';
import UploadCSV from '../components/UploadCSV';

ChartJS.register(ArcElement, CategoryScale, LinearScale, BarElement, PointElement, LineElement, Title, Tooltip, Legend);

function Dashboard() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  const fetchData = async () => {
    setLoading(true);
    try {
      const response = await equipmentAPI.getLatestSummary();
      setData(response.data);
    } catch (error) {
      console.error('Error fetching data:', error);
      setData(null);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleDownloadPDF = async () => {
    try {
      const response = await reportAPI.downloadPDF();
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', `equipment_report_${Date.now()}.pdf`);
      document.body.appendChild(link);
      link.click();
      link.remove();
    } catch (error) {
      console.error('Error downloading PDF:', error);
    }
  };

  if (loading) return (
    <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '80vh' }}>
      <CircularProgress />
    </Box>
  );
  
  if (!data) return (
    <Box sx={{ bgcolor: '#f5f5f5', minHeight: '100vh', display: 'flex', alignItems: 'center', py: 4 }}>
      <Container maxWidth="md">
        <Paper sx={{ p: 6, textAlign: 'center' }}>
          <CloudUpload sx={{ fontSize: 80, color: '#1976d2', mb: 3 }} />
          <Typography variant="h4" fontWeight="600" gutterBottom>
            No Data Available
          </Typography>
          <Typography variant="body1" color="text.secondary" sx={{ mb: 4 }}>
            Upload a CSV file to begin analyzing your equipment data
          </Typography>
          <UploadCSV onUploadSuccess={fetchData} />
          <Typography variant="caption" color="text.secondary" sx={{ mt: 2, display: 'block' }}>
            Required: Equipment Name, Type, Flowrate, Pressure, Temperature
          </Typography>
        </Paper>
      </Container>
    </Box>
  );

  const pieData = {
    labels: Object.keys(data.type_distribution),
    datasets: [{
      data: Object.values(data.type_distribution),
      backgroundColor: ['#1976d2', '#388e3c', '#f57c00', '#d32f2f', '#7b1fa2', '#0097a7'],
      borderWidth: 0
    }]
  };

  const barData = {
    labels: Object.keys(data.type_distribution),
    datasets: [{
      label: 'Flowrate',
      data: Object.keys(data.type_distribution).map(() => data.avg_flowrate),
      backgroundColor: '#1976d2',
      borderRadius: 4
    }]
  };

  const lineData = {
    labels: ['Pressure', 'Temperature'],
    datasets: [{
      label: 'Values',
      data: [data.avg_pressure, data.avg_temperature],
      borderColor: '#1976d2',
      backgroundColor: 'rgba(25, 118, 210, 0.1)',
      borderWidth: 2,
      pointRadius: 4,
      pointBackgroundColor: '#1976d2'
    }]
  };

  const chartOptions = {
    responsive: true,
    maintainAspectRatio: true,
    plugins: {
      legend: {
        position: 'bottom',
        labels: {
          padding: 15,
          font: { size: 12 }
        }
      }
    }
  };

  return (
    <Box sx={{ bgcolor: '#f5f5f5', minHeight: '100vh', py: 3 }}>
      <Container maxWidth="lg">
        <Box sx={{ mb: 3, display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <Box>
            <Typography variant="h4" fontWeight="600" gutterBottom>
              Equipment Analytics
            </Typography>
            <Typography variant="body2" color="text.secondary">
              {data.original_filename} • {data.total_records} records
            </Typography>
          </Box>
          <Box sx={{ display: 'flex', gap: 2 }}>
            <UploadCSV onUploadSuccess={fetchData} />
            <Button variant="outlined" onClick={handleDownloadPDF}>
              Export PDF
            </Button>
          </Box>
        </Box>

        <Grid container spacing={2} sx={{ mb: 3 }}>
          {[
            { label: 'Total Records', value: data.total_records },
            { label: 'Avg Flowrate', value: data.avg_flowrate.toFixed(2) },
            { label: 'Avg Pressure', value: data.avg_pressure.toFixed(2) },
            { label: 'Avg Temperature', value: data.avg_temperature.toFixed(2) }
          ].map((item, index) => (
            <Grid item xs={12} sm={6} md={3} key={index}>
              <Paper sx={{ p: 2.5 }}>
                <Typography variant="body2" color="text.secondary" gutterBottom>
                  {item.label}
                </Typography>
                <Typography variant="h4" fontWeight="600">
                  {item.value}
                </Typography>
              </Paper>
            </Grid>
          ))}
        </Grid>

        <Grid container spacing={2}>
          {[
            { title: 'Equipment Distribution', chart: <Pie data={pieData} options={chartOptions} /> },
            { title: 'Flowrate Analysis', chart: <Bar data={barData} options={chartOptions} /> },
            { title: 'Pressure vs Temperature', chart: <Line data={lineData} options={chartOptions} /> }
          ].map((item, index) => (
            <Grid item xs={12} md={4} key={index}>
              <Paper sx={{ p: 2.5 }}>
                <Typography variant="h6" fontWeight="600" gutterBottom>
                  {item.title}
                </Typography>
                <Divider sx={{ mb: 2 }} />
                {item.chart}
              </Paper>
            </Grid>
          ))}
        </Grid>
      </Container>
    </Box>
  );
}

export default Dashboard;
