from PySide6.QtWidgets import (
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
)
from PySide6.QtCore import Qt, QTimer, Slot

from ..uis.ui_profile import Ui_ProfileWindow
from app.views.main_menu_view import MainMenu
from app.models.test import Test

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
        self.database_methods()
        self.setup_text_labels()
        self.populate_table(self.testsTable)

        self.btnBackMainMenu.clicked.connect(self.back_to_main_menu)

    def setup_text_labels(self):
        self.labelName.setText(self.student_name)
        self.labelTotalTaken.setText(self.total_tests)
        self.labelESASTaken.setText(self.esas_taken)
        self.labelMathTaken.setText(self.math_taken)
        self.labelEEPSTaken.setText(self.eeps_taken)

    def database_methods(self):
        test = Test()

        self.total_tests = str(test.get_total_tests_of_user(self.student_id))
        self.esas_taken, self.math_taken, self.eeps_taken = [
            str(title)
            for title in test.get_total_tests_per_subcategory_of_user(self.student_id)
        ]
        self.tests = test.get_tests_from_db(self.student_id)

    def populate_table(self, table_widget):
        # Populate the table with some sample data
        for row, row_data in enumerate(self.tests):
            table_widget.insertRow(row)
            for col, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data) if col_data != None else "")
                table_widget.setItem(row, col, item)

    def back_to_main_menu(self):
        if self.back_to_main_menu:
            self.main_menu_window.show()

        self.close()
