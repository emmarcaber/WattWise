from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl

from ..uis.ui_print import Ui_PrintWindow
from app.views.main_menu_view import MainMenu


class PrintWindow(QMainWindow, Ui_PrintWindow):
    def __init__(
        self,
        student_name,
        student_id,
        test_controller,
        randomize_window=None,
    ):
        super().__init__()

        self.student_id = student_id
        self.student_name = student_name

        self.setupUi(self)
        self.setWindowTitle(f"WattWise | Print")
        self.randomize_window = randomize_window
        self.test_controller = test_controller

        self.modifyWindow()

        self.showMaximized()
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, False)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)

    def modifyWindow(self):
        self.add_web_view()
        self.btnBackMainMenu.clicked.connect(self.back_to_main_menu)
        self.btnPrint.clicked.connect(self.print_pdf)

    def print_pdf(self):
        # Prompt the user that the printing is happening
        msg = QMessageBox()
        msg.setWindowTitle("Success")
        msg.setIcon(QMessageBox.Information)
        msg.setText("WattWise is printing your questionnaire and answer sheet!")
        msg.exec()

        # Disable the print button after one click
        # To avoid spamming
        self.btnPrint.setEnabled(False)
        self.btnPrint.setStyleSheet(
            """
        QPushButton {
            background-color: #DDDDDD;
        }
            """
        )

        # Enable the backToMainMenu button
        self.btnBackMainMenu.setEnabled(True)
        self.btnBackMainMenu.setStyleSheet(
            """
        QPushButton {
            background-color: #4db8ff;
        }

        QPushButton:hover {
            background-color: #1AA4FF;
        }
            """
        )

        self.test_controller.print_questionnaire_answer_sheet()

    def back_to_main_menu(self):
        self.main_menu_window = MainMenu(
            self.student_name,
            self.student_id,
        )
        self.main_menu_window.show()
        self.hide()

    def add_web_view(self):
        layout = self.printFrame.layout()

        web_view = QWebEngineView()

        web_view.settings().setAttribute(
            web_view.settings().WebAttribute.PluginsEnabled, True
        )
        web_view.settings().setAttribute(
            web_view.settings().WebAttribute.PdfViewerEnabled, True
        )

        web_view.setUrl(
            QUrl.fromLocalFile(
                "C:/Users/Admin/Documents/GitHub/WattWise/app/print_check/Print.pdf"
            )
        )

        layout.addWidget(web_view)
