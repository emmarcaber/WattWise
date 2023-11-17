# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'esas_subcategories.ui'
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

class Ui_ESASWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1503, 887)
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
"	margin-top: 10px;\n"
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
"#menuFrame QPushB"
                        "utton:hover {\n"
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
        self.btnGeneralChemistry = QPushButton(self.frame_4)
        self.btnGeneralChemistry.setObjectName(u"btnGeneralChemistry")
        self.btnGeneralChemistry.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btnGeneralChemistry)

        self.btnCollegePhysics = QPushButton(self.frame_4)
        self.btnCollegePhysics.setObjectName(u"btnCollegePhysics")
        self.btnCollegePhysics.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCollegePhysics.setLayoutDirection(Qt.LeftToRight)
        self.btnCollegePhysics.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.btnCollegePhysics)

        self.btnComputerProgramming = QPushButton(self.frame_4)
        self.btnComputerProgramming.setObjectName(u"btnComputerProgramming")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnComputerProgramming.sizePolicy().hasHeightForWidth())
        self.btnComputerProgramming.setSizePolicy(sizePolicy1)
        self.btnComputerProgramming.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnComputerProgramming.setStyleSheet(u"")
        self.btnComputerProgramming.setAutoRepeat(False)

        self.verticalLayout_3.addWidget(self.btnComputerProgramming)

        self.btnEngineeringMaterials = QPushButton(self.frame_4)
        self.btnEngineeringMaterials.setObjectName(u"btnEngineeringMaterials")
        self.btnEngineeringMaterials.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btnEngineeringMaterials)

        self.btnEngineeringMechanics = QPushButton(self.frame_4)
        self.btnEngineeringMechanics.setObjectName(u"btnEngineeringMechanics")
        self.btnEngineeringMechanics.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btnEngineeringMechanics)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.subcategMainFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btnFluidMechanics = QPushButton(self.frame_3)
        self.btnFluidMechanics.setObjectName(u"btnFluidMechanics")
        self.btnFluidMechanics.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.btnFluidMechanics)

        self.btnStrengthMaterials = QPushButton(self.frame_3)
        self.btnStrengthMaterials.setObjectName(u"btnStrengthMaterials")
        self.btnStrengthMaterials.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.btnStrengthMaterials)

        self.btnThermodynamics = QPushButton(self.frame_3)
        self.btnThermodynamics.setObjectName(u"btnThermodynamics")
        self.btnThermodynamics.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.btnThermodynamics)

        self.btnComponentsDevices = QPushButton(self.frame_3)
        self.btnComponentsDevices.setObjectName(u"btnComponentsDevices")
        self.btnComponentsDevices.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.btnComponentsDevices)

        self.btnEngineeringEconomics = QPushButton(self.frame_3)
        self.btnEngineeringEconomics.setObjectName(u"btnEngineeringEconomics")
        self.btnEngineeringEconomics.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.btnEngineeringEconomics)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.subcategMainFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnEngineeringManagement = QPushButton(self.frame_2)
        self.btnEngineeringManagement.setObjectName(u"btnEngineeringManagement")
        self.btnEngineeringManagement.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btnEngineeringManagement)

        self.btnContractsSpecifications = QPushButton(self.frame_2)
        self.btnContractsSpecifications.setObjectName(u"btnContractsSpecifications")
        self.btnContractsSpecifications.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btnContractsSpecifications)

        self.btnCodeProfessionalEthics = QPushButton(self.frame_2)
        self.btnCodeProfessionalEthics.setObjectName(u"btnCodeProfessionalEthics")
        self.btnCodeProfessionalEthics.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btnCodeProfessionalEthics)

        self.btnPEC = QPushButton(self.frame_2)
        self.btnPEC.setObjectName(u"btnPEC")
        sizePolicy1.setHeightForWidth(self.btnPEC.sizePolicy().hasHeightForWidth())
        self.btnPEC.setSizePolicy(sizePolicy1)
        self.btnPEC.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btnPEC)

        self.btnRandom = QPushButton(self.frame_2)
        self.btnRandom.setObjectName(u"btnRandom")
        self.btnRandom.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btnRandom)


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
        self.labelMainMenuTitle.setText(QCoreApplication.translate("MainWindow", u"Engineering Sciences and Allied Subjects (ESAS)", None))
        self.btnGeneralChemistry.setText(QCoreApplication.translate("MainWindow", u"General Chemistry", None))
        self.btnCollegePhysics.setText(QCoreApplication.translate("MainWindow", u"College Physics", None))
        self.btnComputerProgramming.setText(QCoreApplication.translate("MainWindow", u"Computer Programming", None))
        self.btnEngineeringMaterials.setText(QCoreApplication.translate("MainWindow", u"Engineering Materials", None))
        self.btnEngineeringMechanics.setText(QCoreApplication.translate("MainWindow", u"Engineering Mechanics", None))
        self.btnFluidMechanics.setText(QCoreApplication.translate("MainWindow", u"Fluid Mechanics", None))
        self.btnStrengthMaterials.setText(QCoreApplication.translate("MainWindow", u"Strength of Materials", None))
        self.btnThermodynamics.setText(QCoreApplication.translate("MainWindow", u"Thermodynamics", None))
        self.btnComponentsDevices.setText(QCoreApplication.translate("MainWindow", u"Electrical Engineering Law", None))
        self.btnEngineeringEconomics.setText(QCoreApplication.translate("MainWindow", u"Engineering Economics", None))
        self.btnEngineeringManagement.setText(QCoreApplication.translate("MainWindow", u"Engineering Management", None))
        self.btnContractsSpecifications.setText(QCoreApplication.translate("MainWindow", u"Contracts Specifications", None))
        self.btnCodeProfessionalEthics.setText(QCoreApplication.translate("MainWindow", u"Code of Professional Ethics", None))
        self.btnPEC.setText(QCoreApplication.translate("MainWindow", u"Philippine Electrical Code \n"
"Parts 1 && 2", None))
        self.btnRandom.setText(QCoreApplication.translate("MainWindow", u"RANDOM", None))
        self.labelSelection.setText(QCoreApplication.translate("MainWindow", u"Please choose a subcategory", None))
    # retranslateUi

