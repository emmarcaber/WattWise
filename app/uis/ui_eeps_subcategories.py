# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'eeps_subcategories.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
from app.resources import main_menu_rc

class Ui_EEPSWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1364, 994)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setStyleSheet(u"#header {\n"
"	background-color: #004d99;\n"
"	padding-left: 10px;\n"
"	margin-left: 10px;\n"
"	margin-right: 10px;\n"
"}\n"
"\n"
"#labelMainMenuTitle {\n"
"	font-size: 32px;\n"
"	font-weight: bold;\n"
"	margin-bottom: 10px;\n"
"}\n"
"\n"
"#labelSelection {\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"#title {\n"
"	color: white;\n"
"	font-weight: bold;\n"
"	font-size: 36px;\n"
"}\n"
"\n"
"#btnBack {\n"
"	background-color: #4db8ff;\n"
"	border-radius: 20px;\n"
"	color: white;\n"
"	margin-top: 10px;\n"
"	font-size: 24px;\n"
"	height: 50px;\n"
"}\n"
"\n"
"#btnBack:hover {\n"
"	background-color: #1AA4FF;\n"
"}\n"
"\n"
"#menuFrame {\n"
"	padding: 10px 0px;\n"
"	border: 2px solid #0073e6;\n"
"	border-radius: 20px;\n"
"	margin-right: 10px;\n"
"	margin-left: 3px;\n"
"}\n"
"\n"
"#menuFrame QPushButton {\n"
"	color: #ffffff;\n"
"	background-color:  #004d99;\n"
"	border-radius: 15px;\n"
"	font-weight: bold;\n"
"	font-size: 24px;\n"
"	height: 80px;\n"
"	padding: 10px 16px;\n"
"	margin-bottom: 10px;\n"
"}\n"
"\n"
"#menuFrame QPush"
                        "Button:hover {\n"
"	background-color: #0067CC;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout_2 = QFormLayout(self.centralwidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setBaseSize(QSize(0, 0))
        self.gridLayout_2 = QGridLayout(self.header)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btnBack = QPushButton(self.frame)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setGeometry(QRect(440, 10, 131, 61))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBack.sizePolicy().hasHeightForWidth())
        self.btnBack.setSizePolicy(sizePolicy)
        self.btnBack.setMinimumSize(QSize(0, 0))
        self.btnBack.setBaseSize(QSize(100, 100))
        self.btnBack.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/images/assets/arrow-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnBack.setIcon(icon)
        self.btnBack.setIconSize(QSize(28, 28))

        self.gridLayout_2.addWidget(self.frame, 0, 2, 1, 1)

        self.logo = QLabel(self.header)
        self.logo.setObjectName(u"logo")
        self.logo.setEnabled(True)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMaximumSize(QSize(100, 100))
        self.logo.setFrameShadow(QFrame.Sunken)
        self.logo.setPixmap(QPixmap(u":/images/assets/logo-white.png"))
        self.logo.setScaledContents(True)

        self.gridLayout_2.addWidget(self.logo, 0, 0, 1, 1)

        self.title = QLabel(self.header)
        self.title.setObjectName(u"title")

        self.gridLayout_2.addWidget(self.title, 0, 1, 1, 1)


        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.header)

        self.menuFrame = QFrame(self.centralwidget)
        self.menuFrame.setObjectName(u"menuFrame")
        self.formLayout = QFormLayout(self.menuFrame)
        self.formLayout.setObjectName(u"formLayout")
        self.labelMainMenuTitle = QLabel(self.menuFrame)
        self.labelMainMenuTitle.setObjectName(u"labelMainMenuTitle")
        self.labelMainMenuTitle.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.labelMainMenuTitle)

        self.subcategMainFrame = QFrame(self.menuFrame)
        self.subcategMainFrame.setObjectName(u"subcategMainFrame")
        self.horizontalLayout_2 = QHBoxLayout(self.subcategMainFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_4 = QFrame(self.subcategMainFrame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btnElectricCircuits = QPushButton(self.frame_4)
        self.btnElectricCircuits.setObjectName(u"btnElectricCircuits")
        self.btnElectricCircuits.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btnElectricCircuits)

        self.btnElectronicTheoryCircuits = QPushButton(self.frame_4)
        self.btnElectronicTheoryCircuits.setObjectName(u"btnElectronicTheoryCircuits")
        self.btnElectronicTheoryCircuits.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnElectronicTheoryCircuits.setLayoutDirection(Qt.LeftToRight)
        self.btnElectronicTheoryCircuits.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.btnElectronicTheoryCircuits)

        self.btnEnergyConversion = QPushButton(self.frame_4)
        self.btnEnergyConversion.setObjectName(u"btnEnergyConversion")
        self.btnEnergyConversion.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btnEnergyConversion)

        self.btnPowerTransmissionDistribution = QPushButton(self.frame_4)
        self.btnPowerTransmissionDistribution.setObjectName(u"btnPowerTransmissionDistribution")
        self.btnPowerTransmissionDistribution.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btnPowerTransmissionDistribution)

        self.btnInstrumentationMeasurement = QPushButton(self.frame_4)
        self.btnInstrumentationMeasurement.setObjectName(u"btnInstrumentationMeasurement")
        self.btnInstrumentationMeasurement.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btnInstrumentationMeasurement)

        self.btnCircuitLineProtection = QPushButton(self.frame_4)
        self.btnCircuitLineProtection.setObjectName(u"btnCircuitLineProtection")
        self.btnCircuitLineProtection.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btnCircuitLineProtection)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.subcategMainFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btnControlSystem = QPushButton(self.frame_3)
        self.btnControlSystem.setObjectName(u"btnControlSystem")
        self.btnControlSystem.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.btnControlSystem)

        self.btnPrinciplesCommunication = QPushButton(self.frame_3)
        self.btnPrinciplesCommunication.setObjectName(u"btnPrinciplesCommunication")
        self.btnPrinciplesCommunication.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.btnPrinciplesCommunication)

        self.btnElectricalEquipment = QPushButton(self.frame_3)
        self.btnElectricalEquipment.setObjectName(u"btnElectricalEquipment")
        self.btnElectricalEquipment.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.btnElectricalEquipment)

        self.btnComponentsDevices = QPushButton(self.frame_3)
        self.btnComponentsDevices.setObjectName(u"btnComponentsDevices")
        self.btnComponentsDevices.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.btnComponentsDevices)

        self.btnElectricalMachines = QPushButton(self.frame_3)
        self.btnElectricalMachines.setObjectName(u"btnElectricalMachines")
        self.btnElectricalMachines.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.btnElectricalMachines)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.subcategMainFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnPowerPlant = QPushButton(self.frame_2)
        self.btnPowerPlant.setObjectName(u"btnPowerPlant")
        self.btnPowerPlant.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btnPowerPlant)

        self.btnIllumination = QPushButton(self.frame_2)
        self.btnIllumination.setObjectName(u"btnIllumination")
        self.btnIllumination.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btnIllumination)

        self.btnBuildingWiring = QPushButton(self.frame_2)
        self.btnBuildingWiring.setObjectName(u"btnBuildingWiring")
        self.btnBuildingWiring.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btnBuildingWiring)

        self.btnElectronicPowerEquipment = QPushButton(self.frame_2)
        self.btnElectronicPowerEquipment.setObjectName(u"btnElectronicPowerEquipment")
        self.btnElectronicPowerEquipment.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btnElectronicPowerEquipment)

        self.btnElectricSystems = QPushButton(self.frame_2)
        self.btnElectricSystems.setObjectName(u"btnElectricSystems")
        self.btnElectricSystems.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btnElectricSystems)


        self.horizontalLayout_2.addWidget(self.frame_2)


        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.subcategMainFrame)

        self.labelSelection = QLabel(self.menuFrame)
        self.labelSelection.setObjectName(u"labelSelection")
        self.labelSelection.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.labelSelection)


        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.menuFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnBack.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.logo.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u"PROJECT: WattWise", None))
        self.labelMainMenuTitle.setText(QCoreApplication.translate("MainWindow", u"Electrical Engineering and Professional Subject (EEPS)", None))
        self.btnElectricCircuits.setText(QCoreApplication.translate("MainWindow", u"Electric Circuits", None))
        self.btnElectronicTheoryCircuits.setText(QCoreApplication.translate("MainWindow", u"Electronic Theory && Circuits", None))
        self.btnEnergyConversion.setText(QCoreApplication.translate("MainWindow", u"Energy Conversion", None))
        self.btnPowerTransmissionDistribution.setText(QCoreApplication.translate("MainWindow", u"Power Transmission && Distribution", None))
        self.btnInstrumentationMeasurement.setText(QCoreApplication.translate("MainWindow", u"Instrumentation && Measurement", None))
        self.btnCircuitLineProtection.setText(QCoreApplication.translate("MainWindow", u"Circuit && Line Protection", None))
        self.btnControlSystem.setText(QCoreApplication.translate("MainWindow", u"Control System", None))
        self.btnPrinciplesCommunication.setText(QCoreApplication.translate("MainWindow", u"Principles of Communication", None))
        self.btnElectricalEquipment.setText(QCoreApplication.translate("MainWindow", u"Electrical Equipment", None))
        self.btnComponentsDevices.setText(QCoreApplication.translate("MainWindow", u"Components Devices", None))
        self.btnElectricalMachines.setText(QCoreApplication.translate("MainWindow", u"Electrical Machines", None))
        self.btnPowerPlant.setText(QCoreApplication.translate("MainWindow", u"Power Plant", None))
        self.btnIllumination.setText(QCoreApplication.translate("MainWindow", u"Illumination", None))
        self.btnBuildingWiring.setText(QCoreApplication.translate("MainWindow", u"Building Wiring", None))
        self.btnElectronicPowerEquipment.setText(QCoreApplication.translate("MainWindow", u"Electronic Power Equipment", None))
        self.btnElectricSystems.setText(QCoreApplication.translate("MainWindow", u"Electric Systems", None))
        self.labelSelection.setText(QCoreApplication.translate("MainWindow", u"Please choose a subcategory", None))
    # retranslateUi

