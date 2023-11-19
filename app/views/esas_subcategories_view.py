from PySide6.QtWidgets import QMainWindow
from ..uis.ui_esas_subcategories import Ui_ESASWindow

class ESASWindow(QMainWindow, Ui_ESASWindow):
    def __init__(self, student_name, generate_window = None):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("WattWise | ESAS")
        self.student_name = student_name
        self.generate_window = generate_window

        self.showMaximized()

        self.modifyWindow()

    def modifyWindow(self):
        self.btnBack.clicked.connect(self.back_to_generate_window)

        self.btnGeneralChemistry.clicked.connect(self.generate_generalChemistry)
        self.btnCollegePhysics.clicked.connect(self.generate_collegePhysics)
        self.btnPEC.clicked.connect(self.generate_PEC)
        self.btnComputerProgramming.clicked.connect(self.generate_computerProgramming)
        self.btnFluidMechanics.clicked.connect(self.generate_fluidMechanics)
        self.btnStrengthMaterials.clicked.connect(self.generate_strengthMaterials)
        self.btnThermodynamics.clicked.connect(self.generate_thermodynamics)
        self.btnElectricalEngineeringLaw.clicked.connect(self.generate_electricalEngineeringLaw)
        self.btnEngineeringEconomics.clicked.connect(self.generate_engineeringEconomics)
        self.btnEngineeringManagement.clicked.connect(self.generate_engineeringManagement)
        self.btnContractsSpecifications.clicked.connect(self.generate_contractsSpecifications)
        self.btnCodeProfessionalEthics.clicked.connect(self.generate_codeProfessionalEthics)
        self.btnEngineeringMaterials.clicked.connect(self.generate_engineeringMaterials)
        self.btnEngineeringMechanics.clicked.connect(self.generate_engineeringMechanics)

    
    def generate_generalChemistry(self):
        print("General Chemistry")

    
    def generate_collegePhysics(self):
        print("College Physics")

    
    def generate_PEC(self):
        print("Philippine Electrical Code Parts 1 and 2")

    
    def generate_computerProgramming(self):
        print("Computer Fundamentals and Programming")

    
    def generate_fluidMechanics(self):
        print("Fluid Mechanics")

    
    def generate_strengthMaterials(self):
        print("Strength of Materials")

    
    def generate_thermodynamics(self):
        print("Thermodynamics")

    
    def generate_electricalEngineeringLaw(self):
        print("Electrical Engineering Law")

    
    def generate_engineeringEconomics(self):
        print("Engineering Economics")

    
    def generate_engineeringManagement(self):
        print("Engineering Management")

    
    def generate_contractsSpecifications(self):
        print("Contracts Specifications")

    
    def generate_codeProfessionalEthics(self):
        print("Code of Professional Ethics")

    
    def generate_engineeringMaterials(self):
        print("Engineering Materials")

    
    def generate_engineeringMechanics(self):
        print("Engineering Mechanics")


    def back_to_generate_window(self):
        if self.back_to_generate_window:
            self.generate_window.show()

        # print("back")
        self.close()
