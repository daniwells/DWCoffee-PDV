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
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)
import images

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1160, 778)
        Dialog.setStyleSheet(u"background-color: #F3F3F3;")
        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 190, 1161, 481))
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
        self.frame_10.setGeometry(QRect(0, 318, 460, 144))
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
        self.pushButton.setGeometry(QRect(0, 72, 453, 68))
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
        self.listWidget = QListWidget(self.frame_5)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 51, 450, 268))
        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(61, 20, 601, 40))
        self.comboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	border: .5px solid rgba(0,0,0,.5);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	background-color: #F3F3F3;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"	border: .5px solid rgba(0,0,0,1);\n"
"}\n"
"\n"
"/*QComboBox::down-arrow{\n"
"	image: url(:/imagens/expand_more_FILL0_wght400_GRAD0_opsz24.png);\n"
"	width:30px;\n"
"	height:30px;\n"
"	border-color: transparent;\n"
"}*/")
        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(50, 90, 611, 391))
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setStyleSheet(u"QScrollBar{\n"
"	border-color: transparent; \n"
"	border: none;\n"
"	background-color: none;\n"
"	background: none;\n"
"}\n"
"QScrollBar:vertical{ \n"
"	width: 2px;\n"
"	background-color: black;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{ \n"
"	border: none;\n"
"	border-color: transparent;\n"
"}")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 609, 539))
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
        self.frame_4.setStyleSheet(u"QFrame:hover{\n"
"	border: 1px solid #522E2E;\n"
"	padding: 10px;\n"
"}")
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
        self.frame_6.setStyleSheet(u"QFrame:hover{\n"
"	border: 1px solid #522E2E;\n"
"	padding: 10px;\n"
"}")
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
        self.frame_8.setStyleSheet(u"QFrame:hover{\n"
"	border: 1px solid #522E2E;\n"
"	padding: 10px;\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_12 = QFrame(self.frame_8)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(0, 0, 151, 181))
        self.frame_12.setContextMenuPolicy(Qt.NoContextMenu)
        self.frame_12.setAutoFillBackground(False)
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
        self.frame_13.setGeometry(QRect(20, 269, 151, 221))
        self.frame_13.setStyleSheet(u"QFrame:hover{\n"
"	border: 1px solid #522E2E;\n"
"	padding: 10px;\n"
"}")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(0, 0, 151, 181))
        self.frame_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_14.setStyleSheet(u"image: url(:/imagens/Rectangle 69.png);")
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
        self.frame_17.setStyleSheet(u"QFrame:hover{\n"
"	border: 1px solid #522E2E;\n"
"	padding: 10px;\n"
"}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(0, 0, 151, 181))
        self.frame_18.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_18.setStyleSheet(u"image: url(:/imagens/image 5.png);")
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
        self.frame_19.setStyleSheet(u"QFrame:hover{\n"
"	border: 1px solid #522E2E;\n"
"	padding: 10px;\n"
"}")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(0, 0, 151, 181))
        self.frame_20.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_20.setStyleSheet(u"image: url(:/imagens/Rectangle 71.png);")
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
        self.comboBox.raise_()
        self.scrollArea.raise_()
        self.frame_5.raise_()
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
        self.label.setGeometry(QRect(18, 9, 96, 86))
        self.label.setStyleSheet(u"image: url(:/imagens/cGUFyIrl2tqx3cWHufs9--1--5d252-svg (1) 4.png);")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(470, 4, 281, 91))
        self.label_2.setStyleSheet(u"color: #F8E6D3")
        self.frame_22 = QFrame(Dialog)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setGeometry(QRect(0, 141, 111, 641))
        self.frame_22.setStyleSheet(u"background-color: #522E2E")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setGeometry(QRect(0, 0, 111, 491))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_23)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_31 = QFrame(self.frame_23)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_31.setStyleSheet(u"QFrame:hover{\n"
"	background-color: rgb(136, 85, 78);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.pushButton_27 = QPushButton(self.frame_31)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setGeometry(QRect(9, 9, 71, 41))
        self.pushButton_27.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_27.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;\n"
"image: url(:/imagens/transferir (1) 1.png);\n"
"color: white;")
        self.frame_40 = QFrame(self.frame_31)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setGeometry(QRect(0, 140, 91, 96))
        self.frame_40.setStyleSheet(u"color: white;")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.pushButton_28 = QPushButton(self.frame_40)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setGeometry(QRect(9, 10, 75, 44))
        self.pushButton_28.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;\n"
"image: url(:/imagens/transferir (1) 1.png);\n"
"color: white;")
        self.label_40 = QLabel(self.frame_40)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(18, 60, 60, 16))
        self.pushButton_6 = QPushButton(self.frame_31)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(10, 60, 75, 24))
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"border-color: transparent;\n"
"background-color: transparent;\n"
"color: white")

        self.verticalLayout.addWidget(self.frame_31)

        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_24.setStyleSheet(u"QFrame:hover{\n"
"	background-color: rgb(136, 85, 78);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.pushButton_11 = QPushButton(self.frame_24)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(10, 11, 66, 36))
        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;\n"
"image: url(:/imagens/\ud83e\udd86 icon _cart o_.png);\n"
"color: white;")
        self.frame_29 = QFrame(self.frame_24)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setGeometry(QRect(0, 140, 91, 96))
        self.frame_29.setStyleSheet(u"color: white;")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.pushButton_12 = QPushButton(self.frame_29)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(9, 10, 75, 44))
        self.pushButton_12.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;\n"
"image: url(:/imagens/transferir (1) 1.png);\n"
"color: white;")
        self.label_24 = QLabel(self.frame_29)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(18, 60, 60, 16))
        self.pushButton_9 = QPushButton(self.frame_24)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(7, 58, 75, 24))
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet(u"border-color: transparent;\n"
"background-color: transparent;\n"
"color: white;")

        self.verticalLayout.addWidget(self.frame_24)

        self.frame_34 = QFrame(self.frame_23)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_34.setStyleSheet(u"QFrame:hover{\n"
"	background-color: rgb(136, 85, 78);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.pushButton_21 = QPushButton(self.frame_34)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setGeometry(QRect(11, 10, 70, 40))
        self.pushButton_21.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_21.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;\n"
"image: url(:/imagens/free-invoice-3155204-2630870 1.png);\n"
"color: white;")
        self.frame_37 = QFrame(self.frame_34)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setGeometry(QRect(0, 140, 91, 96))
        self.frame_37.setStyleSheet(u"color: white;")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.pushButton_22 = QPushButton(self.frame_37)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setGeometry(QRect(9, 10, 75, 44))
        self.pushButton_22.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;\n"
"image: url(:/imagens/transferir (1) 1.png);\n"
"color: white;")
        self.label_34 = QLabel(self.frame_37)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(18, 60, 60, 16))
        self.pushButton_13 = QPushButton(self.frame_34)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(7, 58, 75, 24))
        self.pushButton_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet(u"border-color: transparent;\n"
"background-color: transparent;\n"
"color: white;")

        self.verticalLayout.addWidget(self.frame_34)

        self.frame_36 = QFrame(self.frame_23)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_36.setStyleSheet(u"QFrame:hover{\n"
"	background-color: rgb(136, 85, 78);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.pushButton_25 = QPushButton(self.frame_36)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setGeometry(QRect(12, 11, 69, 39))
        self.pushButton_25.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_25.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;\n"
"image: url(:/imagens/free-monitor-1629555-1383411 1.png);\n"
"color: white;")
        self.frame_39 = QFrame(self.frame_36)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setGeometry(QRect(0, 140, 91, 96))
        self.frame_39.setStyleSheet(u"color: white;")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.pushButton_26 = QPushButton(self.frame_39)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setGeometry(QRect(9, 10, 75, 44))
        self.pushButton_26.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;\n"
"image: url(:/imagens/transferir (1) 1.png);\n"
"color: white;")
        self.label_38 = QLabel(self.frame_39)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(18, 60, 60, 16))
        self.pushButton_14 = QPushButton(self.frame_36)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(8, 60, 75, 24))
        self.pushButton_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_14.setStyleSheet(u"border-color: transparent;\n"
"background-color: transparent;\n"
"color: white;")

        self.verticalLayout.addWidget(self.frame_36)

        self.frame_41 = QFrame(self.frame_23)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_41.setStyleSheet(u"QFrame:hover{\n"
"	background-color: rgb(136, 85, 78);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.pushButton_29 = QPushButton(self.frame_41)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setGeometry(QRect(12, 13, 68, 38))
        self.pushButton_29.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_29.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;\n"
"image: url(:/imagens/mindtouch 1.png);\n"
"color: white;")
        self.frame_42 = QFrame(self.frame_41)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setGeometry(QRect(0, 140, 91, 96))
        self.frame_42.setStyleSheet(u"color: white;")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.pushButton_30 = QPushButton(self.frame_42)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setGeometry(QRect(9, 10, 75, 44))
        self.pushButton_30.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;\n"
"image: url(:/imagens/transferir (1) 1.png);\n"
"color: white;")
        self.label_42 = QLabel(self.frame_42)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(18, 60, 60, 16))
        self.pushButton_15 = QPushButton(self.frame_41)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(10, 56, 75, 24))
        self.pushButton_15.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_15.setStyleSheet(u"border-color: transparent;\n"
"background-color: transparent;\n"
"color: white;")

        self.verticalLayout.addWidget(self.frame_41)

        self.pushButton_10 = QPushButton(Dialog)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(110, 140, 16, 641))
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
        self.frame_21 = QFrame(Dialog)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(-10, 667, 1171, 111))
        self.frame_21.setStyleSheet(u"background-color:#DBDBDB;\n"
"border-color: transparent;\n"
"")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.pushButton_7 = QPushButton(self.frame_21)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(440, 38, 131, 31))
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
"		color: rgb(61, 21, 21);\n"
"}\n"
"")
        self.pushButton_8 = QPushButton(self.frame_21)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(640, 38, 131, 31))
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"	border: transparent;\n"
"	background-color: transparent;\n"
"	font-size: 22px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(61, 21, 21);\n"
"}")
        self.frame_2.raise_()
        self.frame.raise_()
        self.frame_21.raise_()
        self.frame_22.raise_()
        self.pushButton_10.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"SUB TOTAL:", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"FINALIZE ORDER", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">YOUR ORDER</p></body></html>", None))
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
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:36pt;\">D.W Coffee</span></p></body></html>", None))
        self.pushButton_27.setText("")
        self.pushButton_28.setText("")
        self.label_40.setText(QCoreApplication.translate("Dialog", u"New Order", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"NEW ORDER", None))
        self.pushButton_11.setText("")
        self.pushButton_12.setText("")
        self.label_24.setText(QCoreApplication.translate("Dialog", u"New Order", None))
        self.pushButton_9.setText(QCoreApplication.translate("Dialog", u"PAYMENT", None))
        self.pushButton_21.setText("")
        self.pushButton_22.setText("")
        self.label_34.setText(QCoreApplication.translate("Dialog", u"New Order", None))
        self.pushButton_13.setText(QCoreApplication.translate("Dialog", u"ORDERS", None))
        self.pushButton_25.setText("")
        self.pushButton_26.setText("")
        self.label_38.setText(QCoreApplication.translate("Dialog", u"New Order", None))
        self.pushButton_14.setText(QCoreApplication.translate("Dialog", u"MONITOR", None))
        self.pushButton_29.setText("")
        self.pushButton_30.setText("")
        self.label_42.setText(QCoreApplication.translate("Dialog", u"New Order", None))
        self.pushButton_15.setText(QCoreApplication.translate("Dialog", u"SETTINGS", None))
        self.pushButton_10.setText("")
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"New Order", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"Payment", None))
    # retranslateUi

