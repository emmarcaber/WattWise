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

        self.btnLogin.clicked.connect(self.clicked_login)

        self.model = User
        self.controler = LoginController(self, self.model)

    def clicked_login(self):
       username = self.lineIDNumber.text()
       password = self.linePassword.text()

       print(username, password)