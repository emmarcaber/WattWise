# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'check.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QFormLayout,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)
from app.resources import main_menu_rc


class Ui_CheckWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1364, 835)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setStyleSheet(
            "#header {\n"
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
            "#btnBackMainMenu {\n"
            "	background-color: #4db8ff;\n"
            "	border-radius: 20px;\n"
            "	color: white;\n"
            "	margin-top: 10px;\n"
            "	font-size: 24px;\n"
            "	height: 50px;\n"
            "}\n"
            "\n"
            "#btnBackMainMenu:hover {\n"
            "	background-color: #1AA4FF;\n"
            "}\n"
            "\n"
            "#mainFrame {\n"
            "	border: 2px solid #0073e6;\n"
            "	margin-left: 3px;\n"
            "	margin-right: 10px;\n"
            "}\n"
            "\n"
            "#mainFrame #btnPrint {\n"
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
            "#mainFrame #btnPrint:hover {\n"
            "	background-color: #0067CC;\n"
            "}\n"
            "\n"
            "#mainFrame QPushButton {\n"
            "	margin-top: 10px;\n"
            "	margin-bottom: 10px;\n"
            "}\n"
            "\n"
            "#btnCapture {\n"
            "	color: #ffffff;\n"
            "	backgr"
            "ound-color:  #004d99;\n"
            "	font-weight: bold;\n"
            "}\n"
            "\n"
            "#btnCapture:hover {\n"
            "	background-color: #2215FB;\n"
            "}\n"
            "\n"
            "#btnCheck {\n"
            "	color: #ffffff;\n"
            "	background-color: #DDDDDD;\n"
            "	font-weight: bold;\n"
            "}\n"
            "\n"
            "#btnCheck:hover {\n"
            "	background-color: #00FF00;\n"
            "}\n"
            "\n"
            "#btnProfile {\n"
            "	color: #ffffff;\n"
            "	background-color:  #DDDDDD;\n"
            "	font-weight: bold;\n"
            "}\n"
            "\n"
            "#btnProfile:hover {\n"
            "	background-color: #E4843F;\n"
            "}\n"
            "\n"
            "#labelItem1, #labelItem2, #labelItem3, #labelItem4, #labelItem5, #labelItem6, #labelItem7, #labelItem8, #labelItem9, #labelItem10,#labelItem11, #labelItem12, #labelItem13, #labelItem14, #labelItem15, #labelItem16, #labelItem17, #labelItem18, #labelItem19, #labelItem20 {\n"
            "	font-size: 18px;\n"
            "}"
        )
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout_2 = QFormLayout(self.centralwidget)
        self.formLayout_2.setObjectName("formLayout_2")
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName("header")
        self.header.setBaseSize(QSize(0, 0))
        self.gridLayout_2 = QGridLayout(self.header)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QFrame(self.header)
        self.frame.setObjectName("frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btnBackMainMenu = QPushButton(self.frame)
        self.btnBackMainMenu.setObjectName("btnBackMainMenu")
        self.btnBackMainMenu.setEnabled(True)
        self.btnBackMainMenu.setGeometry(QRect(330, 10, 261, 61))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnBackMainMenu.sizePolicy().hasHeightForWidth()
        )
        self.btnBackMainMenu.setSizePolicy(sizePolicy)
        self.btnBackMainMenu.setMinimumSize(QSize(0, 0))
        self.btnBackMainMenu.setBaseSize(QSize(100, 100))
        self.btnBackMainMenu.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(":/images/assets/arrow-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnBackMainMenu.setIcon(icon)
        self.btnBackMainMenu.setIconSize(QSize(28, 28))

        self.gridLayout_2.addWidget(self.frame, 0, 2, 1, 1)

        self.logo = QLabel(self.header)
        self.logo.setObjectName("logo")
        self.logo.setEnabled(True)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMaximumSize(QSize(100, 100))
        self.logo.setFrameShadow(QFrame.Sunken)
        self.logo.setPixmap(QPixmap(":/images/assets/logo-white.png"))
        self.logo.setScaledContents(True)

        self.gridLayout_2.addWidget(self.logo, 0, 0, 1, 1)

        self.title = QLabel(self.header)
        self.title.setObjectName("title")

        self.gridLayout_2.addWidget(self.title, 0, 1, 1, 1)

        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.header)

        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName("mainFrame")
        self.gridLayout_3 = QGridLayout(self.mainFrame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cameraFrame = QFrame(self.mainFrame)
        self.cameraFrame.setObjectName("cameraFrame")
        sizePolicy.setHeightForWidth(self.cameraFrame.sizePolicy().hasHeightForWidth())
        self.cameraFrame.setSizePolicy(sizePolicy)
        self.cameraFrame.setMinimumSize(QSize(0, 630))
        self.verticalLayout = QVBoxLayout(self.cameraFrame)
        self.verticalLayout.setObjectName("verticalLayout")

        self.gridLayout_3.addWidget(self.cameraFrame, 0, 1, 1, 2)

        self.answersFrame_2 = QFrame(self.mainFrame)
        self.answersFrame_2.setObjectName("answersFrame_2")
        self.verticalLayout_2 = QVBoxLayout(self.answersFrame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QLabel(self.answersFrame_2)
        self.label.setObjectName("label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.answersFrame = QFrame(self.answersFrame_2)
        self.answersFrame.setObjectName("answersFrame")
        self.horizontalLayout = QHBoxLayout(self.answersFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.firstFrame = QFrame(self.answersFrame)
        self.firstFrame.setObjectName("firstFrame")
        self.verticalLayout_3 = QVBoxLayout(self.firstFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelItem1 = QLabel(self.firstFrame)
        self.labelItem1.setObjectName("labelItem1")

        self.verticalLayout_3.addWidget(self.labelItem1)

        self.labelItem2 = QLabel(self.firstFrame)
        self.labelItem2.setObjectName("labelItem2")

        self.verticalLayout_3.addWidget(self.labelItem2)

        self.labelItem3 = QLabel(self.firstFrame)
        self.labelItem3.setObjectName("labelItem3")

        self.verticalLayout_3.addWidget(self.labelItem3)

        self.labelItem4 = QLabel(self.firstFrame)
        self.labelItem4.setObjectName("labelItem4")

        self.verticalLayout_3.addWidget(self.labelItem4)

        self.labelItem5 = QLabel(self.firstFrame)
        self.labelItem5.setObjectName("labelItem5")

        self.verticalLayout_3.addWidget(self.labelItem5)

        self.labelItem6 = QLabel(self.firstFrame)
        self.labelItem6.setObjectName("labelItem6")

        self.verticalLayout_3.addWidget(self.labelItem6)

        self.labelItem7 = QLabel(self.firstFrame)
        self.labelItem7.setObjectName("labelItem7")

        self.verticalLayout_3.addWidget(self.labelItem7)

        self.labelItem8 = QLabel(self.firstFrame)
        self.labelItem8.setObjectName("labelItem8")

        self.verticalLayout_3.addWidget(self.labelItem8)

        self.labelItem9 = QLabel(self.firstFrame)
        self.labelItem9.setObjectName("labelItem9")

        self.verticalLayout_3.addWidget(self.labelItem9)

        self.labelItem10 = QLabel(self.firstFrame)
        self.labelItem10.setObjectName("labelItem10")

        self.verticalLayout_3.addWidget(self.labelItem10)

        self.horizontalLayout.addWidget(self.firstFrame)

        self.secondFrame = QFrame(self.answersFrame)
        self.secondFrame.setObjectName("secondFrame")
        self.verticalLayout_4 = QVBoxLayout(self.secondFrame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelItem11 = QLabel(self.secondFrame)
        self.labelItem11.setObjectName("labelItem11")

        self.verticalLayout_4.addWidget(self.labelItem11)

        self.labelItem12 = QLabel(self.secondFrame)
        self.labelItem12.setObjectName("labelItem12")

        self.verticalLayout_4.addWidget(self.labelItem12)

        self.labelItem13 = QLabel(self.secondFrame)
        self.labelItem13.setObjectName("labelItem13")

        self.verticalLayout_4.addWidget(self.labelItem13)

        self.labelItem14 = QLabel(self.secondFrame)
        self.labelItem14.setObjectName("labelItem14")

        self.verticalLayout_4.addWidget(self.labelItem14)

        self.labelItem15 = QLabel(self.secondFrame)
        self.labelItem15.setObjectName("labelItem15")

        self.verticalLayout_4.addWidget(self.labelItem15)

        self.labelItem16 = QLabel(self.secondFrame)
        self.labelItem16.setObjectName("labelItem16")

        self.verticalLayout_4.addWidget(self.labelItem16)

        self.labelItem17 = QLabel(self.secondFrame)
        self.labelItem17.setObjectName("labelItem17")

        self.verticalLayout_4.addWidget(self.labelItem17)

        self.labelItem18 = QLabel(self.secondFrame)
        self.labelItem18.setObjectName("labelItem18")

        self.verticalLayout_4.addWidget(self.labelItem18)

        self.labelItem19 = QLabel(self.secondFrame)
        self.labelItem19.setObjectName("labelItem19")

        self.verticalLayout_4.addWidget(self.labelItem19)

        self.labelItem20 = QLabel(self.secondFrame)
        self.labelItem20.setObjectName("labelItem20")

        self.verticalLayout_4.addWidget(self.labelItem20)

        self.horizontalLayout.addWidget(self.secondFrame)

        self.verticalLayout_2.addWidget(self.answersFrame)

        self.gridLayout_3.addWidget(self.answersFrame_2, 0, 3, 1, 1)

        self.rightFrame = QFrame(self.mainFrame)
        self.rightFrame.setObjectName("rightFrame")
        self.verticalLayout_5 = QVBoxLayout(self.rightFrame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.optionFrame = QFrame(self.rightFrame)
        self.optionFrame.setObjectName("optionFrame")
        self.verticalLayout_6 = QVBoxLayout(self.optionFrame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btnCapture = QPushButton(self.optionFrame)
        self.btnCapture.setObjectName("btnCapture")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnCapture.sizePolicy().hasHeightForWidth())
        self.btnCapture.setSizePolicy(sizePolicy2)
        self.btnCapture.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.btnCapture.setFont(font1)
        self.btnCapture.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.btnCapture)

        self.btnCheck = QPushButton(self.optionFrame)
        self.btnCheck.setObjectName("btnCheck")
        self.btnCheck.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.btnCheck.sizePolicy().hasHeightForWidth())
        self.btnCheck.setSizePolicy(sizePolicy2)
        self.btnCheck.setFont(font1)
        self.btnCheck.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.btnCheck)

        self.btnProfile = QPushButton(self.optionFrame)
        self.btnProfile.setObjectName("btnProfile")
        self.btnProfile.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.btnProfile.sizePolicy().hasHeightForWidth())
        self.btnProfile.setSizePolicy(sizePolicy2)
        self.btnProfile.setFont(font1)
        self.btnProfile.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.btnProfile)

        self.verticalLayout_5.addWidget(self.optionFrame)

        self.resultFrame = QFrame(self.rightFrame)
        self.resultFrame.setObjectName("resultFrame")
        self.verticalLayout_7 = QVBoxLayout(self.resultFrame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox = QGroupBox(self.resultFrame)
        self.groupBox.setObjectName("groupBox")
        font2 = QFont()
        font2.setFamilies(["Arial"])
        font2.setPointSize(12)
        self.groupBox.setFont(font2)
        self.verticalLayout_8 = QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.labelResults = QLabel(self.groupBox)
        self.labelResults.setObjectName("labelResults")
        sizePolicy1.setHeightForWidth(
            self.labelResults.sizePolicy().hasHeightForWidth()
        )
        self.labelResults.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(26)
        font3.setBold(True)
        self.labelResults.setFont(font3)
        self.labelResults.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.verticalLayout_8.addWidget(self.labelResults)

        self.verticalLayout_7.addWidget(self.groupBox)

        self.verticalLayout_5.addWidget(self.resultFrame)

        self.gridLayout_3.addWidget(self.rightFrame, 0, 4, 1, 1)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.mainFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.btnBackMainMenu.setText(
            QCoreApplication.translate("MainWindow", "Back to Main Menu", None)
        )
        self.logo.setText("")
        self.title.setText(
            QCoreApplication.translate("MainWindow", "PROJECT: WattWise", None)
        )
        self.label.setText(
            QCoreApplication.translate("MainWindow", "YOUR ANSWERS", None)
        )
        self.labelItem1.setText(QCoreApplication.translate("MainWindow", "1.", None))
        self.labelItem2.setText(QCoreApplication.translate("MainWindow", "2.", None))
        self.labelItem3.setText(QCoreApplication.translate("MainWindow", "3.", None))
        self.labelItem4.setText(QCoreApplication.translate("MainWindow", "4.", None))
        self.labelItem5.setText(QCoreApplication.translate("MainWindow", "5.", None))
        self.labelItem6.setText(QCoreApplication.translate("MainWindow", "6.", None))
        self.labelItem7.setText(QCoreApplication.translate("MainWindow", "7.", None))
        self.labelItem8.setText(QCoreApplication.translate("MainWindow", "8.", None))
        self.labelItem9.setText(QCoreApplication.translate("MainWindow", "9.", None))
        self.labelItem10.setText(QCoreApplication.translate("MainWindow", "10.", None))
        self.labelItem11.setText(QCoreApplication.translate("MainWindow", "11.", None))
        self.labelItem12.setText(QCoreApplication.translate("MainWindow", "12.", None))
        self.labelItem13.setText(QCoreApplication.translate("MainWindow", "13.", None))
        self.labelItem14.setText(QCoreApplication.translate("MainWindow", "14.", None))
        self.labelItem15.setText(QCoreApplication.translate("MainWindow", "15.", None))
        self.labelItem16.setText(QCoreApplication.translate("MainWindow", "16.", None))
        self.labelItem17.setText(QCoreApplication.translate("MainWindow", "17.", None))
        self.labelItem18.setText(QCoreApplication.translate("MainWindow", "18.", None))
        self.labelItem19.setText(QCoreApplication.translate("MainWindow", "19.", None))
        self.labelItem20.setText(QCoreApplication.translate("MainWindow", "20.", None))
        self.btnCapture.setText(
            QCoreApplication.translate("MainWindow", "CAPTURE", None)
        )
        self.btnCheck.setText(QCoreApplication.translate("MainWindow", "CHECK", None))
        self.btnProfile.setText(
            QCoreApplication.translate("MainWindow", "PROFILE", None)
        )
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", "RESULT", None))
        self.labelResults.setText("")

    # retranslateUi
