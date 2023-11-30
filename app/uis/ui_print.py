# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'print.ui'
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
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)
from app.resources import main_menu_rc


class Ui_PrintWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1364, 950)
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
            "	background-color: #DDDDDD;\n"
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
        self.btnBackMainMenu.setEnabled(False)
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
        self.printFrame = QFrame(self.mainFrame)
        self.printFrame.setObjectName("printFrame")
        self.printFrame.setMinimumSize(QSize(0, 750))
        self.verticalLayout = QVBoxLayout(self.printFrame)
        self.verticalLayout.setObjectName("verticalLayout")

        self.gridLayout_3.addWidget(self.printFrame, 0, 1, 1, 2)

        self.btnPrint = QPushButton(self.mainFrame)
        self.btnPrint.setObjectName("btnPrint")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnPrint.sizePolicy().hasHeightForWidth())
        self.btnPrint.setSizePolicy(sizePolicy1)
        self.btnPrint.setMinimumSize(QSize(0, 0))
        self.btnPrint.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(":/images/assets/printer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPrint.setIcon(icon1)
        self.btnPrint.setIconSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.btnPrint, 0, 3, 1, 1)

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
        self.btnPrint.setText(QCoreApplication.translate("MainWindow", "Print", None))

    # retranslateUi
