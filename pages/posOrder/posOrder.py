# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'posOrder.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QWidget)
import imagens_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1160, 768)
        Dialog.setStyleSheet(u"background-color: rgb(255, 243, 243);")
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
        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(309, 260, 541, 361))
        self.frame_3.setStyleSheet(u"background-color: #F6F6F6;\n"
"border: .5px solid rgba(0,0,0,.4);\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(79, 70, 59, 55))
        self.label_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_4.setStyleSheet(u"QLabel{\n"
"	image: url(:/imagens/istockphoto-1313175215-612x612-removebg-preview (1) 2.png);\n"
"	border-color: transparent;\n"
"	padding: 7px;\n"
"	font-size: 13px;\n"
"	font-weight: 500;\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"	background-color: rgba(61, 21, 21, .75);\n"
"	padding:  9px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	background-color: rgba(61, 21, 21, 1);\n"
"	\n"
"}\n"
"\n"
"")
        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(137, 70, 107, 55))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(61,21,21,.75);\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"	padding: 7px;\n"
"	padding-left:20px;\n"
"	font-size: 13px;\n"
"	font-weight: 500;\n"
"	text-align: left;\n"
"	color: white;\n"
"	font-weight: 800;\n"
"	font-size: 18px;\n"
"	border-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(61,21,21,1);\n"
"	color: white;\n"
"}\n"
"\n"
"")
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(295, 70, 59, 55))
        self.label_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_7.setStyleSheet(u"QLabel{\n"
"	image: url(:/imagens/image-removebg-preview 2.png);\n"
"	background-color: rgba(212,162,111,.75);\n"
"	padding: 7px;\n"
"	font-size: 13px;\n"
"	font-weight: 500;\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"	border: transparent;\n"
"	padding: 13px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	background-color: rgba(212,162,111,1);\n"
"}\n"
"\n"
"")
        self.pushButton_4 = QPushButton(self.frame_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(353, 70, 107, 55))
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(212,162,111,.75);\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"	padding-left: 7px;\n"
"	font-size: 14px;\n"
"	font-weight: 500;\n"
"	text-align: left;\n"
"	color: white;\n"
"	font-weight: 800;\n"
"	font-size: 15px;\n"
"	border: tranparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(212,162,111,1);\n"
"	color: white;\n"
"}\n"
"\n"
"")
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(81, 157, 59, 55))
        self.label_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_9.setStyleSheet(u"QLabel{\n"
"	image: url(:/imagens/flat-icon-in-black-and-white-style-shelf-vector-10667669-removebg-preview 2.png);\n"
"	background-color: rgba(212,162,111,.75);\n"
"	padding: 7px;\n"
"	font-size: 13px;\n"
"	font-weight: 500;\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"	border: transparent;\n"
"	padding: 10px\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	background-color: rgba(212,162,111,1);\n"
"}\n"
"\n"
"")
        self.pushButton_5 = QPushButton(self.frame_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(139, 157, 107, 55))
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(212,162,111,.75);\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"	padding-left: 7px;\n"
"	font-size: 13px;\n"
"	font-weight: 500;\n"
"	text-align: left;\n"
"	color: white;\n"
"	font-weight: 800;\n"
"	border: tranparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(212,162,111,1);\n"
"	color: white;\n"
"}")
        self.pushButton_6 = QPushButton(self.frame_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(353, 156, 107, 55))
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(61,21,21,.75);\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"	padding-left:7px;\n"
"	font-weight: 500;\n"
"	text-align: left;\n"
"	color: white;\n"
"	font-weight: 800;\n"
"	font-size: 15px;\n"
"	border-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(61,21,21,1);\n"
"	color: white;\n"
"}\n"
"\n"
"")
        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(295, 156, 59, 55))
        self.label_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_11.setStyleSheet(u"QLabel{\n"
"	image: url(:/imagens/istockphoto-688550958-612x612 2.png);\n"
"	border-color: transparent;\n"
"	padding: 7px;\n"
"	font-size: 13px;\n"
"	font-weight: 500;\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"	background-color: rgba(61, 21, 21, .75);\n"
"	padding: 10px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	background-color: rgba(61, 21, 21, 1);\n"
"}\n"
"\n"
"")
        self.pushButton_7 = QPushButton(self.frame_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(172, 251, 181, 55))
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(118,0,0,.75);\n"
"	border-radius: 5px;\n"
"	font-size: 13px;\n"
"	font-weight: 500;\n"
"	color: white;\n"
"	font-weight: 800;\n"
"	font-size: 18px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(118,0,0,1);\n"
"	color: white;\n"
"}\n"
"\n"
"")
        self.pushButton_2.raise_()
        self.label_4.raise_()
        self.label_7.raise_()
        self.pushButton_4.raise_()
        self.label_9.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.label_11.raise_()
        self.pushButton_7.raise_()
        self.frame_4 = QFrame(Dialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(309, 210, 241, 51))
        self.frame_4.setStyleSheet(u"background-color: white;\n"
"border-left: .5px solid rgba(0,0,0,.4);\n"
"border-top: .5px solid rgba(0,0,0,.4);\n"
"border-right: .5px solid rgba(0,0,0,.4);\n"
"border-bottom: .5px solid rgba(0,0,0,.2);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(19, 18, 56, 16))
        self.label_3.setStyleSheet(u"border-color: transparent;\n"
"font-size: 17px")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:36pt;\">D.W Coffee</span></p></body></html>", None))
        self.label_4.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"PROOF", None))
        self.label_7.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"TAX INVOICE", None))
        self.label_9.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"SHELVE ORDER", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"NEW ORDER", None))
        self.label_11.setText("")
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"RETURN", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Client:", None))
    # retranslateUi

