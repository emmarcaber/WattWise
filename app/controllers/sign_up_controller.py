from PySide6.QtCore import QObject
from PySide6.QtWidgets import QMessageBox, QMainWindow
from app.models.user import User
from app.views.main_menu_view import MainMenu


class SignUpController(QObject):
    def __init__(self, view, model):
        super().__init__()

        self.view = view
        self.model = model

        # Connect signals from the view to controller methods
        self.view.btnSignUp.clicked.connect(self.verify_info)
        self.student_names = User.read_student_names()
        self.id_numbers = User.read_id_numbers()
        # print(self.id_numbers)

    def message_box_error(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setIcon(QMessageBox.Critical)
        msg.setText(text)
        return msg

    def invalid_credentials_error(self):
        msg = self.message_box_error("Invalid ID Number or Password!")
        msg.exec()

        # Empty the fields
        self.empty_fields()

    def empty_fields(self):
        self.view.lineFirstName.setText("")
        self.view.lineLastName.setText("")
        self.view.lineIDNumber.setText("")
        self.view.linePassword.setText("")
        self.view.lineConfirmPassword.setText("")

    def verify_info(self):
        student_first_name = self.view.lineFirstName.text()
        student_last_name = self.view.lineLastName.text()
        student_id = self.view.lineIDNumber.text()
        student_password = self.view.linePassword.text()
        confirm_password = self.view.lineConfirmPassword.text()

        # print(student_first_name, student_last_name, student_id, student_password, confirm_password)

        if (
            not student_first_name
            or not student_last_name
            or not student_id
            or not student_password
            or not confirm_password
        ):
            msg = self.message_box_error("Please fill in all the fields!")
            msg.exec()

        elif f"{student_first_name} {student_last_name}" in self.student_names:
            msg = self.message_box_error("Student name has been already registered!")
            msg.exec()
            self.empty_fields()

        elif student_id in self.id_numbers:
            msg = self.message_box_error(
                "Student ID Number has been already registered!"
            )
            msg.exec()
            self.empty_fields()

        elif student_password != confirm_password:
            msg = self.message_box_error("Password does not matched!")
            msg.exec()
            self.view.lineConfirmPassword.setText("")

        else:
            User.register_user(
                student_first_name, student_last_name, student_id, student_password
            )

            # Prompt a messagebox
            msg = QMessageBox()
            msg.setWindowTitle("Success")
            msg.setIcon(QMessageBox.Information)
            msg.setText("Student has been registered successfully!")
            msg.exec()

            # Redirect automatically to main menu
            self.main_menu_window = MainMenu(
                f"{student_first_name} {student_last_name}", student_id
            )
            self.main_menu_window.show()
            self.view.hide()
