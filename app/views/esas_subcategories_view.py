from PySide6.QtWidgets import QMainWindow
from ..uis.ui_esas_subcategories import Ui_ESASWindow

class ESASWindow(QMainWindow, Ui_ESASWindow):
    def __init__(self, student_name, generate_window = None):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("WattWise | ESAS")
        self.student_name = student_name
        self.generate_window = generate_window

        self.showMaximized()

        self.modifyWindow()

    def modifyWindow(self):
        self.btnBack.clicked.connect(self.back_to_generate_window)

    def back_to_generate_window(self):
        if self.back_to_generate_window:
            self.generate_window.show()

        # print("back")
        self.close()
