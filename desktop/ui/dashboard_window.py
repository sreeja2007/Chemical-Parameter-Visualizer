from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, 
                             QFileDialog, QMessageBox, QFrame, QGridLayout, QScrollArea, QSizePolicy)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class DashboardWindow(QWidget):
    def __init__(self, api_service):
        super().__init__()
        self.api_service = api_service
        self.current_data = None
        self.history_window = None
        self.init_ui()
        self.load_data()
    
    def init_ui(self):
        self.setWindowTitle('Chemical Equipment Visualizer - Dashboard')
        self.setGeometry(100, 100, 1400, 900)
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
                min-width: 100px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #764ba2, stop:1 #667eea);
            }
        """)
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet('QScrollArea { border: none; }')
        
        content_widget = QWidget()
        self.main_layout = QVBoxLayout(content_widget)
        self.main_layout.setSpacing(20)
        self.main_layout.setContentsMargins(30, 30, 30, 30)
        
        header_layout = QHBoxLayout()
        title = QLabel('Analytics Dashboard')
        title.setFont(QFont('Segoe UI', 24, QFont.Bold))
        title.setStyleSheet('color: #667eea;')
        header_layout.addWidget(title)
        header_layout.addStretch()
        
        self.upload_btn = QPushButton('Upload')
        self.upload_btn.clicked.connect(self.upload_csv)
        header_layout.addWidget(self.upload_btn)
        
        self.history_btn = QPushButton('History')
        self.history_btn.clicked.connect(self.show_history)
        header_layout.addWidget(self.history_btn)
        
        self.pdf_btn = QPushButton('PDF')
        self.pdf_btn.clicked.connect(self.download_pdf)
        header_layout.addWidget(self.pdf_btn)
        
        self.refresh_btn = QPushButton('Refresh')
        self.refresh_btn.clicked.connect(self.load_data)
        header_layout.addWidget(self.refresh_btn)
        
        self.logout_btn = QPushButton('Logout')
        self.logout_btn.setStyleSheet("""
            QPushButton {
                background: #dc3545;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 8px;
                font-weight: bold;
                font-size: 13px;
                min-width: 100px;
            }
            QPushButton:hover {
                background: #c82333;
            }
        """)
        self.logout_btn.clicked.connect(self.logout)
        header_layout.addWidget(self.logout_btn)
        
        self.main_layout.addLayout(header_layout)
        
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout()
        self.content_widget.setLayout(self.content_layout)
        self.main_layout.addWidget(self.content_widget)
        
        scroll.setWidget(content_widget)
        
        main_container = QVBoxLayout()
        main_container.setContentsMargins(0, 0, 0, 0)
        main_container.addWidget(scroll)
        self.setLayout(main_container)
    
    def show_history(self):
        from ui.history_window import HistoryWindow
        self.history_window = HistoryWindow(self.api_service)
        self.history_window.show()
    
    def show_empty_state(self):
        self.clear_content()
        
        empty_frame = QFrame()
        empty_frame.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #667eea, stop:1 #764ba2);
                border-radius: 20px;
            }
        """)
        empty_frame.setMinimumHeight(400)
        empty_layout = QVBoxLayout()
        empty_layout.setAlignment(Qt.AlignCenter)
        empty_layout.setContentsMargins(40, 40, 40, 40)
        
        icon_label = QLabel('☁️')
        icon_label.setStyleSheet('font-size: 100px; background: transparent;')
        icon_label.setAlignment(Qt.AlignCenter)
        empty_layout.addWidget(icon_label)
        
        welcome_label = QLabel('Welcome to Dashboard')
        welcome_label.setFont(QFont('Segoe UI', 28, QFont.Bold))
        welcome_label.setStyleSheet('color: white; background: transparent;')
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setWordWrap(True)
        empty_layout.addWidget(welcome_label)
        
        message_label = QLabel('No data yet. Upload CSV to start!')
        message_label.setFont(QFont('Segoe UI', 14))
        message_label.setStyleSheet('color: rgba(255, 255, 255, 0.9); background: transparent;')
        message_label.setAlignment(Qt.AlignCenter)
        message_label.setWordWrap(True)
        empty_layout.addWidget(message_label)
        
        upload_btn_large = QPushButton('Upload CSV File')
        upload_btn_large.setStyleSheet("""
            QPushButton {
                background: white;
                color: #667eea;
                border: none;
                padding: 18px 35px;
                border-radius: 12px;
                font-weight: bold;
                font-size: 16px;
                min-width: 200px;
            }
            QPushButton:hover {
                background: #f0f0f0;
            }
        """)
        upload_btn_large.clicked.connect(self.upload_csv)
        empty_layout.addWidget(upload_btn_large, alignment=Qt.AlignCenter)
        
        empty_frame.setLayout(empty_layout)
        self.content_layout.addWidget(empty_frame)
    
    def clear_content(self):
        while self.content_layout.count():
            item = self.content_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
    
    def load_data(self):
        success, data = self.api_service.get_latest_summary()
        if success:
            self.current_data = data
            self.update_ui()
        else:
            self.current_data = None
            self.show_empty_state()
    
    def create_kpi_card(self, label, value, color):
        card = QFrame()
        card.setStyleSheet(f"""
            QFrame {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 {color}, stop:1 {color}dd);
                border-radius: 12px;
            }}
        """)
        card.setMinimumHeight(120)
        card.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(15, 15, 15, 15)
        
        label_text = QLabel(label)
        label_text.setStyleSheet('color: white; font-size: 12px; font-weight: bold; background: transparent;')
        label_text.setWordWrap(True)
        layout.addWidget(label_text)
        
        value_text = QLabel(str(value))
        value_text.setFont(QFont('Segoe UI', 26, QFont.Bold))
        value_text.setStyleSheet('color: white; background: transparent;')
        layout.addWidget(value_text)
        
        card.setLayout(layout)
        return card
    
    def update_ui(self):
        if not self.current_data:
            self.show_empty_state()
            return
        
        self.clear_content()
        
        kpi_layout = QGridLayout()
        kpi_layout.setSpacing(15)
        
        kpis = [
            ('Total Records', self.current_data['total_records'], '#667eea'),
            ('Avg Flowrate', f"{self.current_data['avg_flowrate']:.2f}", '#764ba2'),
            ('Avg Pressure', f"{self.current_data['avg_pressure']:.2f}", '#f093fb'),
            ('Avg Temp', f"{self.current_data['avg_temperature']:.2f}", '#4facfe')
        ]
        
        for i, (label, value, color) in enumerate(kpis):
            card = self.create_kpi_card(label, value, color)
            kpi_layout.addWidget(card, 0, i)
        
        self.content_layout.addLayout(kpi_layout)
        
        charts_layout = QHBoxLayout()
        charts_layout.setSpacing(15)
        
        type_dist = self.current_data['type_distribution']
        
        pie_frame = self.create_chart_frame('Type Distribution')
        fig = Figure(figsize=(5, 4), dpi=80)
        ax = fig.add_subplot(111)
        ax.pie(type_dist.values(), labels=type_dist.keys(), autopct='%1.1f%%', startangle=90)
        fig.tight_layout()
        pie_canvas = FigureCanvas(fig)
        pie_canvas.setMinimumSize(QSize(300, 300))
        pie_frame.layout().addWidget(pie_canvas)
        charts_layout.addWidget(pie_frame)
        
        bar_frame = self.create_chart_frame('Flowrate')
        fig = Figure(figsize=(5, 4), dpi=80)
        ax = fig.add_subplot(111)
        ax.bar(list(type_dist.keys()), [self.current_data['avg_flowrate']] * len(type_dist), color='#667eea')
        ax.set_ylabel('Value')
        fig.tight_layout()
        bar_canvas = FigureCanvas(fig)
        bar_canvas.setMinimumSize(QSize(300, 300))
        bar_frame.layout().addWidget(bar_canvas)
        charts_layout.addWidget(bar_frame)
        
        line_frame = self.create_chart_frame('Pressure & Temp')
        fig = Figure(figsize=(5, 4), dpi=80)
        ax = fig.add_subplot(111)
        ax.plot(['Pressure', 'Temperature'], 
                [self.current_data['avg_pressure'], self.current_data['avg_temperature']], 
                marker='o', linestyle='-', color='#764ba2', linewidth=2)
        ax.set_ylabel('Value')
        ax.grid(True, alpha=0.3)
        fig.tight_layout()
        line_canvas = FigureCanvas(fig)
        line_canvas.setMinimumSize(QSize(300, 300))
        line_frame.layout().addWidget(line_canvas)
        charts_layout.addWidget(line_frame)
        
        self.content_layout.addLayout(charts_layout)
    
    def create_chart_frame(self, title):
        frame = QFrame()
        frame.setStyleSheet("""
            QFrame {
                background: white;
                border-radius: 12px;
            }
        """)
        frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout = QVBoxLayout()
        layout.setContentsMargins(15, 15, 15, 15)
        
        title_label = QLabel(title)
        title_label.setFont(QFont('Segoe UI', 13, QFont.Bold))
        title_label.setStyleSheet('color: #667eea; background: transparent;')
        layout.addWidget(title_label)
        
        frame.setLayout(layout)
        return frame
    
    def upload_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Select CSV File', '', 'CSV Files (*.csv)')
        if file_path:
            try:
                success, data = self.api_service.upload_csv(file_path)
                if success:
                    QMessageBox.information(self, 'Success', 'File uploaded successfully!')
                    self.load_data()
                else:
                    error_msg = str(data.get('error', 'Upload failed')) if isinstance(data, dict) else str(data)
                    QMessageBox.warning(self, 'Error', error_msg)
            except Exception as e:
                QMessageBox.warning(self, 'Error', f'Upload failed: {str(e)}')
    
    def download_pdf(self):
        if not self.current_data:
            QMessageBox.warning(self, 'No Data', 'Please upload data first.')
            return
            
        save_path, _ = QFileDialog.getSaveFileName(self, 'Save PDF Report', '', 'PDF Files (*.pdf)')
        if save_path:
            success = self.api_service.download_pdf(save_path)
            if success:
                QMessageBox.information(self, 'Success', 'PDF downloaded!')
            else:
                QMessageBox.warning(self, 'Error', 'Failed to download PDF')
    
    def logout(self):
        reply = QMessageBox.question(self, 'Logout', 'Are you sure you want to logout?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.api_service.logout()
            self.close()
            from ui.login_window import LoginWindow
            self.login_window = LoginWindow()
            self.login_window.show()
