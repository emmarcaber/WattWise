# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
from app.resources import main_menu_rc

class Ui_LoginWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"#formFrame {\n"
"	background-color: white;\n"
"}\n"
"\n"
"#logoFrame {\n"
"	background-color: #0067FF;\n"
"}\n"
"\n"
"#separator {\n"
"	background-color: #0067FF;\n"
"}\n"
"\n"
"#labelWelcome {\n"
"	font-size: 40px;\n"
"	margin-top: 80px;\n"
"	margin-bottom: 30px;\n"
"	font-family: Arial;\n"
"}\n"
"\n"
"#labelIDNumber, #labelPassword {\n"
"	font-size: 24px;\n"
"	font-family: Arial;\n"
"}\n"
"\n"
"#lineIDNumber, #linePassword {\n"
"	font-size: 25px;\n"
"	margin-bottom: 20px;\n"
"	font-family: Century Gothic;\n"
"	padding: 10px 12px;\n"
"	border: 2px solid #0067FF;\n"
"	background-color: #0067FF; \n"
"	border-radius: 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"#btnLogin {\n"
"	font-size: 24px;\n"
"	padding: 10px 12px;\n"
"	margin-top: 30px;\n"
"	background-color: #0067FF;\n"
"	color: white;\n"
"	height: 40px;\n"
"}\n"
"\n"
"#btnLogin:hover {\n"
"	border: 2px solid #0067FF;\n"
"	background-color: #eee;\n"
"	color: black;\n"
"}\n"
"\n"
"#btnSignUp {\n"
"	font-size: 16px;\n"
"	color: #0067FF;\n"
"	background-color: whi"
                        "te;\n"
"	border: 0;\n"
"}\n"
"\n"
"#btnSignUp:hover{\n"
"	color: #3385FF;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logoFrame = QFrame(self.centralwidget)
        self.logoFrame.setObjectName(u"logoFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logoFrame.sizePolicy().hasHeightForWidth())
        self.logoFrame.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.logoFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.logoFrame)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(300, 300))
        self.label.setMaximumSize(QSize(300, 300))
        self.label.setBaseSize(QSize(300, 300))
        self.label.setPixmap(QPixmap(u":/images/assets/logo-white.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.logoFrame)

        self.separator = QFrame(self.centralwidget)
        self.separator.setObjectName(u"separator")
        self.separator.setFrameShape(QFrame.VLine)
        self.separator.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.separator)

        self.formFrame = QFrame(self.centralwidget)
        self.formFrame.setObjectName(u"formFrame")
        self.formLayout = QFormLayout(self.formFrame)
        self.formLayout.setObjectName(u"formLayout")
        self.labelWelcome = QLabel(self.formFrame)
        self.labelWelcome.setObjectName(u"labelWelcome")
        self.labelWelcome.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.labelWelcome)

        self.labelIDNumber = QLabel(self.formFrame)
        self.labelIDNumber.setObjectName(u"labelIDNumber")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.labelIDNumber)

        self.lineIDNumber = QLineEdit(self.formFrame)
        self.lineIDNumber.setObjectName(u"lineIDNumber")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineIDNumber.sizePolicy().hasHeightForWidth())
        self.lineIDNumber.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.lineIDNumber)

        self.labelPassword = QLabel(self.formFrame)
        self.labelPassword.setObjectName(u"labelPassword")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.labelPassword)

        self.linePassword = QLineEdit(self.formFrame)
        self.linePassword.setObjectName(u"linePassword")
        sizePolicy2.setHeightForWidth(self.linePassword.sizePolicy().hasHeightForWidth())
        self.linePassword.setSizePolicy(sizePolicy2)
        self.linePassword.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.linePassword)

        self.btnLogin = QPushButton(self.formFrame)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setCursor(QCursor(Qt.PointingHandCursor))

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.btnLogin)

        self.btnSignUp = QPushButton(self.formFrame)
        self.btnSignUp.setObjectName(u"btnSignUp")
        self.btnSignUp.setCursor(QCursor(Qt.PointingHandCursor))

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.btnSignUp)


        self.horizontalLayout.addWidget(self.formFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.labelWelcome.setText(QCoreApplication.translate("MainWindow", u"Welcome to WattWise!", None))
        self.labelIDNumber.setText(QCoreApplication.translate("MainWindow", u"ID Number", None))
        self.lineIDNumber.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID Number", None))
        self.labelPassword.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.linePassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.btnLogin.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.btnSignUp.setText(QCoreApplication.translate("MainWindow", u"Don't have an account? Sign up.", None))
    # retranslateUi

