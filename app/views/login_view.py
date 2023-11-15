from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon
from PySide6.QtCore import QDateTime
from ..uis.ui_login import Ui_MainWindow
from app.controllers.login_controller import LoginController
from app.models.user import User

class LoginForm(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.setWindowTitle("WattWise | Login")
        self.showMaximized()

        self.model = User
        self.controler = LoginController(self, self.model)

