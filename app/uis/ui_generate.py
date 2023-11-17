# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generate.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
from app.resources import main_menu_rc

class Ui_GenerateWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1112, 1012)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setStyleSheet(u"#header {\n"
"	background-color: #004d99;\n"
"	padding-left: 10px;\n"
"	margin-left: 10px;\n"
"	margin-right: 15px;\n"
"}\n"
"\n"
"#labelMainMenuTitle {\n"
"	font-size:36px;\n"
"	font-weight: bold;\n"
"	margin-bottom: 10px;\n"
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
"#profileFrame {\n"
"	padding-left: 10px;\n"
"	background-color: #0073e6;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	height: 160px;\n"
"	font-size: 32px;\n"
"	color: white;\n"
"	margin-bottom: 20px;\n"
"	width: 500px;\n"
"}\n"
"\n"
"#btnESAS {\n"
"	background-color: #00cc00;\n"
"}\n"
"\n"
"#btnESAS:hover {\n"
"	background-color: #00FF00;\n"
"}\n"
"\n"
"#btnMathematics {\n"
"	background-color: #007acc;\n"
"}\n"
"\n"
"#btnMathematics:hover {\n"
"	b"
                        "ackground-color: #0099FF;\n"
"}\n"
"\n"
"#btnEEPS {\n"
"	background-color: #e6b800;\n"
"}\n"
"\n"
"#btnEEPS:hover {\n"
"	background-color: #FFD11A;\n"
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
        self.horizontalFrame = QFrame(self.centralwidget)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.menuFrame = QFrame(self.horizontalFrame)
        self.menuFrame.setObjectName(u"menuFrame")
        self.verticalLayout_2 = QVBoxLayout(self.menuFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelMainMenuTitle = QLabel(self.menuFrame)
        self.labelMainMenuTitle.setObjectName(u"labelMainMenuTitle")
        self.labelMainMenuTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelMainMenuTitle)

        self.line = QFrame(self.menuFrame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.btnESAS = QPushButton(self.menuFrame)
        self.btnESAS.setObjectName(u"btnESAS")
        self.btnESAS.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnESAS.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.btnESAS)

        self.btnMathematics = QPushButton(self.menuFrame)
        self.btnMathematics.setObjectName(u"btnMathematics")
        self.btnMathematics.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnMathematics.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.btnMathematics)

        self.btnEEPS = QPushButton(self.menuFrame)
        self.btnEEPS.setObjectName(u"btnEEPS")
        self.btnEEPS.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnEEPS.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.btnEEPS)


        self.horizontalLayout.addWidget(self.menuFrame)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout.addWidget(self.horizontalFrame, 1, 0, 1, 1)

        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.gridLayout_2 = QGridLayout(self.header)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btnBack = QPushButton(self.frame)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setGeometry(QRect(430, 10, 131, 81))
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


        self.gridLayout.addWidget(self.header, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelMainMenuTitle.setText(QCoreApplication.translate("MainWindow", u"CHOOSE A CATEGORY", None))
        self.btnESAS.setText(QCoreApplication.translate("MainWindow", u"ESAS", None))
        self.btnMathematics.setText(QCoreApplication.translate("MainWindow", u"Mathematics", None))
        self.btnEEPS.setText(QCoreApplication.translate("MainWindow", u"EEPS", None))
        self.btnBack.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.logo.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u"PROJECT: WattWise", None))
    # retranslateUi

