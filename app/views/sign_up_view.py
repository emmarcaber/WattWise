from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt
from ..uis.ui_sign_up import Ui_SignUpWindow
from app.controllers.sign_up_controller import SignUpController
from app.models.user import User


class SignUpWindow(QMainWindow, Ui_SignUpWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("WattWise | Sign Up")

        self.showMaximized()
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, False)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)

        self.model = User
        self.controller = SignUpController(self, self.model)

        self.btnLogin.clicked.connect(self.open_login_window)

    def open_login_window(self):
        from app.views.login_view import LoginWindow

        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()
