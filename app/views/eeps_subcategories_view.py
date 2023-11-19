from PySide6.QtWidgets import QMainWindow
from ..uis.ui_eeps_subcategories import Ui_EEPSWindow

class EEPSWindow(QMainWindow, Ui_EEPSWindow):
    def __init__(self, student_name, generate_window = None):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("WattWise | EEPS")
        self.student_name = student_name
        self.generate_window = generate_window

        self.showMaximized()

        self.modifyWindow()

    def modifyWindow(self):
        self.btnBack.clicked.connect(self.back_to_generate_window)

        self.btnElectricCircuits.clicked.connect(self.generate_electricCircuits)
        self.btnElectronicTheoryCircuits.clicked.connect(self.generate_electronicTheoryCircuits)
        self.btnEnergyConversion.clicked.connect(self.generate_energyConversion)
        self.btnPowerTransmissionDistribution.clicked.connect(self.generate_powerTransmissionDistribution)
        self.btnInstrumentationMeasurement.clicked.connect(self.generate_instrumentationMeasurement)
        self.btnCircuitLineProtection.clicked.connect(self.generate_circuitLineProtection)
        self.btnControlSystem.clicked.connect(self.generate_controlSystem)
        self.btnPrinciplesCommunication.clicked.connect(self.generate_principlesCommunication)
        self.btnComponentsDevices.clicked.connect(self.generate_componentsDevices)
        self.btnElectricalMachines.clicked.connect(self.generate_electricalMachines)
        self.btnPowerPlant.clicked.connect(self.generate_powerPlant)
        self.btnIllumination.clicked.connect(self.generate_illumination)
        self.btnBuildingWiring.clicked.connect(self.generate_buildingWiring)
        self.btnElectronicPowerEquipment.clicked.connect(self.generate_electronicPowerEquipment)
        self.btnElectricSystems.clicked.connect(self.generate_electricSystems)


    def generate_electricCircuits(self):
        print("Electric Circuits")


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
        print("Control System")


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


    def back_to_generate_window(self):
        if self.back_to_generate_window:
            self.generate_window.show()

        # print("back")
        self.close()
