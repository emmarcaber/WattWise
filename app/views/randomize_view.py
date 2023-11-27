from PySide6.QtWidgets import QMainWindow, QMessageBox

from ..uis.ui_randomize import Ui_RandomizeWindow
import random


class RandomizeWindow(QMainWindow, Ui_RandomizeWindow):
    def __init__(self, window_title, questions, subcategories_window=None):
        super().__init__()

        # Get the questions
        self.questions = questions

        self.setupUi(self)
        self.setWindowTitle(f"WattWise | {window_title}")
        self.labelSubcategory.setText(window_title)

        self.subcategories_window = subcategories_window

        self.showMaximized()
        self.modifyWindow()

    def modifyWindow(self):
        self.btnBack.clicked.connect(self.back_to_subcategories_window)
        self.btnRandomize.clicked.connect(self.randomize_questions)
        self.add_questions_to_textEdit()

    def add_questions_to_textEdit(self):
        self.txtEditQuestions.setPlainText(" QUESTIONS: \n\n")

        count = 1
        for question, details in self.questions.items():
            prev_content = self.txtEditQuestions.toPlainText()
            self.txtEditQuestions.setPlainText(f"{prev_content} {count}. {question} \n")

            options = details["options"]
            for option, text in options.items():
                prev_content = self.txtEditQuestions.toPlainText()
                self.txtEditQuestions.setPlainText(
                    f"{prev_content} {option}. {text} \n"
                )

            prev_content = self.txtEditQuestions.toPlainText()
            self.txtEditQuestions.setPlainText(f"{prev_content} \n")

            count += 1

    def randomize_questions(self):
        old_questions = self.questions.copy()
        keys = list(old_questions.keys())
        random.shuffle(keys)
        self.questions = {key: old_questions[key] for key in keys}

        # Prompt the user that the randomization is succesful
        msg = QMessageBox()
        msg.setWindowTitle("Success")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Questions are randomized successfully!")
        msg.exec()

        self.add_questions_to_textEdit()

    def back_to_subcategories_window(self):
        if self.subcategories_window:
            self.subcategories_window.show()

        self.hide()
