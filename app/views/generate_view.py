from PySide6.QtWidgets import QMainWindow
from ..uis.ui_generate import Ui_Generate
from app.views.main_menu_view import MainMenu

class GenerateWindow(QMainWindow, Ui_Generate):
    def __init__(self, student_name, main_menu_window = None):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("WattWise | Generate")
        self.student_name = student_name
        self.main_menu_window = main_menu_window

        self.showMaximized()

        self.modifyWindow()

    def modifyWindow(self):
        self.btnBack.clicked.connect(self.back_to_main_menu)

    def back_to_main_menu(self):
        if self.back_to_main_menu:
            self.main_menu_window.show()

        # print("back")
        self.close()
