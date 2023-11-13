from PySide6.QtWidgets import QMainWindow
from ..uis.ui_main_menu import Ui_MainWindow


class MainMenu(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("WattWise | Main Menu")
