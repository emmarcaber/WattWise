# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile.ui'
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
    QAbstractItemView,
    QApplication,
    QFormLayout,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)
from app.resources import main_menu_rc


class Ui_ProfileWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1364, 955)
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
            "	background-color:  #004d99;\n"
            ""
            "	font-weight: bold;\n"
            "}\n"
            "\n"
            "#btnCapture:hover {\n"
            "	background-color: #2215FB;\n"
            "}\n"
            "\n"
            "#btnCheck {\n"
            "	color: #ffffff;\n"
            "	background-color: #00cc00;\n"
            "	font-weight: bold;\n"
            "}\n"
            "\n"
            "#btnCheck:hover {\n"
            "	background-color: #00FF00;\n"
            "}\n"
            "\n"
            "#btnProfile {\n"
            "	color: #ffffff;\n"
            "	background-color:  #d2691e;\n"
            "	font-weight: bold;\n"
            "}\n"
            "\n"
            "#btnProfile:hover {\n"
            "	background-color: #E4843F;\n"
            "}\n"
            "\n"
            "#leftFrame {\n"
            "	background-color: #0067cc;\n"
            "}\n"
            "\n"
            "#labelName {\n"
            "	color: #ffffff;\n"
            "}\n"
            "\n"
            "#resultFrame {\n"
            "	background-color: #ffffff;\n"
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
        self.tableFrame = QFrame(self.mainFrame)
        self.tableFrame.setObjectName("tableFrame")
        self.tableFrame.setMinimumSize(QSize(0, 400))
        self.verticalLayout = QVBoxLayout(self.tableFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.testsTable = QTableWidget(self.tableFrame)
        if self.testsTable.columnCount() < 5:
            self.testsTable.setColumnCount(5)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter)
        __qtablewidgetitem.setFont(font)
        self.testsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter)
        __qtablewidgetitem1.setFont(font)
        self.testsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter)
        __qtablewidgetitem2.setFont(font)
        self.testsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter)
        __qtablewidgetitem3.setFont(font)
        self.testsTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter)
        __qtablewidgetitem4.setFont(font)
        self.testsTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.testsTable.setObjectName("testsTable")
        font1 = QFont()
        font1.setPointSize(10)
        self.testsTable.setFont(font1)
        self.testsTable.setAutoFillBackground(False)
        self.testsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.testsTable.setAlternatingRowColors(True)
        self.testsTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.testsTable.setSortingEnabled(True)
        self.testsTable.setColumnCount(5)
        self.testsTable.horizontalHeader().setDefaultSectionSize(230)

        self.verticalLayout.addWidget(self.testsTable)

        self.gridLayout_3.addWidget(self.tableFrame, 0, 1, 1, 2)

        self.leftFrame = QFrame(self.mainFrame)
        self.leftFrame.setObjectName("leftFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftFrame.sizePolicy().hasHeightForWidth())
        self.leftFrame.setSizePolicy(sizePolicy1)
        self.verticalLayout_5 = QVBoxLayout(self.leftFrame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.nameFrame = QFrame(self.leftFrame)
        self.nameFrame.setObjectName("nameFrame")
        self.verticalLayout_6 = QVBoxLayout(self.nameFrame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.labelName = QLabel(self.nameFrame)
        self.labelName.setObjectName("labelName")
        font2 = QFont()
        font2.setPointSize(24)
        font2.setBold(True)
        self.labelName.setFont(font2)
        self.labelName.setLayoutDirection(Qt.LeftToRight)
        self.labelName.setAlignment(Qt.AlignCenter)
        self.labelName.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.labelName)

        self.resultFrame = QFrame(self.nameFrame)
        self.resultFrame.setObjectName("resultFrame")
        self.verticalLayout_7 = QVBoxLayout(self.resultFrame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_1 = QLabel(self.resultFrame)
        self.label_1.setObjectName("label_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy2)
        self.label_1.setMinimumSize(QSize(0, 50))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.label_1.setFont(font3)
        self.label_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelESAS = QLabel(self.resultFrame)
        self.labelESAS.setObjectName("labelESAS")
        self.labelESAS.setFont(font1)
        self.labelESAS.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.labelESAS)

        self.labelESASTaken = QLabel(self.resultFrame)
        self.labelESASTaken.setObjectName("labelESASTaken")
        self.labelESASTaken.setFont(font1)
        self.labelESASTaken.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.labelESASTaken)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelMath = QLabel(self.resultFrame)
        self.labelMath.setObjectName("labelMath")
        self.labelMath.setFont(font1)
        self.labelMath.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.labelMath)

        self.labelMathTaken = QLabel(self.resultFrame)
        self.labelMathTaken.setObjectName("labelMathTaken")
        self.labelMathTaken.setFont(font1)
        self.labelMathTaken.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.labelMathTaken)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelEEPS = QLabel(self.resultFrame)
        self.labelEEPS.setObjectName("labelEEPS")
        self.labelEEPS.setFont(font1)
        self.labelEEPS.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.labelEEPS)

        self.labelEEPSTaken = QLabel(self.resultFrame)
        self.labelEEPSTaken.setObjectName("labelEEPSTaken")
        self.labelEEPSTaken.setFont(font1)
        self.labelEEPSTaken.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.labelEEPSTaken)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.line = QFrame(self.resultFrame)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelTotal = QLabel(self.resultFrame)
        self.labelTotal.setObjectName("labelTotal")
        self.labelTotal.setFont(font)
        self.labelTotal.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.labelTotal)

        self.labelTotalTaken = QLabel(self.resultFrame)
        self.labelTotalTaken.setObjectName("labelTotalTaken")
        self.labelTotalTaken.setFont(font)
        self.labelTotalTaken.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.labelTotalTaken)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout_7.addLayout(self.verticalLayout_2)

        self.verticalLayout_6.addWidget(self.resultFrame)

        self.verticalLayout_5.addWidget(self.nameFrame)

        self.gridLayout_3.addWidget(self.leftFrame, 0, 0, 1, 1)

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
        ___qtablewidgetitem = self.testsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("MainWindow", "Test ID", None)
        )
        ___qtablewidgetitem1 = self.testsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("MainWindow", "Category/Subcategory", None)
        )
        ___qtablewidgetitem2 = self.testsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("MainWindow", "Test Taken", None)
        )
        ___qtablewidgetitem3 = self.testsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("MainWindow", "Score", None)
        )
        ___qtablewidgetitem4 = self.testsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(
            QCoreApplication.translate("MainWindow", "Status", None)
        )
        self.labelName.setText(
            QCoreApplication.translate("MainWindow", "Jobert Lian Na\u00f1oz", None)
        )
        self.label_1.setText(
            QCoreApplication.translate("MainWindow", "Number of Tests Taken", None)
        )
        self.labelESAS.setText(QCoreApplication.translate("MainWindow", "ESAS", None))
        self.labelESASTaken.setText(
            QCoreApplication.translate("MainWindow", "#10", None)
        )
        self.labelMath.setText(
            QCoreApplication.translate("MainWindow", "MATHEMATICS", None)
        )
        self.labelMathTaken.setText(
            QCoreApplication.translate("MainWindow", "#10", None)
        )
        self.labelEEPS.setText(QCoreApplication.translate("MainWindow", "EEPS", None))
        self.labelEEPSTaken.setText(
            QCoreApplication.translate("MainWindow", "#10", None)
        )
        self.labelTotal.setText(
            QCoreApplication.translate("MainWindow", "TOTAL ", None)
        )
        self.labelTotalTaken.setText(
            QCoreApplication.translate("MainWindow", "#10", None)
        )

    # retranslateUi
