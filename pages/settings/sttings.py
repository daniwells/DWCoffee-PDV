# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)
import imagens_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1160, 768)
        Dialog.setStyleSheet(u"background-color: #F3F3F3;")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 40, 1161, 101))
        self.frame.setStyleSheet(u"background-color: #121212")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 135, 102))
        self.frame_2.setStyleSheet(u"background-color: #D4A26F")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(18, 6, 98, 90))
        self.label.setStyleSheet(u"image: url(:/imagens/cGUFyIrl2tqx3cWHufs9--1--5d252-svg (1) 4.png);")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(470, 4, 281, 91))
        self.label_2.setStyleSheet(u"color: #F8E6D3")
        self.pushButton_9 = QPushButton(Dialog)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(-3, 140, 22, 631))
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"	image: url(:/imagens/Arrow 2.png);\n"
"	background-color: rgba(0, 0, 0, .1);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(0, 0, 0, .2);\n"
"}")
        self.pushButton_10 = QPushButton(Dialog)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(110, 140, 16, 631))
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet(u"QPushButton{\n"
"	image: url(:/imagens/Arrow 1.png);\n"
"	background-color: rgba(0, 0, 0, .1);\n"
"	transform: rotate(45deg)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(0, 0, 0, .2);\n"
"}")
        self.frame_15 = QFrame(Dialog)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(0, 141, 111, 631))
        self.frame_15.setStyleSheet(u"background-color: #522E2E")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.label_12 = QLabel(self.frame_17)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(-1, -14, 91, 81))
        self.label_12.setStyleSheet(u"image: url(:/imagens/transferir (1) 1.png);")
        self.label_13 = QLabel(self.frame_17)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(15, 60, 61, 16))
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_15)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.label_14 = QLabel(self.frame_18)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(1, 4, 83, 49))
        self.label_14.setStyleSheet(u"image: url(:/imagens/\ud83e\udd86 icon _cart o_.png);")
        self.label_15 = QLabel(self.frame_18)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(24, 60, 44, 16))
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"text-align: center;")

        self.verticalLayout.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_15)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.label_16 = QLabel(self.frame_19)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(-1, -14, 91, 81))
        self.label_16.setStyleSheet(u"image: url(:/imagens/free-invoice-3155204-2630870 1.png);")
        self.label_17 = QLabel(self.frame_19)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(24, 60, 41, 16))
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_15)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.label_18 = QLabel(self.frame_20)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(-1, -14, 91, 81))
        self.label_18.setStyleSheet(u"image: url(:/imagens/free-monitor-1629555-1383411 1.png);")
        self.label_19 = QLabel(self.frame_20)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(22, 60, 51, 16))
        self.label_19.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_15)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.label_20 = QLabel(self.frame_21)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(-1, -14, 91, 81))
        self.label_20.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_20.setStyleSheet(u"image: url(:/imagens/mindtouch 1.png);\n"
"")
        self.label_21 = QLabel(self.frame_21)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(21, 60, 51, 16))
        self.label_21.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_21.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.frame_21)

        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(260, 170, 321, 281))
        self.frame_3.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px solid black;\n"
"background-color: white;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 0, 321, 55))
        self.frame_6.setStyleSheet(u"border-top-right-radius: 10px;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-right-radius: 0px; \n"
"border-bottom-left-radius: 0px;\n"
"background-color: #E5E5E5;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(23, 6, 77, 43))
        self.label_3.setStyleSheet(u"border-color: transparent;\n"
"font-size: 24px;\n"
"font-weight: 600; ")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(29, 71, 56, 43))
        self.label_4.setStyleSheet(u"border-color: transparent;\n"
"font-size: 20px;\n"
"font-weight: 400; ")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(29, 119, 109, 43))
        self.label_5.setStyleSheet(u"border-color: transparent;\n"
"font-size: 20px;\n"
"font-weight: 400; ")
        self.radioButton = QRadioButton(self.frame_3)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(190, 132, 41, 21))
        self.radioButton.setStyleSheet(u"border-color: transparent;\n"
"font-size: 14px;\n"
"\n"
"")
        self.radioButton_3 = QRadioButton(self.frame_3)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(249, 132, 43, 21))
        self.radioButton_3.setStyleSheet(u"border-color: transparent;\n"
"font-size: 14px;\n"
"\n"
"")
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(28, 167, 128, 88))
        self.label_6.setStyleSheet(u"image: url(:/imagens/image 22.png);\n"
"border-radius: 0px;\n"
"")
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(165, 168, 129, 88))
        self.label_7.setStyleSheet(u"image: url(:/imagens/image 23.png);\n"
"border-radius: 0px;\n"
"")
        self.frame_4 = QFrame(Dialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(600, 170, 321, 186))
        self.frame_4.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px solid black;\n"
"background-color: white;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(0, 0, 321, 55))
        self.frame_7.setStyleSheet(u"border-top-right-radius: 10px;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-right-radius: 0px; \n"
"border-bottom-left-radius: 0px;\n"
"background-color: #E5E5E5;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(23, 6, 77, 43))
        self.label_8.setStyleSheet(u"border-color: transparent;\n"
"font-size: 24px;\n"
"font-weight: 600; ")
        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(29, 71, 101, 43))
        self.label_9.setStyleSheet(u"border-color: transparent;\n"
"font-size: 20px;\n"
"font-weight: 400; ")
        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(29, 119, 109, 43))
        self.label_10.setStyleSheet(u"border-color: transparent;\n"
"font-size: 20px;\n"
"font-weight: 400; ")
        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(188, 86, 100, 20))
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	border-color: rgba(0, 0, 0, .4);\n"
"	padding-left: 10px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"	border-color: rgba(0, 0, 0, 1);\n"
"}\n"
"")
        self.frame_5 = QFrame(Dialog)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(600, 370, 321, 281))
        self.frame_5.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px solid black;\n"
"background-color: white;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(0, 0, 321, 55))
        self.frame_8.setStyleSheet(u"border-top-right-radius: 10px;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-right-radius: 0px; \n"
"border-bottom-left-radius: 0px;\n"
"background-color: #E5E5E5;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_23 = QLabel(self.frame_8)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(23, 6, 100, 43))
        self.label_23.setStyleSheet(u"border-color: transparent;\n"
"font-size: 24px;\n"
"font-weight: 600; ")
        self.label_24 = QLabel(self.frame_5)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(29, 71, 110, 43))
        self.label_24.setStyleSheet(u"border-color: transparent;\n"
"font-size: 20px;\n"
"font-weight: 400; ")
        self.label_25 = QLabel(self.frame_5)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(29, 119, 170, 43))
        self.label_25.setStyleSheet(u"border-color: transparent;\n"
"font-size: 20px;\n"
"font-weight: 400; ")
        self.label_26 = QLabel(self.frame_5)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(30, 170, 130, 43))
        self.label_26.setStyleSheet(u"border-color: transparent;\n"
"font-size: 20px;\n"
"font-weight: 400; ")
        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(220, 80, 71, 30))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	background-color: rgba(61, 21, 21, .75);\n"
"	color: white;\n"
"	font-weight: 700;\n"
"	border-color: transparent;\n"
"	padding: 6px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(61, 21, 21, 1);\n"
"}")
        self.pushButton_2 = QPushButton(self.frame_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(220, 130, 71, 30))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	background-color: rgba(61, 21, 21, .75);\n"
"	color: white;\n"
"	font-weight: 700;\n"
"	border-color: transparent;\n"
"	padding: 6px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(61, 21, 21, 1);\n"
"}")
        self.pushButton_3 = QPushButton(self.frame_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(112, 228, 91, 34))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	background-color: rgba(61, 21, 21, .75);\n"
"	color: white;\n"
"	font-weight: 700;\n"
"	border-color: transparent;\n"
"	padding: 6px;\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(61, 21, 21, 1);\n"
"}")
        self.frame.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.frame_5.raise_()
        self.frame_15.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:36pt;\">D.W Coffee</span></p></body></html>", None))
        self.pushButton_9.setText("")
        self.pushButton_10.setText("")
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("Dialog", u"NEW ORDER", None))
        self.label_14.setText("")
        self.label_15.setText(QCoreApplication.translate("Dialog", u"PAYMENT", None))
        self.label_16.setText("")
        self.label_17.setText(QCoreApplication.translate("Dialog", u"ORDERS", None))
        self.label_18.setText("")
        self.label_19.setText(QCoreApplication.translate("Dialog", u"MONITOR", None))
        self.label_20.setText("")
        self.label_21.setText(QCoreApplication.translate("Dialog", u"SETTINGS", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Visual", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Light:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Dark Mode:", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"Off", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"On", None))
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Language", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Language:", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Size World:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Portuguese", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Curitibano", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Japonese", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"German", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"English", None))

        self.label_23.setText(QCoreApplication.translate("Dialog", u"Security", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"Name User:", None))
        self.label_25.setText(QCoreApplication.translate("Dialog", u"Change Password:", None))
        self.label_26.setText(QCoreApplication.translate("Dialog", u"Notifications:", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Change", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Change", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Log Out", None))
    # retranslateUi

