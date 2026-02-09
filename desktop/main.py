import sys
from PyQt5.QtWidgets import QApplication
from services.api_service import APIService
from ui.login_window import LoginWindow
from ui.dashboard_window import DashboardWindow

class MainApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.api_service = APIService()
        self.login_window = None
        self.dashboard_window = None
        self.show_login()
    
    def show_login(self):
        self.login_window = LoginWindow(self.api_service, self.show_dashboard)
        self.login_window.show()
    
    def show_dashboard(self):
        if self.login_window:
            self.login_window.close()
        self.dashboard_window = DashboardWindow(self.api_service)
        self.dashboard_window.show()
    
    def run(self):
        sys.exit(self.app.exec_())

if __name__ == '__main__':
    app = MainApp()
    app.run()
