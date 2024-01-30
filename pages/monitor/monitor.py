# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'monitor.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import imagens_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1160, 768)
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
        self.frame_16 = QFrame(Dialog)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(0, 670, 1171, 101))
        self.frame_16.setStyleSheet(u"background-color: #DBDBDB;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.pushButton_7 = QPushButton(self.frame_16)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(437, 35, 131, 31))
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"	border: transparent;\n"
"	background-color: transparent;\n"
"	font-size: 22px;\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgba(61, 21, 21, .75);\n"
"}\n"
"")
        self.pushButton_8 = QPushButton(self.frame_16)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(637, 35, 131, 31))
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"	border: transparent;\n"
"	background-color: transparent;\n"
"	font-size: 22px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgba(61, 21, 21, .75);\n"
"}")
        self.pushButton_9 = QPushButton(Dialog)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(0, 140, 21, 631))
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"	image: url(:/imagens/Arrow 2.png);\n"
"	background-color: rgba(0, 0, 0, .1);\n"
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
        self.label_14.setGeometry(QRect(11, 8, 61, 41))
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

        self.pushButton_10 = QPushButton(Dialog)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(110, 141, 16, 631))
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
        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(176, 164, 321, 111))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 70, 41, 32))
        self.label_5.setStyleSheet(u"QLabel{\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"	image: url(:/imagens/image_20-removebg-preview.png);\n"
"	border: .5px solid rgba(0, 0, 0, .5);\n"
"	background-color: white;\n"
"	padding: 5px;\n"
"	border-right-color: transparent;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: .5px solid rgba(0, 0, 0, 1);\n"
"	border-right-color: transparent;\n"
"}\n"
"\n"
"\n"
"")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(159, 10, 51, 41))
        self.label_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_4.setStyleSheet(u"QLabel{\n"
"	image: url(:/imagens/box-icon-vector-21613827 2 (1).png);\n"
"	background-color: rgba(86, 46, 46, .75);\n"
"	padding: 7px\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	background-color: rgba(86, 46, 46, 1);\n"
"}\n"
"\n"
"")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 51, 41))
        self.label_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_3.setStyleSheet(u"QLabel{\n"
"	background-color: rgba(86, 46, 46, .75);\n"
"	image: url(:/imagens/\ud83e\udd86 icon _cart o_.png);\n"
"	padding: 10px\n"
"\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	background-color: rgba(86, 46, 46, 1);\n"
"}\n"
"")
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(61, 10, 81, 41))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(86, 46, 46, .75);\n"
"	color: white;\n"
"	border: transparent;\n"
"	font-size: 13px;\n"
"	font-weight: bold;\n"
"	padding-right: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(86, 46, 46, 1);\n"
"}\n"
"\n"
"")
        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(210, 71, 101, 31))
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	border-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"	border: .5px solid rgba(0, 0, 0, .5);\n"
"	font-size: 13px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"	border: .5px solid rgba(0, 0, 0, 1);;\n"
"}")
        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(210, 10, 81, 41))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(86, 46, 46, .75);\n"
"	color: white;\n"
"	border: transparent;\n"
"	font-size: 13px;\n"
"	font-weight: bold;\n"
"	padding-right: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(86, 46, 46, 1);\n"
"}\n"
"\n"
"")
        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(50, 70, 151, 32))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"	border: .5px solid rgba(0, 0, 0, .5);\n"
"	border-left-color: transparent;\n"
"	font-size: 13px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: .5px solid rgba(0, 0, 0, 1);\n"
"	border-left-color: transparent;\n"
"}\n"
"\n"
"")
        self.frame_4 = QFrame(Dialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(190, 290, 213, 60))
        self.frame_4.setStyleSheet(u"border: .5px solid rgba(0, 0, 0, .2);\n"
"background: #E3E3E3;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(36, 10, 131, 41))
        self.label_6.setStyleSheet(u"border-color: transparent;\n"
"font-size: 20px;\n"
"font-weight: bold;")
        self.frame_5 = QFrame(Dialog)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(419, 290, 213, 60))
        self.frame_5.setStyleSheet(u"border: .5px solid rgba(0, 0, 0, .2);\n"
"background: #E3E3E3")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(17, 10, 181, 41))
        self.label_7.setStyleSheet(u"border-color: transparent;\n"
"font-size: 20px;\n"
"font-weight: bold;")
        self.frame_6 = QFrame(Dialog)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(875, 290, 213, 60))
        self.frame_6.setStyleSheet(u"border: .5px solid rgba(0, 0, 0, .2);\n"
"background: #E3E3E3")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(34, 10, 141, 41))
        self.label_9.setStyleSheet(u"border-color: transparent;\n"
"font-size: 20px;\n"
"font-weight: bold;")
        self.frame_7 = QFrame(Dialog)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(648, 290, 213, 60))
        self.frame_7.setStyleSheet(u"border: .5px solid rgba(0, 0, 0, .2);\n"
"background: #E3E3E3")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(61, 10, 81, 41))
        self.label_8.setStyleSheet(u"border-color: transparent;\n"
"font-size: 20px;\n"
"font-weight: bold;")
        self.frame.raise_()
        self.frame_16.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.frame_5.raise_()
        self.frame_6.raise_()
        self.frame_7.raise_()
        self.frame_15.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:36pt;\">D.W Coffee</span></p></body></html>", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"orders", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"Monitor", None))
        self.pushButton_9.setText("")
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
        self.pushButton_10.setText("")
        self.label_5.setText("")
        self.label_4.setText("")
        self.label_3.setText("")
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"COUNTER", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"1111", None))

        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"DELIVERY", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Search Word", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"SCHEDULED", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"IN PRODUCTION", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"IN DELIVERY", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"READY", None))
    # retranslateUi

