from PySide6.QtWidgets import QMainWindow
from ..uis.ui_categories import Ui_CategoriesWindow
from app.views.eeps_subcategories_view import EEPSWindow
from app.views.esas_subcategories_view import ESASWindow
from app.views.math_subcategories_view import MathWindow


class CategoriesWindow(QMainWindow, Ui_CategoriesWindow):
    def __init__(self, student_name, student_id, main_menu_window=None):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("WattWise | Generate")
        self.student_name = student_name
        self.student_id = student_id
        self.main_menu_window = main_menu_window

        self.showMaximized()

        self.modifyWindow()

    def modifyWindow(self):
        self.btnBack.clicked.connect(self.back_to_main_menu)
        self.btnEEPS.clicked.connect(self.open_EEPSWindow)
        self.btnESAS.clicked.connect(self.open_ESASWindow)
        self.btnMathematics.clicked.connect(self.open_MathWindow)

    def open_EEPSWindow(self):
        self.eeps_window = EEPSWindow(self.student_name, self.student_id, self)
        self.eeps_window.show()
        self.hide()

    def open_ESASWindow(self):
        self.esas_window = ESASWindow(self.student_name, self.student_id, self)
        self.esas_window.show()
        self.hide()

    def open_MathWindow(self):
        self.math_window = MathWindow(self.student_name, self.student_id, self)
        self.math_window.show()
        self.hide()

    def back_to_main_menu(self):
        if self.back_to_main_menu:
            self.main_menu_window.show()

        # print("back")
        self.close()
