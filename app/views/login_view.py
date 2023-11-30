from PySide6.QtWidgets import QMainWindow, QLabel
from PySide6.QtCore import Qt
from ..uis.ui_login import Ui_LoginWindow
from app.controllers.login_controller import LoginController
from app.models.user import User
from app.views.sign_up_view import SignUpWindow


class LoginWindow(QMainWindow, Ui_LoginWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("WattWise | Login")
        self.showMaximized()
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, False)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)

        self.model = User()
        self.controller = LoginController(self, self.model)

        self.btnSignUp.clicked.connect(self.open_sign_up_window)

    def open_sign_up_window(self):
        self.open_sign_up_window = SignUpWindow()
        self.open_sign_up_window.show()
        self.close()
