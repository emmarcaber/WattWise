from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt
from ..uis.ui_eeps_subcategories import Ui_EEPSWindow
from app.views.randomize_view import RandomizeWindow

from app.models.question import Question
from app.models.option import Option

import random


class EEPSWindow(QMainWindow, Ui_EEPSWindow):
    def __init__(self, student_name, student_id, categories_window=None):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("WattWise | EEPS")
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

        self.btnElectricCircuits.clicked.connect(self.generate_electricCircuits)
        self.btnElectronicTheoryCircuits.clicked.connect(
            self.generate_electronicTheoryCircuits
        )
        self.btnEnergyConversion.clicked.connect(self.generate_energyConversion)
        self.btnPowerTransmissionDistribution.clicked.connect(
            self.generate_powerTransmissionDistribution
        )
        self.btnInstrumentationMeasurement.clicked.connect(
            self.generate_instrumentationMeasurement
        )
        self.btnCircuitLineProtection.clicked.connect(
            self.generate_circuitLineProtection
        )
        self.btnControlSystem.clicked.connect(self.generate_controlSystem)
        self.btnPrinciplesCommunication.clicked.connect(
            self.generate_principlesCommunication
        )
        self.btnComponentsDevices.clicked.connect(self.generate_componentsDevices)
        self.btnElectricalMachines.clicked.connect(self.generate_electricalMachines)
        self.btnPowerPlant.clicked.connect(self.generate_powerPlant)
        self.btnIllumination.clicked.connect(self.generate_illumination)
        self.btnBuildingWiring.clicked.connect(self.generate_buildingWiring)
        self.btnElectronicPowerEquipment.clicked.connect(
            self.generate_electronicPowerEquipment
        )
        self.btnElectricSystems.clicked.connect(self.generate_electricSystems)

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

    def generate_electricCircuits(self):
        # Get all the questions from db and format it
        formatted_questions = self.format_questions_and_options("Electric Circuits")

        self.randomize_window = RandomizeWindow(
            "EEPS - Electric Circuits",
            formatted_questions,
            self.student_name,
            self.student_id,
            subcategories_window=self,
        )

        self.randomize_window.show()
        self.hide()

    def generate_electronicTheoryCircuits(self):
        print("Electronic Theory Circuits")

    def generate_energyConversion(self):
        print("Energy Conversion")

    def generate_powerTransmissionDistribution(self):
        print("Power Transmission and Distribution")

    def generate_instrumentationMeasurement(self):
        print("Instrumentation and Measurement ")

    def generate_circuitLineProtection(self):
        print("Circuit Line and Protection")

    def generate_controlSystem(self):
        # Get all the questions from db and format it
        formatted_questions = self.format_questions_and_options("Control System")

        self.randomize_window = RandomizeWindow(
            "EEPS - Control System",
            formatted_questions,
            self.student_name,
            self.student_id,
            subcategories_window=self,
        )

        self.randomize_window.show()
        self.hide()

    def generate_principlesCommunication(self):
        print("Principles of Communication")

    def generate_componentsDevices(self):
        print("Components and Devices")

    def generate_electricalMachines(self):
        print("Electrical Machines")

    def generate_powerPlant(self):
        print("Power Plant")

    def generate_illumination(self):
        print("Illumination")

    def generate_buildingWiring(self):
        print("Building Wiring")

    def generate_electronicPowerEquipment(self):
        print("Electronic Power Equipment")

    def generate_electricSystems(self):
        print("Electric Systems")

    def back_to_categories_window(self):
        if self.back_to_categories_window:
            self.categories_window.show()

        # print("back")
        self.close()
