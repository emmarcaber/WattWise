from PySide6.QtCore import QObject
from app.models.user import User

class LoginController(QObject):
    def __init__(self, view, model):
        super().__init__()

        self.view = view
        self.model = model

        # Connect signals from the view to controller methods
        self.all_users = User.read_users()
        print(self.all_users)

    def verify_student(self):
        student_id = self.view.txtIDNumber.text()

        if (self.all_users.get(student_id)):
            user = self.all_users[student_id]
            print(user['first_name'], user['last_name'])
        