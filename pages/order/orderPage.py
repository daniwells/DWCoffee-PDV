# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'orderPage.ui'
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
    QLabel, QPushButton, QScrollArea, QScrollBar,
    QSizePolicy, QVBoxLayout, QWidget)

import images

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1160, 768)
        Dialog.setStyleSheet(u"background-color: rgb(250, 233, 234);")
        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 190, 1161, 581))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-top: 0.5px solid rgba(0,0,0,.4);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(710, 19, 460, 470))
        self.frame_5.setStyleSheet(u"QFrame{\n"
"	border: .5px solid black\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(0, 320, 460, 150))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_10)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(36, 28, 108, 16))
        self.label_3.setStyleSheet(u"border-color: transparent;\n"
"font-weight: bold;\n"
"font-size: 18px;")
        self.pushButton = QPushButton(self.frame_10)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1, 75, 453, 66))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(211, 164, 110, .9);\n"
"	color: white;\n"
"	font-weight: bold;\n"
"	font-size: 20px;	\n"
"	border-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(211, 164, 110, 1);\n"
"}")
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 451, 55))
        self.label_4.setStyleSheet(u"border-color: transparent;\n"
"background-color: rgba(61, 21, 21, .75);\n"
"color: white;\n"
"font-size: 20px;")
        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(61, 20, 587, 40))
        self.comboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	border: .5px solid rgba(0,0,0,.5);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	background-color: rgb(250, 233, 234);\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"	border: .5px solid rgba(0,0,0,1);\n"
"}")
        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(39, 109, 611, 371))
        self.scrollArea.setStyleSheet(u"border-color: transparent")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 609, 369))
        self.verticalScrollBar = QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(590, 0, 17, 401))
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.frame_7 = QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(258, 9, 20, 46))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_15 = QFrame(self.frame_7)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_7)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_16)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(20, 10, 151, 231))
        self.frame_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(0, 0, 151, 181))
        self.frame_9.setStyleSheet(u"image: url(:/imagens/image 1.png);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(1, 189, 140, 16))
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(46, 210, 48, 16))
        self.label_6.setStyleSheet(u"color: #220C0C;\n"
"font-weight: 900;")
        self.frame_6 = QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(210, 10, 151, 231))
        self.frame_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(0, 0, 151, 181))
        self.frame_11.setStyleSheet(u"image: url(:/imagens/image 1.png);\n"
"image: url(:/imagens/image 3.png);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(49, 210, 48, 16))
        self.label_8.setStyleSheet(u"color: #220C0C;\n"
"font-weight: 900;")
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(4, 189, 140, 16))
        self.frame_8 = QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(400, 10, 151, 231))
        self.frame_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_12 = QFrame(self.frame_8)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(0, 0, 151, 181))
        self.frame_12.setStyleSheet(u"image: url(:/imagens/image 4.png);")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.frame_8)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(3, 189, 140, 16))
        self.label_10 = QLabel(self.frame_8)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(48, 210, 48, 16))
        self.label_10.setStyleSheet(u"color: #220C0C;\n"
"font-weight: 900;")
        self.frame_13 = QFrame(self.scrollAreaWidgetContents)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(20, 260, 151, 231))
        self.frame_13.setStyleSheet(u"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(0, 0, 151, 181))
        self.frame_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_14.setStyleSheet(u"image: url(:/imagens/image 1.png);")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.label_11 = QLabel(self.frame_13)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(1, 189, 140, 16))
        self.label_12 = QLabel(self.frame_13)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(46, 210, 48, 16))
        self.label_12.setStyleSheet(u"color: #220C0C;\n"
"font-weight: 900;")
        self.frame_17 = QFrame(self.scrollAreaWidgetContents)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(210, 270, 151, 231))
        self.frame_17.setStyleSheet(u"")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(0, 0, 151, 181))
        self.frame_18.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_18.setStyleSheet(u"image: url(:/imagens/image 1.png);")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.label_13 = QLabel(self.frame_17)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(1, 189, 140, 16))
        self.label_14 = QLabel(self.frame_17)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(46, 210, 48, 16))
        self.label_14.setStyleSheet(u"color: #220C0C;\n"
"font-weight: 900;")
        self.frame_19 = QFrame(self.scrollAreaWidgetContents)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(400, 270, 151, 231))
        self.frame_19.setStyleSheet(u"")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(0, 0, 151, 181))
        self.frame_20.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_20.setStyleSheet(u"image: url(:/imagens/image 1.png);")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.label_15 = QLabel(self.frame_19)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(1, 189, 140, 16))
        self.label_16 = QLabel(self.frame_19)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(46, 210, 48, 16))
        self.label_16.setStyleSheet(u"color: #220C0C;\n"
"font-weight: 900;")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.frame_7.raise_()
        self.verticalScrollBar.raise_()
        self.frame_4.raise_()
        self.frame_6.raise_()
        self.frame_8.raise_()
        self.frame_13.raise_()
        self.frame_17.raise_()
        self.frame_19.raise_()
        self.frame_21 = QFrame(self.frame_2)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(0, 478, 1171, 104))
        self.frame_21.setStyleSheet(u"background-color: #DBDBDB;\n"
"border-color: transparent;")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.pushButton_7 = QPushButton(self.frame_21)
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
        self.pushButton_8 = QPushButton(self.frame_21)
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
        self.scrollArea.raise_()
        self.frame_5.raise_()
        self.comboBox.raise_()
        self.frame_21.raise_()
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 40, 1161, 101))
        self.frame.setStyleSheet(u"background-color: #121212")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 135, 102))
        self.frame_3.setStyleSheet(u"background-color: #D4A26F")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(18, 6, 98, 90))
        self.label.setStyleSheet(u"image: url(:/imagens/cGUFyIrl2tqx3cWHufs9--1--5d252-svg (1) 4.png);")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(470, 4, 281, 91))
        self.label_2.setStyleSheet(u"color: #F8E6D3")
        self.pushButton_9 = QPushButton(Dialog)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(-2, 140, 21, 630))
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"	image: url(:/imagens/Arrow 2.png);\n"
"	background-color: rgba(0, 0, 0, .1);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(0, 0, 0, .2);\n"
"}")
        self.frame_22 = QFrame(Dialog)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setGeometry(QRect(0, 141, 111, 631))
        self.frame_22.setStyleSheet(u"background-color: #522E2E")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_22)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.label_17 = QLabel(self.frame_23)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(-1, -14, 91, 81))
        self.label_17.setStyleSheet(u"image: url(:/imagens/transferir (1) 1.png);")
        self.label_18 = QLabel(self.frame_23)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(15, 60, 68, 16))
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_22)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.label_19 = QLabel(self.frame_24)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(11, 8, 61, 41))
        self.label_19.setStyleSheet(u"image: url(:/imagens/\ud83e\udd86 icon _cart o_.png);")
        self.label_20 = QLabel(self.frame_24)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(24, 60, 55, 16))
        self.label_20.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"text-align: center;")

        self.verticalLayout.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.frame_22)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.label_21 = QLabel(self.frame_25)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(-1, -14, 91, 81))
        self.label_21.setStyleSheet(u"image: url(:/imagens/free-invoice-3155204-2630870 1.png);")
        self.label_22 = QLabel(self.frame_25)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(24, 60, 46, 16))
        self.label_22.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_22)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.label_23 = QLabel(self.frame_26)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(-1, -14, 91, 81))
        self.label_23.setStyleSheet(u"image: url(:/imagens/free-monitor-1629555-1383411 1.png);")
        self.label_24 = QLabel(self.frame_26)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(22, 60, 51, 16))
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.frame_22)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.label_25 = QLabel(self.frame_27)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(-1, -14, 91, 81))
        self.label_25.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_25.setStyleSheet(u"image: url(:/imagens/mindtouch 1.png);\n"
"")
        self.label_26 = QLabel(self.frame_27)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(21, 60, 51, 16))
        self.label_26.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_26.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.frame_27)

        self.pushButton_10 = QPushButton(Dialog)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(110, 140, 16, 631))
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet(u"QPushButton{\n"
"	image: url(:/imagens/Arrow 1.png);\n"
"	background-color: rgba(0, 0, 0, .2);\n"
"	transform: rotate(45deg)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(0, 0, 0, .3);\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"SUB TOTAL:", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"FINALIZE ORDER", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">YOUR ORDER</p></body></html>", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Traditional Espresso", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Double Espresso", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Macchiato", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"Espresso Romano", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"Doppio", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Dialog", u"Ristretto", None))

        self.label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:8pt;\">Traditional Espresso - 300g</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:8pt;\">R$ 7.00</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:8pt;\">R$ 7.00</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:8pt;\">Traditional Espresso - 300g</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:8pt;\">Traditional Espresso - 300g</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:8pt;\">R$ 7.00</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:8pt;\">Traditional Espresso - 300g</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:8pt;\">R$ 7.00</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:8pt;\">Traditional Espresso - 300g</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:8pt;\">R$ 7.00</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:8pt;\">Traditional Espresso - 300g</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:8pt;\">R$ 7.00</span></p></body></html>", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"New Order", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"Payment", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:36pt;\">D.W Coffee</span></p></body></html>", None))
        self.pushButton_9.setText("")
        self.label_17.setText("")
        self.label_18.setText(QCoreApplication.translate("Dialog", u"NEW ORDER", None))
        self.label_19.setText("")
        self.label_20.setText(QCoreApplication.translate("Dialog", u"PAYMENT", None))
        self.label_21.setText("")
        self.label_22.setText(QCoreApplication.translate("Dialog", u"ORDERS", None))
        self.label_23.setText("")
        self.label_24.setText(QCoreApplication.translate("Dialog", u"MONITOR", None))
        self.label_25.setText("")
        self.label_26.setText(QCoreApplication.translate("Dialog", u"SETTINGS", None))
        self.pushButton_10.setText("")
    # retranslateUi

