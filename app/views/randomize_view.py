from PySide6.QtWidgets import QMainWindow
from ..uis.ui_randomize import Ui_RandomizeWindow

class RandomizeWindow(QMainWindow, Ui_RandomizeWindow):

    def __init__(self, window_title, questions,subcategories_window = None):
        super().__init__()
        
        # Get the questions
        self.questions = questions

        # count = 1
        # for question_text in selected_questions:
        #     question_data = formatted_questions[question_text]
        #     print(f"{count}. Question: {question_text}")
        #     print("Options:")
        #     for option, text in question_data['options'].items():
        #         print(f"{option}: {text}")
        #     print(f"Correct Option: {question_data['correct_option']}")
        #     print()
        #     count += 1

        self.setupUi(self)
        self.setWindowTitle(f"WattWise | {window_title}")
        self.labelSubcategory.setText(window_title)

        self.subcategories_window = subcategories_window

        self.showMaximized()
        self.modifyWindow()


    def modifyWindow(self):

        self.btnBack.clicked.connect(self.back_to_subcategories_window)
        self.add_questions_to_textEdit()


    def add_questions_to_textEdit(self):
        self.txtEditQuestions.setPlainText(f"1. {self.questions[0]} \n")

        for question in list(self.questions.keys()):
            prev_content = self.txtEditQuestions.toPlainText()
            # self.txtEditQuestions.setPlainText(f"{prevContent}")
            print(question)

    
    def back_to_subcategories_window(self):
        if self.subcategories_window:
            self.subcategories_window.show()

        self.hide()
