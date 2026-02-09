from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, 
                             QTableWidget, QTableWidgetItem, QHeaderView, QFrame, QScrollArea)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class HistoryWindow(QWidget):
    def __init__(self, api_service):
        super().__init__()
        self.api_service = api_service
        self.init_ui()
        self.load_history()
    
    def init_ui(self):
        self.setWindowTitle('Upload History')
        self.setGeometry(100, 100, 1200, 700)
        self.setStyleSheet("""
            QWidget {
                background-color: #f8f9fa;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #667eea, stop:1 #764ba2);
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 8px;
                font-weight: bold;
                font-size: 13px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #764ba2, stop:1 #667eea);
            }
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)
        
        # Header
        header_layout = QHBoxLayout()
        title = QLabel('📋 Upload History')
        title.setFont(QFont('Segoe UI', 24, QFont.Bold))
        title.setStyleSheet('color: #667eea;')
        header_layout.addWidget(title)
        header_layout.addStretch()
        
        refresh_btn = QPushButton('🔄 Refresh')
        refresh_btn.clicked.connect(self.load_history)
        header_layout.addWidget(refresh_btn)
        
        layout.addLayout(header_layout)
        
        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            'Filename', 'Upload Date', 'Records', 'Avg Flowrate', 'Avg Pressure', 'Avg Temperature'
        ])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setStyleSheet("""
            QTableWidget {
                background: white;
                border-radius: 10px;
                gridline-color: #e0e0e0;
            }
            QHeaderView::section {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #667eea, stop:1 #764ba2);
                color: white;
                padding: 10px;
                border: none;
                font-weight: bold;
            }
            QTableWidget::item {
                padding: 10px;
            }
        """)
        self.table.setAlternatingRowColors(True)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        
        layout.addWidget(self.table)
        self.setLayout(layout)
    
    def load_history(self):
        success, data = self.api_service.get_history()
        if success and data:
            self.table.setRowCount(len(data))
            for row, item in enumerate(data):
                self.table.setItem(row, 0, QTableWidgetItem(item['original_filename']))
                # Parse datetime safely
                upload_date = item['uploaded_at']
                if 'T' in upload_date:
                    upload_date = upload_date.split('T')[0] + ' ' + upload_date.split('T')[1].split('.')[0]
                self.table.setItem(row, 1, QTableWidgetItem(upload_date))
                self.table.setItem(row, 2, QTableWidgetItem(str(item['total_records'])))
                self.table.setItem(row, 3, QTableWidgetItem(f"{item['avg_flowrate']:.2f}"))
                self.table.setItem(row, 4, QTableWidgetItem(f"{item['avg_pressure']:.2f}"))
                self.table.setItem(row, 5, QTableWidgetItem(f"{item['avg_temperature']:.2f}"))
        else:
            self.table.setRowCount(0)
