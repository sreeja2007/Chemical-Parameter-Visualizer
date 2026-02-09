import requests

class APIService:
    BASE_URL = 'http://localhost:8000/api'
    
    def __init__(self):
        self.token = None
    
    def login(self, username, password):
        response = requests.post(f'{self.BASE_URL}/auth/login', json={
            'username': username,
            'password': password
        })
        if response.status_code == 200:
            data = response.json()
            self.token = data['access']
            return True, data
        return False, response.json()
    
    def register(self, username, email, password):
        response = requests.post(f'{self.BASE_URL}/auth/register', json={
            'username': username,
            'email': email,
            'password': password
        })
        if response.status_code == 201:
            data = response.json()
            self.token = data['access']
            return True, data
        return False, response.json()
    
    def upload_csv(self, file_path):
        headers = {'Authorization': f'Bearer {self.token}'}
        with open(file_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(f'{self.BASE_URL}/upload', files=files, headers=headers)
        return response.status_code == 201, response.json()
    
    def get_latest_summary(self):
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.get(f'{self.BASE_URL}/summary/latest', headers=headers)
        if response.status_code == 200:
            return True, response.json()
        return False, None
    
    def get_history(self):
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.get(f'{self.BASE_URL}/history', headers=headers)
        if response.status_code == 200:
            return True, response.json()
        return False, None
    
    def download_pdf(self, save_path):
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.get(f'{self.BASE_URL}/report/pdf', headers=headers)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            return True
        return False
    
    def logout(self):
        self.token = None
