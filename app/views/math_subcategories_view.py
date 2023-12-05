from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt
from ..uis.ui_math_subcategories import Ui_MathWindow
from app.views.randomize_view import RandomizeWindow

from app.models.question import Question
from app.models.option import Option

import random


class MathWindow(QMainWindow, Ui_MathWindow):
    def __init__(self, student_name, student_id, categories_window=None):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("WattWise | Mathematics")
        self.student_name = student_name
        self.student_id = student_id
        self.categories_window = categories_window

        self.showMaximized()
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, False)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)

        self.modifyWindow()

    def modifyWindow(self):
        self.btnBack.clicked.connect(self.back_to_categories_window)

        self.btnAlgebra.clicked.connect(self.generate_algebra)
        self.btnTrigonometry.clicked.connect(self.generate_trigonometry)
        self.btnAnalyticalGeometry.clicked.connect(self.generate_analyticalGeometry)
        self.btnDifferentialCalculus.clicked.connect(self.generate_differentialCalculus)
        self.btnDifferentialEquations.clicked.connect(
            self.generate_differentialEquations
        )
        self.btnIntegralCalculus.clicked.connect(self.generate_integralCalculus)
        self.btnComplexNumbers.clicked.connect(self.generate_complexNumbers)
        self.btnMatrices.clicked.connect(self.generate_matrices)
        self.btnPowerSeries.clicked.connect(self.generate_powerSeries)
        self.btnFourierAnalysis.clicked.connect(self.generate_fourierAnalysis)
        self.btnLaplaceTransforms.clicked.connect(self.generate_laplaceTransforms)
        self.btnProbabilityStatistics.clicked.connect(
            self.generate_probabilityStatistics
        )

    def format_questions_and_options(self, subcategory_name):
        # Get the questions and options from db
        questions = Question.get_questions_by_subcategories(subcategory_name)
        options = Option.get_options_by_subcategories(subcategory_name)

        # Initialize an empty dict that will hold questions
        formatted_questions = {}

        # Get all the questions first
        for question in questions:
            question_text = question["text"]
            question_id = question["id"]
            correct_option = question["correct_option"]

            question_options = {}

            # Iterate through all the options
            # and if matches the questionId, include it
            for option in options:
                if option["questionId"] == question_id:
                    question_options[option["option"]] = option["text"]

            # Finalize and format the questions
            formatted_questions[question_text] = {
                "options": question_options,
                "correct_option": correct_option,
            }

        # Select random 20 questions from DB without replicates
        selected_questions = random.sample(list(formatted_questions.keys()), 20)

        # Shuffle the formatted questions based on selected random 20 questions
        shuffle_formatted_questions = {
            key: formatted_questions[key] for key in selected_questions
        }

        return shuffle_formatted_questions

    def generate_algebra(self):
        # Get all the questions from db and format it
        formatted_questions = self.format_questions_and_options("Algebra")

        self.randomize_window = RandomizeWindow(
            "Mathematics - Algebra",
            formatted_questions,
            self.student_name,
            self.student_id,
            subcategories_window=self,
        )

        self.randomize_window.show()
        self.hide()

    def generate_trigonometry(self):
        print("Trigonometry")

    def generate_analyticalGeometry(self):
        # Get all the questions from db and format it
        formatted_questions = self.format_questions_and_options("Analytical Geometry")

        self.randomize_window = RandomizeWindow(
            "Mathematics - Analytical Geometry",
            formatted_questions,
            self.student_name,
            self.student_id,
            subcategories_window=self,
        )

        self.randomize_window.show()
        self.hide()

    def generate_differentialCalculus(self):
        # Get all the questions from db and format it
        formatted_questions = self.format_questions_and_options("Differential Calculus")

        self.randomize_window = RandomizeWindow(
            "Mathematics - Differential Calculus",
            formatted_questions,
            self.student_name,
            self.student_id,
            subcategories_window=self,
        )

        self.randomize_window.show()
        self.hide()

    def generate_differentialEquations(self):
        print("Differential Equations")

    def generate_integralCalculus(self):
        print("Integral Calculus")

    def generate_complexNumbers(self):
        print("Complex Numbers")

    def generate_matrices(self):
        print("Matrices")

    def generate_powerSeries(self):
        print("Power Series")

    def generate_fourierAnalysis(self):
        print("Fourier Analysis")

    def generate_laplaceTransforms(self):
        print("Laplace Transforms")

    def generate_probabilityStatistics(self):
        # Get all the questions from db and format it
        formatted_questions = self.format_questions_and_options(
            "Probability and Statistics"
        )

        self.randomize_window = RandomizeWindow(
            "Mathematics - Probability and Statistics",
            formatted_questions,
            self.student_name,
            self.student_id,
            subcategories_window=self,
        )

        self.randomize_window.show()
        self.hide()

    def back_to_categories_window(self):
        if self.back_to_categories_window:
            self.categories_window.show()

        # print("back")
        self.close()
