# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sign_up.ui'
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

class Ui_SignUpWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 684)
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
"	font-size: 32px;\n"
"	margin-top: 20px;\n"
"	margin-bottom: 10px;\n"
"	font-family: Arial;\n"
"}\n"
"\n"
"#labelIDNumber, #labelPassword, #labelFirstName, #labelLastName, #labelConfirmPassword {\n"
"	font-size: 16px;\n"
"	font-family: Arial;\n"
"}\n"
"\n"
"#lineIDNumber, #linePassword, #lineFirstName, #lineLastName, #lineConfirmPassword {\n"
"	font-size: 17px;\n"
"	margin-bottom: 20px;\n"
"	font-family: Century Gothic;\n"
"	padding: 10px 12px;\n"
"	border: 2px solid #FF9800;\n"
"	background-color: #FF9800; \n"
"	border-radius: 20px;\n"
"	color: black;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"#btnSignUp {\n"
"	font-size: 16px;\n"
"	font-weight: bold;\n"
"	padding: 10px 12px;\n"
"	background-color: #FF9800;\n"
"	color: black;\n"
"	height: 30px;\n"
"	margin-top: 10px;\n"
"}\n"
"\n"
"#btnSignUp:hover {\n"
"	border: 2px s"
                        "olid #FF9800;\n"
"	background-color: #eee;\n"
"	color: black;\n"
"}\n"
"\n"
"#btnLogin {\n"
"	font-size: 16px;\n"
"	color: black;\n"
"	background-color: white;\n"
"	border: 0;\n"
"}\n"
"\n"
"#btnLogin:hover{\n"
"	color: #666;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formFrame = QFrame(self.centralwidget)
        self.formFrame.setObjectName(u"formFrame")
        self.formLayout = QFormLayout(self.formFrame)
        self.formLayout.setObjectName(u"formLayout")
        self.labelWelcome = QLabel(self.formFrame)
        self.labelWelcome.setObjectName(u"labelWelcome")
        self.labelWelcome.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.labelWelcome)

        self.labelFirstName = QLabel(self.formFrame)
        self.labelFirstName.setObjectName(u"labelFirstName")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.labelFirstName)

        self.lineFirstName = QLineEdit(self.formFrame)
        self.lineFirstName.setObjectName(u"lineFirstName")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineFirstName.sizePolicy().hasHeightForWidth())
        self.lineFirstName.setSizePolicy(sizePolicy)
        self.lineFirstName.setClearButtonEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.lineFirstName)

        self.labelLastName = QLabel(self.formFrame)
        self.labelLastName.setObjectName(u"labelLastName")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.labelLastName)

        self.lineLastName = QLineEdit(self.formFrame)
        self.lineLastName.setObjectName(u"lineLastName")
        sizePolicy.setHeightForWidth(self.lineLastName.sizePolicy().hasHeightForWidth())
        self.lineLastName.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.lineLastName)

        self.labelIDNumber = QLabel(self.formFrame)
        self.labelIDNumber.setObjectName(u"labelIDNumber")

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.labelIDNumber)

        self.lineIDNumber = QLineEdit(self.formFrame)
        self.lineIDNumber.setObjectName(u"lineIDNumber")
        sizePolicy.setHeightForWidth(self.lineIDNumber.sizePolicy().hasHeightForWidth())
        self.lineIDNumber.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.lineIDNumber)

        self.labelPassword = QLabel(self.formFrame)
        self.labelPassword.setObjectName(u"labelPassword")

        self.formLayout.setWidget(7, QFormLayout.SpanningRole, self.labelPassword)

        self.linePassword = QLineEdit(self.formFrame)
        self.linePassword.setObjectName(u"linePassword")
        sizePolicy.setHeightForWidth(self.linePassword.sizePolicy().hasHeightForWidth())
        self.linePassword.setSizePolicy(sizePolicy)
        self.linePassword.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(8, QFormLayout.SpanningRole, self.linePassword)

        self.labelConfirmPassword = QLabel(self.formFrame)
        self.labelConfirmPassword.setObjectName(u"labelConfirmPassword")

        self.formLayout.setWidget(9, QFormLayout.SpanningRole, self.labelConfirmPassword)

        self.lineConfirmPassword = QLineEdit(self.formFrame)
        self.lineConfirmPassword.setObjectName(u"lineConfirmPassword")
        sizePolicy.setHeightForWidth(self.lineConfirmPassword.sizePolicy().hasHeightForWidth())
        self.lineConfirmPassword.setSizePolicy(sizePolicy)
        self.lineConfirmPassword.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(10, QFormLayout.SpanningRole, self.lineConfirmPassword)

        self.btnSignUp = QPushButton(self.formFrame)
        self.btnSignUp.setObjectName(u"btnSignUp")
        self.btnSignUp.setCursor(QCursor(Qt.PointingHandCursor))

        self.formLayout.setWidget(11, QFormLayout.SpanningRole, self.btnSignUp)

        self.btnLogin = QPushButton(self.formFrame)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setCursor(QCursor(Qt.PointingHandCursor))

        self.formLayout.setWidget(12, QFormLayout.SpanningRole, self.btnLogin)


        self.horizontalLayout.addWidget(self.formFrame)

        self.separator = QFrame(self.centralwidget)
        self.separator.setObjectName(u"separator")
        self.separator.setFrameShape(QFrame.VLine)
        self.separator.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.separator)

        self.logoFrame = QFrame(self.centralwidget)
        self.logoFrame.setObjectName(u"logoFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logoFrame.sizePolicy().hasHeightForWidth())
        self.logoFrame.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.logoFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.logoFrame)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QSize(300, 300))
        self.label.setMaximumSize(QSize(300, 300))
        self.label.setBaseSize(QSize(300, 300))
        self.label.setPixmap(QPixmap(u":/images/assets/logo-white.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.logoFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelWelcome.setText(QCoreApplication.translate("MainWindow", u"Sign Up to WattWise!", None))
        self.labelFirstName.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.lineFirstName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex. Juan", None))
        self.labelLastName.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.lineLastName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex. Dela Cruz", None))
        self.labelIDNumber.setText(QCoreApplication.translate("MainWindow", u"ID Number", None))
        self.lineIDNumber.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex. 20111272365", None))
        self.labelPassword.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.linePassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.labelConfirmPassword.setText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.lineConfirmPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.btnSignUp.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.btnLogin.setText(QCoreApplication.translate("MainWindow", u"Already have an account? Login.", None))
        self.label.setText("")
    # retranslateUi

