from PySide6.QtWidgets import QMainWindow, QMessageBox, QLabel
from PySide6.QtCore import Qt, QTimer, Slot

from ..uis.ui_profile import Ui_ProfileWindow
from app.views.main_menu_view import MainMenu

import cv2
import os


class ProfileWindow(QMainWindow, Ui_ProfileWindow):
    def __init__(self, student_name, student_id, main_menu_window=None):
        super().__init__()

        self.student_name = student_name
        self.student_id = student_id
        self.main_menu_window = main_menu_window

        self.setupUi(self)
        self.setWindowTitle(f"WattWise | Profile")

        self.modifyWindow()

        self.showMaximized()
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, False)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)

    def modifyWindow(self):
        pass
