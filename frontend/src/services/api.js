import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.request.use(
  (config) => {
    // Don't add token for auth endpoints
    if (!config.url.includes('/auth/')) {
      const token = localStorage.getItem('access_token');
      if (token) {
        config.headers.Authorization = `Bearer ${token}`;
      }
    }
    return config;
  },
  (error) => Promise.reject(error)
);

export const authAPI = {
  register: (data) => api.post('/auth/register', data),
  login: (data) => api.post('/auth/login', data),
};

export const equipmentAPI = {
  uploadCSV: (file) => {
    const formData = new FormData();
    formData.append('file', file);
    return api.post('/upload', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    });
  },
  getLatestSummary: () => api.get('/summary/latest'),
  getHistory: () => api.get('/history'),
  getDatasetDetail: (id) => api.get(`/history/${id}`),
};

export const reportAPI = {
  downloadPDF: () => api.get('/report/pdf', { responseType: 'blob' }),
};

export default api;
