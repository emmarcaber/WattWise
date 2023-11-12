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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import app.resources.login_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(997, 623)
        MainWindow.setStyleSheet(u"background-color: #eee;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 50, 979, 491))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btnLetterC = QPushButton(self.frame)
        self.btnLetterC.setObjectName(u"btnLetterC")
        self.btnLetterC.setGeometry(QRect(50, 210, 106, 241))
        self.btnLetterC.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnLetterC.setStyleSheet(u"font-size: 40px;\n"
"background-color: #0167FE;\n"
"color: white;\n"
"height: 100px;")
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(180, 340, 631, 110))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setSpacing(25)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnSix = QPushButton(self.layoutWidget)
        self.btnSix.setObjectName(u"btnSix")
        self.btnSix.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSix.setStyleSheet(u"font-size: 40px;\n"
"background-color: #0167FE;\n"
"color: white;\n"
"height: 100px;")

        self.horizontalLayout_2.addWidget(self.btnSix)

        self.btnSeven = QPushButton(self.layoutWidget)
        self.btnSeven.setObjectName(u"btnSeven")
        self.btnSeven.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSeven.setStyleSheet(u"font-size: 40px;\n"
"background-color: #0167FE;\n"
"color: white;\n"
"height: 100px;")

        self.horizontalLayout_2.addWidget(self.btnSeven)

        self.btnEight = QPushButton(self.layoutWidget)
        self.btnEight.setObjectName(u"btnEight")
        self.btnEight.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnEight.setStyleSheet(u"font-size: 40px;\n"
"background-color: #0167FE;\n"
"color: white;\n"
"height: 100px;")

        self.horizontalLayout_2.addWidget(self.btnEight)

        self.btnNine = QPushButton(self.layoutWidget)
        self.btnNine.setObjectName(u"btnNine")
        self.btnNine.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnNine.setStyleSheet(u"font-size: 40px;\n"
"background-color: #0167FE;\n"
"color: white;\n"
"height: 100px;")

        self.horizontalLayout_2.addWidget(self.btnNine)

        self.btnZero = QPushButton(self.layoutWidget)
        self.btnZero.setObjectName(u"btnZero")
        self.btnZero.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnZero.setStyleSheet(u"font-size: 40px;\n"
"background-color: #0167FE;\n"
"color: white;\n"
"height: 100px;")

        self.horizontalLayout_2.addWidget(self.btnZero)

        self.layoutWidget1 = QWidget(self.frame)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(180, 210, 631, 110))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setSpacing(25)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnOne = QPushButton(self.layoutWidget1)
        self.btnOne.setObjectName(u"btnOne")
        self.btnOne.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnOne.setStyleSheet(u"font-size: 40px;\n"
"background-color: #0167FE;\n"
"color: white;\n"
"height: 100px;")

        self.horizontalLayout.addWidget(self.btnOne)

        self.btnTwo = QPushButton(self.layoutWidget1)
        self.btnTwo.setObjectName(u"btnTwo")
        self.btnTwo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnTwo.setStyleSheet(u"font-size: 40px;\n"
"background-color: #0167FE;\n"
"color: white;\n"
"height: 100px;")

        self.horizontalLayout.addWidget(self.btnTwo)

        self.btnThree = QPushButton(self.layoutWidget1)
        self.btnThree.setObjectName(u"btnThree")
        self.btnThree.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnThree.setStyleSheet(u"font-size: 40px;\n"
"background-color: #0167FE;\n"
"color: white;\n"
"height: 100px;")

        self.horizontalLayout.addWidget(self.btnThree)

        self.btnFour = QPushButton(self.layoutWidget1)
        self.btnFour.setObjectName(u"btnFour")
        self.btnFour.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnFour.setStyleSheet(u"font-size: 40px;\n"
"background-color: #0167FE;\n"
"color: white;\n"
"height: 100px;")

        self.horizontalLayout.addWidget(self.btnFour)

        self.btnFive = QPushButton(self.layoutWidget1)
        self.btnFive.setObjectName(u"btnFive")
        self.btnFive.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnFive.setStyleSheet(u"font-size: 40px;\n"
"background-color: #0167FE;\n"
"color: white;\n"
"height: 100px;")

        self.horizontalLayout.addWidget(self.btnFive)

        self.btnDelete = QPushButton(self.frame)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setGeometry(QRect(830, 210, 106, 241))
        self.btnDelete.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDelete.setStyleSheet(u"font-size: 40px;\n"
"background-color: #888;\n"
"color: white;\n"
"height: 100px;")
        self.layoutWidget2 = QWidget(self.frame)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(300, 40, 405, 146))
        self.verticalLayout = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.txtIDNumber = QLineEdit(self.layoutWidget2)
        self.txtIDNumber.setObjectName(u"txtIDNumber")
        self.txtIDNumber.setStyleSheet(u"font-size: 48px;\n"
"font-family: Century Gothic;\n"
"background-color: #0167FE;\n"
"color: white;\n"
"padding: 3px;\n"
"height: 80px;")
        self.txtIDNumber.setAlignment(Qt.AlignCenter)
        self.txtIDNumber.setReadOnly(True)

        self.verticalLayout.addWidget(self.txtIDNumber)

        self.idNumberLabel = QLabel(self.layoutWidget2)
        self.idNumberLabel.setObjectName(u"idNumberLabel")
        self.idNumberLabel.setStyleSheet(u"font-size: 24px;\n"
"font-family: Century Gothic;")
        self.idNumberLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.idNumberLabel)

        self.dateLabel = QLabel(self.centralwidget)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setGeometry(QRect(790, 560, 201, 19))
        self.dateLabel.setStyleSheet(u"font-size: 16px;")
        self.dateLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.timeLabel = QLabel(self.centralwidget)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setGeometry(QRect(850, 580, 141, 20))
        self.timeLabel.setStyleSheet(u"font-size: 16px;")
        self.timeLabel.setAlignment(Qt.AlignCenter)
        self.labelLogo = QLabel(self.centralwidget)
        self.labelLogo.setObjectName(u"labelLogo")
        self.labelLogo.setGeometry(QRect(0, 0, 101, 101))
        self.labelLogo.setCursor(QCursor(Qt.ArrowCursor))
        self.labelLogo.setPixmap(QPixmap(u":/images/images/wattwise-logo.png"))
        self.labelLogo.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnLetterC.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btnSix.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btnSeven.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btnEight.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btnNine.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btnZero.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btnOne.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btnTwo.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btnThree.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btnFour.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btnFive.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btnDelete.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
        self.idNumberLabel.setText(QCoreApplication.translate("MainWindow", u"ID NUMBER", None))
        self.dateLabel.setText(QCoreApplication.translate("MainWindow", u"November 11, 2023", None))
        self.timeLabel.setText(QCoreApplication.translate("MainWindow", u"07:36:53 PM", None))
        self.labelLogo.setText("")
    # retranslateUi
