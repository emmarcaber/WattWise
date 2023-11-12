from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon
from PySide6.QtCore import QDateTime
from ..uis.ui_login import Ui_MainWindow
from app.controllers.login_controller import LoginController
from app.models.user import User

class LoginForm(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.setWindowTitle("WattWise | Login")
        
        self.btnLetterC.clicked.connect(self.letterC_to_idNumber)
        self.btnOne.clicked.connect(self.one_to_idNumber)
        self.btnTwo.clicked.connect(self.two_to_idNumber)
        self.btnThree.clicked.connect(self.three_to_idNumber)
        self.btnFour.clicked.connect(self.four_to_idNumber)
        self.btnFive.clicked.connect(self.five_to_idNumber)
        self.btnSix.clicked.connect(self.six_to_idNumber)
        self.btnSeven.clicked.connect(self.seven_to_idNumber)
        self.btnEight.clicked.connect(self.eight_to_idNumber)
        self.btnNine.clicked.connect(self.nine_to_idNumber)
        self.btnZero.clicked.connect(self.zero_to_idNumber)
        self.btnDelete.clicked.connect(self.delete_char_in_idNumber)
        
        self.update_datetime()
        self.timer = self.startTimer(1000)
        
        self.model = User 
        self.controller = LoginController(self, self.model)
    
    
    
    def update_datetime(self):
        current_datetime = QDateTime.currentDateTime()

        # Update date label
        formatted_date = current_datetime.toString('MMMM dd, yyyy')
        self.dateLabel.setText(formatted_date)

        # Update time label
        formatted_time = current_datetime.toString('hh:mm:ss AP')
        self.timeLabel.setText(formatted_time)
    
    
    def timerEvent(self, event):
        if event.timerId() == self.timer:
            self.update_datetime()
        else:
            super().timerEvent(event)
    
    def letterC_to_idNumber(self):
        current_text = self.txtIDNumber.text()
        self.txtIDNumber.setText(current_text + "C")
        
    def one_to_idNumber(self):
        current_text = self.txtIDNumber.text()
        self.txtIDNumber.setText(current_text + "1")
        
    def two_to_idNumber(self):
        current_text = self.txtIDNumber.text()
        self.txtIDNumber.setText(current_text + "2")
        
    def three_to_idNumber(self):
        current_text = self.txtIDNumber.text()
        self.txtIDNumber.setText(current_text + "3")
        
    def four_to_idNumber(self):
        current_text = self.txtIDNumber.text()
        self.txtIDNumber.setText(current_text + "4")
        
    def five_to_idNumber(self):
        current_text = self.txtIDNumber.text()
        self.txtIDNumber.setText(current_text + "5")
        
    def six_to_idNumber(self):
        current_text = self.txtIDNumber.text()
        self.txtIDNumber.setText(current_text + "6")
        
    def seven_to_idNumber(self):
        current_text = self.txtIDNumber.text()
        self.txtIDNumber.setText(current_text + "7")
        
    def eight_to_idNumber(self):
        current_text = self.txtIDNumber.text()
        self.txtIDNumber.setText(current_text + "8")
        
    def nine_to_idNumber(self):
        current_text = self.txtIDNumber.text()
        self.txtIDNumber.setText(current_text + "9")
        
    def zero_to_idNumber(self):
        current_text = self.txtIDNumber.text()
        self.txtIDNumber.setText(current_text + "0")
        
    def delete_char_in_idNumber(self):
        current_text = self.txtIDNumber.text()
        if current_text:
            new_text = current_text[:-1]  # Remove the last character
            self.txtIDNumber.setText(new_text)
