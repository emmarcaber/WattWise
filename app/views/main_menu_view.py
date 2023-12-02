from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt
from ..uis.ui_main_menu import Ui_MainMenu


class MainMenu(QMainWindow, Ui_MainMenu):
    def __init__(self, student_name, student_id):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("WattWise | Main Menu")

        self.student_name = student_name
        self.student_id = student_id
        self.labelStudentName.setText(student_name + "!")

        self.showMaximized()
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, False)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)

        self.modifyWindow()

    def modifyWindow(self):
        self.btnLogout.clicked.connect(self.open_login_window)
        self.btnGenerate.clicked.connect(self.open_categories_window)
        self.btnCheck.clicked.connect(self.open_check_window)

    def open_categories_window(self):
        from app.views.categories_view import CategoriesWindow

        self.categories_window = CategoriesWindow(
            self.student_name, self.student_id, main_menu_window=self
        )
        self.categories_window.show()
        self.hide()

    def open_login_window(self):
        from app.views.login_view import LoginWindow

        self.login_window = LoginWindow()
        self.login_window.show()
        self.hide()

    def open_check_window(self):
        from app.views.check_view import CheckWindow

        self.check_window = CheckWindow(
            self.student_name, self.student_id, main_menu_window=self
        )
        self.check_window.show()
        self.hide()
