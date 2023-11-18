from PySide6.QtWidgets import QMainWindow
from ..uis.ui_main_menu import Ui_MainMenu

class MainMenu(QMainWindow, Ui_MainMenu):
    def __init__(self, student_name):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("WattWise | Main Menu")

        self.student_name = student_name
        self.labelStudentName.setText(student_name + "!")

        self.showMaximized()

        self.modifyWindow()

    def modifyWindow(self):
        self.btnLogout.clicked.connect(self.open_logout_window)
        self.btnGenerate.clicked.connect(self.open_generate_window)

    def open_generate_window(self):
        from app.views.generate_view import GenerateWindow
        
        self.generate_window = GenerateWindow(self.student_name, main_menu_window = self)
        self.generate_window.show()
        self.hide()

    def open_logout_window(self):
        from app.views.login_view import LoginWindow

        self.login_window = LoginWindow()
        self.login_window.show()
        self.hide()
