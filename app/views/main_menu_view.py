from PySide6.QtWidgets import QMainWindow
from ..uis.ui_main_menu import Ui_MainMenu

class MainMenu(QMainWindow, Ui_MainMenu):
    def __init__(self, student_name):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("WattWise | Main Menu")
        self.labelStudentName.setText(student_name + "!")

        self.showMaximized()

        self.modifyWindow()

    def modifyWindow(self):
        self.btnLogout.clicked.connect(self.logout)

    def logout(self):
        from app.views.login_view import LoginForm

        self.login_window = LoginForm()
        self.login_window.show()
        self.hide()
