# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QWidget)

import images

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1160, 768)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 42, 1161, 101))
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
        self.frame_3.setGeometry(QRect(364, 198, 441, 491))
        self.frame_3.setStyleSheet(u"background-color: white;\n"
"border: .5px solid rgba(0, 0, 0, .3)")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 0, 441, 79))
        self.frame_4.setStyleSheet(u"background-color: #D4A26F;\n"
"border-bottom-color: transparent;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(99, 4, 251, 73))
        self.label_3.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"border-color: transparent")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(38, 115, 91, 31))
        self.label_4.setStyleSheet(u"border-color: transparent;\n"
"font-size: 18px;\n"
"font-weight: 500;")
        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(43, 150, 339, 33))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px;\n"
"	background-color: #F6F6F6;\n"
"	padding-left: 15px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: .5px solid rgba(0, 0, 0, 1);\n"
"}")
        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(45, 232, 339, 33))
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px;\n"
"	background-color: #F6F6F6;\n"
"	padding-left: 15px;\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover{\n"
"	border: .5px solid rgba(0, 0, 0, 1);\n"
"}")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 197, 95, 31))
        self.label_5.setStyleSheet(u"border-color: transparent;\n"
"font-size: 18px;\n"
"font-weight: 500;")
        self.lineEdit_3 = QLineEdit(self.frame_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(45, 317, 339, 33))
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px;\n"
"	background-color: #F6F6F6;\n"
"	padding-left: 15px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: .5px solid rgba(0, 0, 0, 1);\n"
"}")
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 282, 91, 31))
        self.label_6.setStyleSheet(u"border-color: transparent;\n"
"font-size: 18px;\n"
"font-weight: 500;")
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 365, 54, 16))
        self.label_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_7.setStyleSheet(u"QLabel{\n"
"	border-color: transparent;	\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	padding-bottom: 3px;\n"
"	border-bottom: .5px solid rgba(0, 0, 0, .3)\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	color: #D4A26F;\n"
"	border-bottom-color: #D4A26F;\n"
"}\n"
"\n"
"")
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(290, 362, 100, 19))
        self.label_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_8.setStyleSheet(u"QLabel{\n"
"	border-color: transparent;\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	color: #D4A26F;\n"
"}\n"
"")
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(142, 402, 130, 36))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	border-color: transparent;\n"
"	background-color: rgba(61, 21, 21, .75);\n"
"	color: white;\n"
"	font-weight: bold;\n"
"	padding: 5px;\n"
"	border-radius: 5px;\n"
"	font-size: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(61, 21, 21, 1);\n"
"}\n"
"\n"
"")
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(177, 446, 54, 16))
        self.label_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_9.setStyleSheet(u"QLabel{\n"
"	border-color: transparent;\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	font-size: 13px;\n"
"	font-weight: 700;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	color: rgba(61, 21, 21, .75)\n"
"}\n"
"\n"
"")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:36pt;\">D.W Coffee</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:22pt;\">SYSTEM ACCESS</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Company", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Type it your company here", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"Type it your company here", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Dialog", u"Type it your company here", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"REGISTER", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Forgot Password?", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"LOG IN", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"RETURN", None))
    # retranslateUi

