from PySide6.QtCore import QObject
from PySide6.QtWidgets import QMessageBox, QMainWindow
from app.models.user import User
from app.views.main_menu_view import MainMenu

class LoginController(QObject):
    def __init__(self, view, model):
        super().__init__()

        self.view = view
        self.model = model

        # Connect signals from the view to controller methods
        self.view.btnLogin.clicked.connect(self.verify_student)
        self.all_users = User.read_users()
        # print(self.all_users)

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
        self.view.linePassword.setText("")

    def verify_student(self):
        student_id = self.view.lineIDNumber.text()
        student_password = self.view.linePassword.text()

        if not student_id or not student_password:
            msg = self.message_box_error("Please fill in all the fields!")
            msg.exec()

        # Verify if there is existing student ID number in DB
        elif (self.all_users.get(student_id)):
            current_student = self.all_users.get(student_id)

            if current_student['password'] == student_password:
                msg = QMessageBox()
                msg.setWindowTitle("Success")
                msg.setIcon(QMessageBox.Information)
                msg.setText("Successfully login!")
                msg.exec()
                
                self.main_menu_window = MainMenu()
                self.main_menu_window.show()
                self.view.hide()
                

            else:
                self.invalid_credentials_error()

        else:
            self.invalid_credentials_error()