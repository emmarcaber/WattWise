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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1144, 730)
        MainWindow.setStyleSheet(u"#loginFrame {\n"
"	background-color: #172F5F;\n"
"	padding: 100px 300px;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: white;\n"
"	font-size: 28px;\n"
"	margin-top: 10px;\n"
"}\n"
"\n"
"#lblTitle {\n"
"	font-size: 60px;\n"
"    font-weight: bold;\n"
"	margin-bottom: 20px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	height: 50px;\n"
"	margin-top: 10px;\n"
"    border: 2px solid gray;\n"
"	padding: 5px 15px;\n"
"	font-size: 28px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 2px solid #007bff;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid green;\n"
"}\n"
"\n"
"#btnLogin {\n"
"	margin-top: 30px;\n"
"	height: 80px;\n"
"	width: 100px;\n"
"	color: white;\n"
"	background-color: green;\n"
"	border-radius: 15px;\n"
"	font-size: 28px;\n"
"}\n"
"\n"
"#btnLogin:hover {\n"
"	border: 2px solid green;\n"
"	color: green;\n"
"	background-color: white;\n"
"}")
        self.LoginWidget = QWidget(MainWindow)
        self.LoginWidget.setObjectName(u"LoginWidget")
        self.gridLayout = QGridLayout(self.LoginWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.loginFrame = QFrame(self.LoginWidget)
        self.loginFrame.setObjectName(u"loginFrame")
        self.loginFrame.setFrameShape(QFrame.StyledPanel)
        self.loginFrame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.loginFrame)
        self.formLayout.setObjectName(u"formLayout")
        self.lblTitle = QLabel(self.loginFrame)
        self.lblTitle.setObjectName(u"lblTitle")
        self.lblTitle.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lblTitle)

        self.lblUsername = QLabel(self.loginFrame)
        self.lblUsername.setObjectName(u"lblUsername")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lblUsername)

        self.lineIDNumber = QLineEdit(self.loginFrame)
        self.lineIDNumber.setObjectName(u"lineIDNumber")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineIDNumber)

        self.lblPassword = QLabel(self.loginFrame)
        self.lblPassword.setObjectName(u"lblPassword")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lblPassword)

        self.linePassword = QLineEdit(self.loginFrame)
        self.linePassword.setObjectName(u"linePassword")
        self.linePassword.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.linePassword)

        self.btnLogin = QPushButton(self.loginFrame)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setCursor(QCursor(Qt.PointingHandCursor))

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.btnLogin)


        self.gridLayout.addWidget(self.loginFrame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.LoginWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblTitle.setText(QCoreApplication.translate("MainWindow", u"WattWise", None))
        self.lblUsername.setText(QCoreApplication.translate("MainWindow", u"ID Number", None))
        self.lineIDNumber.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID Number", None))
        self.lblPassword.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.linePassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.btnLogin.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

