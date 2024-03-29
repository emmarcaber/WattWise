from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt
from ..uis.ui_esas_subcategories import Ui_ESASWindow
from app.views.randomize_view import RandomizeWindow

from app.models.question import Question
from app.models.option import Option

import random


class ESASWindow(QMainWindow, Ui_ESASWindow):
    def __init__(self, student_name, student_id, categories_window=None):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("WattWise | ESAS")
        self.student_name = student_name
        self.student_id = student_id
        self.categories_window = categories_window

        self.question = Question()
        self.option = Option()

        self.showMaximized()
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, False)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)

        self.modifyWindow()

    def modifyWindow(self):
        self.btnBack.clicked.connect(self.back_to_categories_window)

        self.btnGeneralChemistry.clicked.connect(self.generate_generalChemistry)
        self.btnCollegePhysics.clicked.connect(self.generate_collegePhysics)
        self.btnPEC.clicked.connect(self.generate_PEC)
        self.btnComputerProgramming.clicked.connect(self.generate_computerProgramming)
        self.btnFluidMechanics.clicked.connect(self.generate_fluidMechanics)
        self.btnStrengthMaterials.clicked.connect(self.generate_strengthMaterials)
        self.btnThermodynamics.clicked.connect(self.generate_thermodynamics)
        self.btnElectricalEngineeringLaw.clicked.connect(
            self.generate_electricalEngineeringLaw
        )
        self.btnEngineeringEconomics.clicked.connect(self.generate_engineeringEconomics)
        self.btnEngineeringManagement.clicked.connect(
            self.generate_engineeringManagement
        )
        self.btnContractsSpecifications.clicked.connect(
            self.generate_contractsSpecifications
        )
        self.btnCodeProfessionalEthics.clicked.connect(
            self.generate_codeProfessionalEthics
        )
        self.btnEngineeringMaterials.clicked.connect(self.generate_engineeringMaterials)
        self.btnEngineeringMechanics.clicked.connect(self.generate_engineeringMechanics)

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

    def generate_generalChemistry(self):
        # Get all the questions from db and format it
        formatted_questions = self.format_questions_and_options("General Chemistry")

        self.randomize_window = RandomizeWindow(
            "ESAS - General Chemistry",
            formatted_questions,
            self.student_name,
            self.student_id,
            subcategories_window=self,
        )

        self.randomize_window.show()
        self.hide()

    def generate_collegePhysics(self):
        # Get all the questions from db and format it
        formatted_questions = self.format_questions_and_options("College Physics")

        self.randomize_window = RandomizeWindow(
            "ESAS - College Physics",
            formatted_questions,
            self.student_name,
            self.student_id,
            subcategories_window=self,
        )

        self.randomize_window.show()
        self.hide()

    def generate_PEC(self):
        # Get all the questions from db and format it
        formatted_questions = self.format_questions_and_options(
            "Philippine Electrical Code Parts 1 and 2"
        )

        self.randomize_window = RandomizeWindow(
            "ESAS - Philippine Electrical Code Parts 1 and 2",
            formatted_questions,
            self.student_name,
            self.student_id,
            subcategories_window=self,
        )

        self.randomize_window.show()
        self.hide()

    def generate_computerProgramming(self):
        #print("Computer Fundamentals and Programming")
        formatted_questions = self.format_questions_and_options("Computer Fundamentals and Programming")

        self.randomize_window = RandomizeWindow(
            "ESAS - Computer Fundamentals and Programming",
            formatted_questions,
            self.student_name,
            self.student_id,
            subcategories_window=self,
        )

        self.randomize_window.show()
        self.hide()

    def generate_fluidMechanics(self):
        #print("Fluid Mechanics")
        formatted_questions = self.format_questions_and_options("Fluid Mechanics")

        self.randomize_window = RandomizeWindow(
            "ESAS - Fluid Mechanics",
            formatted_questions,
            self.student_name,
            self.student_id,
            subcategories_window=self,
        )

        self.randomize_window.show()
        self.hide()

    def generate_strengthMaterials(self):
        #print("Strength of Materials")
        formatted_questions = self.format_questions_and_options("Strength of Materials")

        self.randomize_window = RandomizeWindow(
            "ESAS - Strength of Materials",
            formatted_questions,
            self.student_name,
            self.student_id,
            subcategories_window=self,
        )

        self.randomize_window.show()
        self.hide()

    def generate_thermodynamics(self):
        # Get all the questions from db and format it
        formatted_questions = self.format_questions_and_options("Thermodynamics")

        self.randomize_window = RandomizeWindow(
            "ESAS - Thermodynamics",
            formatted_questions,
            self.student_name,
            self.student_id,
            subcategories_window=self,
        )

        self.randomize_window.show()
        self.hide()

    def generate_electricalEngineeringLaw(self):
        # Get all the questions from db and format it
        formatted_questions = self.format_questions_and_options(
            "Electrical Engineering Law"
        )

        self.randomize_window = RandomizeWindow(
            "ESAS - Electrical Engineering Law",
            formatted_questions,
            self.student_name,
            self.student_id,
            subcategories_window=self,
        )

        self.randomize_window.show()
        self.hide()

    def generate_engineeringEconomics(self):
        # Get all the questions from db and format it
        formatted_questions = self.format_questions_and_options("Engineering Economics")

        self.randomize_window = RandomizeWindow(
            "ESAS - Engineering Economics",
            formatted_questions,
            self.student_name,
            self.student_id,
            subcategories_window=self,
        )

        self.randomize_window.show()
        self.hide()

    def generate_engineeringManagement(self):
        #print("Engineering Management")
        formatted_questions = self.format_questions_and_options("Engineering Management")

        self.randomize_window = RandomizeWindow(
            "ESAS - Engineering Management",
            formatted_questions,
            self.student_name,
            self.student_id,
            subcategories_window=self,
        )

        self.randomize_window.show()
        self.hide()

    def generate_contractsSpecifications(self):
        #print("Contracts Specifications")
        formatted_questions = self.format_questions_and_options("Contracts Specifications")

        self.randomize_window = RandomizeWindow(
            "ESAS - Contracts Specifications",
            formatted_questions,
            self.student_name,
            self.student_id,
            subcategories_window=self,
        )

        self.randomize_window.show()
        self.hide()

    def generate_codeProfessionalEthics(self):
        #print("Code of Professional Ethics")
        formatted_questions = self.format_questions_and_options("Code of Professional Ethics")

        self.randomize_window = RandomizeWindow(
            "ESAS - Code of Professional Ethics",
            formatted_questions,
            self.student_name,
            self.student_id,
            subcategories_window=self,
        )

        self.randomize_window.show()
        self.hide()

    def generate_engineeringMaterials(self):
        #print("Engineering Materials")
        formatted_questions = self.format_questions_and_options("Engineering Materials")

        self.randomize_window = RandomizeWindow(
            "ESAS - Engineering Materials",
            formatted_questions,
            self.student_name,
            self.student_id,
            subcategories_window=self,
        )

        self.randomize_window.show()
        self.hide()

    def generate_engineeringMechanics(self):
        #print("Engineering Mechanics")
        formatted_questions = self.format_questions_and_options("Engineering Mechanics")

        self.randomize_window = RandomizeWindow(
            "ESAS - Engineering Mechanics",
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
