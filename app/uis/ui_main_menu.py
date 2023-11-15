# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_menu.ui'
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
    QHBoxLayout, QLabel, QLayout, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
from app.resources import main_menu_rc

class Ui_MainMenu(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1112, 600)
        MainWindow.setStyleSheet(u"#header {\n"
"	background-color: #004d99;\n"
"	padding-left: 10px;\n"
"	margin-left: 10px;\n"
"	margin-right: 15px;\n"
"}\n"
"\n"
"#title {\n"
"	color: white;\n"
"	font-weight: bold;\n"
"	font-size: 36px;\n"
"}\n"
"\n"
"#profileFrame {\n"
"	padding-left: 10px;\n"
"	background-color: #0073e6;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	height: 160px;\n"
"	font-size: 28px;\n"
"	color: white;\n"
"	margin-bottom: 20px;\n"
"}\n"
"\n"
"#btnGenerate {\n"
"	background-color: #00cc00;\n"
"}\n"
"\n"
"#btnCheck {\n"
"	background-color: #007acc;\n"
"}\n"
"\n"
"#btnAnalysis {\n"
"	background-color: #e6b800;\n"
"}\n"
"\n"
"#btnLogout {\n"
"	background-color: #e62e00;\n"
"}\n"
"\n"
"#menuFrame {\n"
"	padding: 10px 0px;\n"
"}\n"
"\n"
"#labelWelcome {\n"
"	font-size: 36px;\n"
"	color: white;\n"
"}\n"
"\n"
"#labelStudentName {\n"
"	font-size: 48px;\n"
"	color: white;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.formLayout = QFormLayout(self.header)
        self.formLayout.setObjectName(u"formLayout")
        self.logo = QLabel(self.header)
        self.logo.setObjectName(u"logo")
        self.logo.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMaximumSize(QSize(100, 100))
        self.logo.setFrameShadow(QFrame.Sunken)
        self.logo.setPixmap(QPixmap(u":/images/assets/logo-white.png"))
        self.logo.setScaledContents(True)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.logo)

        self.title = QLabel(self.header)
        self.title.setObjectName(u"title")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.title)


        self.gridLayout.addWidget(self.header, 0, 0, 1, 1)

        self.horizontalFrame = QFrame(self.centralwidget)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.profileFrame = QFrame(self.horizontalFrame)
        self.profileFrame.setObjectName(u"profileFrame")
        self.formLayout_3 = QFormLayout(self.profileFrame)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout_3.setFormAlignment(Qt.AlignCenter)
        self.labelWelcome = QLabel(self.profileFrame)
        self.labelWelcome.setObjectName(u"labelWelcome")
        self.labelWelcome.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(0, QFormLayout.SpanningRole, self.labelWelcome)

        self.labelStudentName = QLabel(self.profileFrame)
        self.labelStudentName.setObjectName(u"labelStudentName")
        self.labelStudentName.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(1, QFormLayout.SpanningRole, self.labelStudentName)


        self.horizontalLayout.addWidget(self.profileFrame)

        self.menuFrame = QFrame(self.horizontalFrame)
        self.menuFrame.setObjectName(u"menuFrame")
        self.verticalLayout_2 = QVBoxLayout(self.menuFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btnGenerate = QPushButton(self.menuFrame)
        self.btnGenerate.setObjectName(u"btnGenerate")
        icon = QIcon()
        icon.addFile(u":/images/assets/printer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnGenerate.setIcon(icon)
        self.btnGenerate.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.btnGenerate)

        self.btnCheck = QPushButton(self.menuFrame)
        self.btnCheck.setObjectName(u"btnCheck")
        icon1 = QIcon()
        icon1.addFile(u":/images/assets/archive.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCheck.setIcon(icon1)
        self.btnCheck.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.btnCheck)

        self.btnAnalysis = QPushButton(self.menuFrame)
        self.btnAnalysis.setObjectName(u"btnAnalysis")
        icon2 = QIcon()
        icon2.addFile(u":/images/assets/zoom-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAnalysis.setIcon(icon2)
        self.btnAnalysis.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.btnAnalysis)

        self.btnLogout = QPushButton(self.menuFrame)
        self.btnLogout.setObjectName(u"btnLogout")
        icon3 = QIcon()
        icon3.addFile(u":/images/assets/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnLogout.setIcon(icon3)
        self.btnLogout.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.btnLogout)


        self.horizontalLayout.addWidget(self.menuFrame)


        self.gridLayout.addWidget(self.horizontalFrame, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u"PROJECT: WattWise", None))
        self.labelWelcome.setText(QCoreApplication.translate("MainWindow", u"Welcome,", None))
        self.labelStudentName.setText(QCoreApplication.translate("MainWindow", u"EMMAR CABER", None))
        self.btnGenerate.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.btnCheck.setText(QCoreApplication.translate("MainWindow", u"Check", None))
        self.btnAnalysis.setText(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.btnLogout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
    # retranslateUi

