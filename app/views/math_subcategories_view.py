from PySide6.QtWidgets import QMainWindow
from ..uis.ui_math_subcategories import Ui_MathWindow

class MathWindow(QMainWindow, Ui_MathWindow):
    def __init__(self, student_name, generate_window = None):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("WattWise | Mathematics")
        self.student_name = student_name
        self.generate_window = generate_window

        self.showMaximized()

        self.modifyWindow()

    def modifyWindow(self):
        self.btnBack.clicked.connect(self.back_to_generate_window)

        self.btnAlgebra.clicked.connect(self.generate_algebra)
        self.btnTrigonometry.clicked.connect(self.generate_trigonometry)
        self.btnAnalyticalGeometry.clicked.connect(self.generate_analyticalGeometry)
        self.btnDifferentialCalculus.clicked.connect(self.generate_differentialCalculus)
        self.btnDifferentialEquations.clicked.connect(self.generate_differentialEquations)
        self.btnIntegralCalculus.clicked.connect(self.generate_integralCalculus)
        self.btnComplexNumbers.clicked.connect(self.generate_complexNumbers)
        self.btnMatrices.clicked.connect(self.generate_matrices)
        self.btnPowerSeries.clicked.connect(self.generate_powerSeries)
        self.btnFourierAnalysis.clicked.connect(self.generate_fourierAnalysis)
        self.btnLaplaceTransforms.clicked.connect(self.generate_laplaceTransforms)
        self.btnProbabilityStatistics.clicked.connect(self.generate_probabilityStatistics)


    def generate_algebra(self):
        print("Algebra")


    def generate_trigonometry(self):
        print("Trigonometry")


    def generate_analyticalGeometry(self):
        print("Analytical Geometry")


    def generate_differentialCalculus(self):
        print("Differential Calculus")


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
        print("Probability and Statistics")

    def back_to_generate_window(self):
        if self.back_to_generate_window:
            self.generate_window.show()

        # print("back")
        self.close()
