# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'randomize.ui'
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
    QLabel, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QWidget)
from app.resources import main_menu_rc

class Ui_RandomizeWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1364, 724)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setStyleSheet(u"#header {\n"
"	background-color: #004d99;\n"
"	padding-left: 10px;\n"
"	margin-left: 10px;\n"
"	margin-right: 10px;\n"
"}\n"
"\n"
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
"#mainFrame {\n"
"	padding: 10px 0px;\n"
"	border: 2px solid #0073e6;\n"
"	margin-top: 10px;\n"
"	margin-right: 10px;\n"
"	margin-left: 3px;\n"
"}\n"
"\n"
"#mainFrame QPushButton {\n"
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
"#mainFrame QPushButton:hover {\n"
"	background-color: #0067CC;\n"
"}\n"
"\n"
"#mainFrame #btnPrint {\n"
"	background-color: green;\n"
"}\n"
"\n"
"#menuFrame #btnPrint:hover {\n"
""
                        "	background-color: #398416;\n"
"}\n"
"\n"
"#labelSubcategory {\n"
"	font-size: 28px;\n"
"	font-weight: bold;\n"
"	font-family: Arial;\n"
"	margin-bottom: 10px;\n"
"}\n"
"\n"
"#txtEditQuestions {\n"
"	margin-left: 10px;\n"
"	margin-right: 10px;\n"
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

        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.gridLayout_3 = QGridLayout(self.mainFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.labelSubcategory = QLabel(self.mainFrame)
        self.labelSubcategory.setObjectName(u"labelSubcategory")
        self.labelSubcategory.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.labelSubcategory, 1, 0, 1, 2)

        self.formFrame = QFrame(self.mainFrame)
        self.formFrame.setObjectName(u"formFrame")
        self.gridLayout = QGridLayout(self.formFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnRandomize = QPushButton(self.formFrame)
        self.btnRandomize.setObjectName(u"btnRandomize")
        self.btnRandomize.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/images/assets/refresh-ccw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnRandomize.setIcon(icon1)
        self.btnRandomize.setIconSize(QSize(28, 28))

        self.gridLayout.addWidget(self.btnRandomize, 0, 0, 1, 1)

        self.btnPrint = QPushButton(self.formFrame)
        self.btnPrint.setObjectName(u"btnPrint")
        self.btnPrint.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/images/assets/check-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPrint.setIcon(icon2)
        self.btnPrint.setIconSize(QSize(28, 28))

        self.gridLayout.addWidget(self.btnPrint, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.formFrame, 2, 1, 1, 1)

        self.txtEditQuestions = QPlainTextEdit(self.mainFrame)
        self.txtEditQuestions.setObjectName(u"txtEditQuestions")
        self.txtEditQuestions.setMinimumSize(QSize(0, 450))
        self.txtEditQuestions.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        self.txtEditQuestions.setFont(font)
        self.txtEditQuestions.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))

        self.gridLayout_3.addWidget(self.txtEditQuestions, 2, 0, 1, 1)


        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.mainFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnBack.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.logo.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u"PROJECT: WattWise", None))
        self.labelSubcategory.setText(QCoreApplication.translate("MainWindow", u"Subcategory Name", None))
        self.btnRandomize.setText(QCoreApplication.translate("MainWindow", u"Randomize", None))
        self.btnPrint.setText(QCoreApplication.translate("MainWindow", u"Finalize", None))
    # retranslateUi

