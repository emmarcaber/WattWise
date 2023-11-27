from PySide6.QtWidgets import QMainWindow, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl

from ..uis.ui_print import Ui_PrintWindow
from app.views.main_menu_view import MainMenu


class PrintWindow(QMainWindow, Ui_PrintWindow):
    def __init__(
        self,
        student_name,
        student_id,
        randomize_window=None,
    ):
        super().__init__()

        self.student_id = student_id
        self.student_name = student_name

        self.setupUi(self)
        self.setWindowTitle(f"WattWise | Print")
        self.randomize_window = randomize_window

        self.showMaximized()
        self.modifyWindow()

    def modifyWindow(self):
        self.add_web_view()
        self.btnBackMainMenu.clicked.connect(self.back_to_main_menu)

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
                "C:/Users/caber/OneDrive/Documents/Coding/WattWise/app/print/final_paper.pdf"
            )
        )

        layout.addWidget(web_view)
