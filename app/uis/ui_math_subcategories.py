# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'math_subcategories.ui'
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

class Ui_MathWindow(object):
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
        self.btnAlgebra = QPushButton(self.frame_4)
        self.btnAlgebra.setObjectName(u"btnAlgebra")
        self.btnAlgebra.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btnAlgebra)

        self.btnTrigonometry = QPushButton(self.frame_4)
        self.btnTrigonometry.setObjectName(u"btnTrigonometry")
        self.btnTrigonometry.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnTrigonometry.setLayoutDirection(Qt.LeftToRight)
        self.btnTrigonometry.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.btnTrigonometry)

        self.btnAnalyticalGeometry = QPushButton(self.frame_4)
        self.btnAnalyticalGeometry.setObjectName(u"btnAnalyticalGeometry")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnAnalyticalGeometry.sizePolicy().hasHeightForWidth())
        self.btnAnalyticalGeometry.setSizePolicy(sizePolicy1)
        self.btnAnalyticalGeometry.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAnalyticalGeometry.setStyleSheet(u"")
        self.btnAnalyticalGeometry.setAutoRepeat(False)

        self.verticalLayout_3.addWidget(self.btnAnalyticalGeometry)

        self.btnDifferentialCalculus = QPushButton(self.frame_4)
        self.btnDifferentialCalculus.setObjectName(u"btnDifferentialCalculus")
        self.btnDifferentialCalculus.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btnDifferentialCalculus)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.subcategMainFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btnDifferentialEquations = QPushButton(self.frame_3)
        self.btnDifferentialEquations.setObjectName(u"btnDifferentialEquations")
        self.btnDifferentialEquations.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.btnDifferentialEquations)

        self.btnIntegralCalculus = QPushButton(self.frame_3)
        self.btnIntegralCalculus.setObjectName(u"btnIntegralCalculus")
        self.btnIntegralCalculus.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.btnIntegralCalculus)

        self.btnComplexNumbers = QPushButton(self.frame_3)
        self.btnComplexNumbers.setObjectName(u"btnComplexNumbers")
        self.btnComplexNumbers.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.btnComplexNumbers)

        self.btnProbabilityStatistics = QPushButton(self.frame_3)
        self.btnProbabilityStatistics.setObjectName(u"btnProbabilityStatistics")
        self.btnProbabilityStatistics.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.btnProbabilityStatistics)

        self.btnMatrices = QPushButton(self.frame_3)
        self.btnMatrices.setObjectName(u"btnMatrices")

        self.verticalLayout_2.addWidget(self.btnMatrices)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.subcategMainFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnPowerSeries = QPushButton(self.frame_2)
        self.btnPowerSeries.setObjectName(u"btnPowerSeries")
        self.btnPowerSeries.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btnPowerSeries)

        self.btnFourierAnalysis = QPushButton(self.frame_2)
        self.btnFourierAnalysis.setObjectName(u"btnFourierAnalysis")
        self.btnFourierAnalysis.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btnFourierAnalysis)

        self.btnLaplaceTransforms = QPushButton(self.frame_2)
        self.btnLaplaceTransforms.setObjectName(u"btnLaplaceTransforms")
        sizePolicy1.setHeightForWidth(self.btnLaplaceTransforms.sizePolicy().hasHeightForWidth())
        self.btnLaplaceTransforms.setSizePolicy(sizePolicy1)
        self.btnLaplaceTransforms.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btnLaplaceTransforms)

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
        self.labelMainMenuTitle.setText(QCoreApplication.translate("MainWindow", u"Mathematics", None))
        self.btnAlgebra.setText(QCoreApplication.translate("MainWindow", u"Algebra", None))
        self.btnTrigonometry.setText(QCoreApplication.translate("MainWindow", u"Trigonometry", None))
        self.btnAnalyticalGeometry.setText(QCoreApplication.translate("MainWindow", u"Analytical Geometry", None))
        self.btnDifferentialCalculus.setText(QCoreApplication.translate("MainWindow", u"Differential Calculus", None))
        self.btnDifferentialEquations.setText(QCoreApplication.translate("MainWindow", u"Differential Equations", None))
        self.btnIntegralCalculus.setText(QCoreApplication.translate("MainWindow", u"Integral Calculus", None))
        self.btnComplexNumbers.setText(QCoreApplication.translate("MainWindow", u"Complex Numbers", None))
        self.btnProbabilityStatistics.setText(QCoreApplication.translate("MainWindow", u"Probability && Statistics", None))
        self.btnMatrices.setText(QCoreApplication.translate("MainWindow", u"Matrices", None))
        self.btnPowerSeries.setText(QCoreApplication.translate("MainWindow", u"Power Series", None))
        self.btnFourierAnalysis.setText(QCoreApplication.translate("MainWindow", u"Fourier Analysis", None))
        self.btnLaplaceTransforms.setText(QCoreApplication.translate("MainWindow", u"Laplace Transforms", None))
        self.btnRandom.setText(QCoreApplication.translate("MainWindow", u"RANDOM", None))
        self.labelSelection.setText(QCoreApplication.translate("MainWindow", u"Please choose a subcategory", None))
    # retranslateUi

