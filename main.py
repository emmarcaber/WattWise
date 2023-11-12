import sys

from PySide6.QtWidgets import QApplication
from app.views.login_view import LoginForm

def main():
    app = QApplication(sys.argv)

    # Create an instance of the LoginForm
    login_form = LoginForm()
    login_form.show()

    # Start the application event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()