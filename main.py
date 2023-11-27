import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from app.views.login_view import LoginWindow


def main():
    QApplication.setAttribute(Qt.AA_ShareOpenGLContexts, True)

    app = QApplication(sys.argv)

    # Create an instance of the LoginWindow
    login_form = LoginWindow()
    login_form.show()

    # Start the application event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
