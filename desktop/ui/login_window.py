from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class LoginWindow(QWidget):
    def __init__(self, api_service, on_login_success):
        super().__init__()
        self.api_service = api_service
        self.on_login_success = on_login_success
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle('Chemical Equipment Visualizer - Login')
        self.setFixedSize(400, 500)
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #667eea, stop:1 #764ba2);
            }
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(15)
        
        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background: white;
                border-radius: 12px;
            }
        """)
        
        card_layout = QVBoxLayout()
        card_layout.setContentsMargins(25, 25, 25, 25)
        card_layout.setSpacing(12)
        
        icon = QLabel('🧪')
        icon.setStyleSheet('font-size: 50px; background: transparent;')
        icon.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(icon)
        
        title = QLabel('Chemical Equipment')
        title.setFont(QFont('Segoe UI', 16, QFont.Bold))
        title.setStyleSheet('color: #667eea; background: transparent;')
        title.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(title)
        
        subtitle = QLabel('Parameter Visualizer')
        subtitle.setFont(QFont('Segoe UI', 12, QFont.Bold))
        subtitle.setStyleSheet('color: #764ba2; background: transparent; margin-bottom: 10px;')
        subtitle.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(subtitle)
        
        username_label = QLabel('Username')
        username_label.setFont(QFont('Segoe UI', 9, QFont.Bold))
        username_label.setStyleSheet('color: #2c3e50; background: transparent;')
        card_layout.addWidget(username_label)
        
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText('Enter username')
        self.username_input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 2px solid #e0e0e0;
                border-radius: 5px;
                font-size: 12px;
                background: white;
            }
            QLineEdit:focus {
                border: 2px solid #667eea;
            }
        """)
        card_layout.addWidget(self.username_input)
        
        password_label = QLabel('Password')
        password_label.setFont(QFont('Segoe UI', 9, QFont.Bold))
        password_label.setStyleSheet('color: #2c3e50; background: transparent;')
        card_layout.addWidget(password_label)
        
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText('Enter password')
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 2px solid #e0e0e0;
                border-radius: 5px;
                font-size: 12px;
                background: white;
            }
            QLineEdit:focus {
                border: 2px solid #667eea;
            }
        """)
        card_layout.addWidget(self.password_input)
        
        login_btn = QPushButton('Login')
        login_btn.clicked.connect(self.handle_login)
        login_btn.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #667eea, stop:1 #764ba2);
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
                font-size: 13px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #764ba2, stop:1 #667eea);
            }
        """)
        card_layout.addWidget(login_btn)
        
        register_btn = QPushButton('Register')
        register_btn.clicked.connect(self.handle_register)
        register_btn.setStyleSheet("""
            QPushButton {
                background: white;
                color: #667eea;
                border: 2px solid #667eea;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
                font-size: 13px;
            }
            QPushButton:hover {
                background: #f8f9fa;
            }
        """)
        card_layout.addWidget(register_btn)
        
        card.setLayout(card_layout)
        layout.addWidget(card)
        self.setLayout(layout)
    
    def handle_login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        
        if not username or not password:
            QMessageBox.warning(self, 'Error', 'Please enter username and password')
            return
        
        success, data = self.api_service.login(username, password)
        if success:
            QMessageBox.information(self, 'Success', 'Login successful!')
            self.on_login_success()
        else:
            QMessageBox.warning(self, 'Error', data.get('error', 'Login failed'))
    
    def handle_register(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        
        if not username or not password:
            QMessageBox.warning(self, 'Error', 'Please enter username and password')
            return
        
        success, data = self.api_service.register(username, '', password)
        if success:
            QMessageBox.information(self, 'Success', 'Registration successful!')
            self.on_login_success()
        else:
            QMessageBox.warning(self, 'Error', str(data))
