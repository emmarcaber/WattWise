# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_menu.ui'
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
    QFrame,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QWidget,
)

# import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 607)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet(
            "#titleFrame {\n"
            "	background-color: #004d99;\n"
            "}\n"
            "\n"
            "#title {\n"
            "	color: #ffffff;\n"
            "}\n"
            "\n"
            "#profileWidget {\n"
            "	background-color: #0073e6;\n"
            "	border-radius: 20px;\n"
            "}\n"
            "\n"
            "#optionWidget {\n"
            "	background-color: #ffffff;\n"
            "	border-radius: 20px;\n"
            "	border: 2px solid #0073e6;\n"
            "}\n"
            "\n"
            "#btnGenerate {\n"
            "	color: #ffffff;\n"
            "	background-color: #00cc00;\n"
            "}\n"
            "\n"
            "#btnCheck {\n"
            "	color: #ffffff;\n"
            "	background-color: #007acc;\n"
            "}\n"
            "\n"
            "#btnProfile {\n"
            "	color: #ffffff;\n"
            "	background-color: #e6b800;\n"
            "}\n"
            "\n"
            "#btnLogout {\n"
            "	color: #ffffff;\n"
            "	background-color: #e62e00;\n"
            "}\n"
            "\n"
            "#label_2, #label_3 {\n"
            "	color: #ffffff;\n"
            "}"
        )
        self.titleFrame = QWidget(self.centralwidget)
        self.titleFrame.setObjectName("titleFrame")
        self.titleFrame.setGeometry(QRect(0, 0, 801, 71))
        self.logo = QLabel(self.titleFrame)
        self.logo.setObjectName("logo")
        self.logo.setGeometry(QRect(20, 10, 55, 51))
        self.logo.setPixmap(QPixmap("logo_white1.png"))
        self.logo.setScaledContents(True)
        self.title = QLabel(self.titleFrame)
        self.title.setObjectName("title")
        self.title.setGeometry(QRect(80, 10, 401, 51))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.title.setFont(font)
        self.profileWidget = QWidget(self.centralwidget)
        self.profileWidget.setObjectName("profileWidget")
        self.profileWidget.setGeometry(QRect(20, 90, 341, 501))
        self.label_2 = QLabel(self.profileWidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(60, 110, 231, 51))
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.profileWidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(50, 160, 261, 71))
        font2 = QFont()
        font2.setPointSize(22)
        font2.setBold(True)
        self.label_3.setFont(font2)
        self.optionWidget = QWidget(self.centralwidget)
        self.optionWidget.setObjectName("optionWidget")
        self.optionWidget.setGeometry(QRect(380, 90, 401, 501))
        self.btnGenerate = QPushButton(self.optionWidget)
        self.btnGenerate.setObjectName("btnGenerate")
        self.btnGenerate.setGeometry(QRect(40, 110, 321, 71))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        self.btnGenerate.setFont(font3)
        self.btnGenerate.setLayoutDirection(Qt.LeftToRight)
        self.btnGenerate.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(
            ":/White Icons/white Icon/printer.svg", QSize(), QIcon.Normal, QIcon.Off
        )
        self.btnGenerate.setIcon(icon)
        self.btnGenerate.setCheckable(False)
        self.btnGenerate.setFlat(False)
        self.btnCheck = QPushButton(self.optionWidget)
        self.btnCheck.setObjectName("btnCheck")
        self.btnCheck.setGeometry(QRect(40, 200, 321, 71))
        self.btnCheck.setFont(font3)
        self.btnCheck.setLayoutDirection(Qt.LeftToRight)
        icon1 = QIcon()
        icon1.addFile(
            ":/White Icons/white Icon/archive.svg", QSize(), QIcon.Normal, QIcon.Off
        )
        self.btnCheck.setIcon(icon1)
        self.btnProfile = QPushButton(self.optionWidget)
        self.btnProfile.setObjectName("btnProfile")
        self.btnProfile.setGeometry(QRect(40, 290, 321, 71))
        self.btnProfile.setFont(font3)
        self.btnProfile.setLayoutDirection(Qt.LeftToRight)
        icon2 = QIcon()
        icon2.addFile(
            ":/White Icons/white Icon/smile.svg", QSize(), QIcon.Normal, QIcon.Off
        )
        self.btnProfile.setIcon(icon2)
        self.btnLogout = QPushButton(self.optionWidget)
        self.btnLogout.setObjectName("btnLogout")
        self.btnLogout.setGeometry(QRect(40, 380, 321, 71))
        self.btnLogout.setFont(font3)
        self.btnLogout.setLayoutDirection(Qt.LeftToRight)
        icon3 = QIcon()
        icon3.addFile(
            ":/White Icons/white Icon/log-out.svg", QSize(), QIcon.Normal, QIcon.Off
        )
        self.btnLogout.setIcon(icon3)
        self.label = QLabel(self.optionWidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(120, 30, 171, 41))
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(True)
        self.label.setFont(font4)
        self.line = QFrame(self.optionWidget)
        self.line.setObjectName("line")
        self.line.setGeometry(QRect(20, 80, 361, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.btnGenerate.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.logo.setText("")
        self.title.setText(
            QCoreApplication.translate("MainWindow", "PROJECT: WattWise", None)
        )
        self.label_2.setText(QCoreApplication.translate("MainWindow", "WELCOME!", None))
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", "JOBERT LIAN", None)
        )
        self.btnGenerate.setText(
            QCoreApplication.translate("MainWindow", "GENERATE", None)
        )
        self.btnCheck.setText(QCoreApplication.translate("MainWindow", "CHECK", None))
        self.btnProfile.setText(
            QCoreApplication.translate("MainWindow", "PROFILE", None)
        )
        self.btnLogout.setText(QCoreApplication.translate("MainWindow", "LOGOUT", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "MAIN MENU", None))

    # retranslateUi
