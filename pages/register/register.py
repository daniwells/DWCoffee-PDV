# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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
    QWidget)
import images

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
        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(130, 185, 441, 262))
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
        self.label_3.setGeometry(QRect(74, 4, 290, 73))
        self.label_3.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"border-color: transparent")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(38, 92, 150, 31))
        self.label_4.setStyleSheet(u"border-color: transparent;\n"
"font-size: 18px;\n"
"font-weight: 800;")
        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(43, 127, 339, 33))
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
        self.lineEdit_2.setGeometry(QRect(45, 204, 339, 33))
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
        self.label_5.setGeometry(QRect(40, 170, 50, 31))
        self.label_5.setStyleSheet(u"border-color: transparent;\n"
"font-size: 18px;\n"
"font-weight: 800;")
        self.frame_5 = QFrame(Dialog)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(130, 465, 441, 185))
        self.frame_5.setStyleSheet(u"background-color: white;\n"
"border: .5px solid rgba(0, 0, 0, .3)")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 0, 441, 79))
        self.frame_6.setStyleSheet(u"background-color: #D4A26F;\n"
"border-bottom-color: transparent;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(88, 4, 250, 73))
        self.label_6.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"border-color: transparent")
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(38, 91, 50, 31))
        self.label_7.setStyleSheet(u"border-color: transparent;\n"
"font-size: 18px;\n"
"font-weight: 800;")
        self.lineEdit_3 = QLineEdit(self.frame_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(43, 126, 340, 33))
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px;\n"
"	background-color: #F6F6F6;\n"
"	padding-left: 15px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: .5px solid rgba(0, 0, 0, 1);\n"
"}")
        self.frame_7 = QFrame(Dialog)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(580, 185, 440, 524))
        self.frame_7.setStyleSheet(u"background-color: white;\n"
"border: .5px solid rgba(0, 0, 0, .3)")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(0, 0, 441, 79))
        self.frame_8.setStyleSheet(u"background-color: #D4A26F;\n"
"border-bottom-color: transparent;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(74, 4, 290, 73))
        self.label_8.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"border-color: transparent")
        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(38, 94, 140, 31))
        self.label_9.setStyleSheet(u"border-color: transparent;\n"
"font-size: 18px;\n"
"font-weight: 800;")
        self.lineEdit_5 = QLineEdit(self.frame_7)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(47, 206, 339, 33))
        self.lineEdit_5.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px;\n"
"	background-color: #F6F6F6;\n"
"	padding-left: 15px;\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover{\n"
"	border: .5px solid rgba(0, 0, 0, 1);\n"
"}")
        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(42, 172, 96, 31))
        self.label_10.setStyleSheet(u"border-color: transparent;\n"
"font-size: 18px;\n"
"font-weight: 800;")
        self.lineEdit_6 = QLineEdit(self.frame_7)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(48, 283, 339, 33))
        self.lineEdit_6.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px;\n"
"	background-color: #F6F6F6;\n"
"	padding-left: 15px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: .5px solid rgba(0, 0, 0, 1);\n"
"}")
        self.label_11 = QLabel(self.frame_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(45, 326, 160, 31))
        self.label_11.setStyleSheet(u"border-color: transparent;\n"
"font-size: 18px;\n"
"font-weight: 800;\n"
"")
        self.label_12 = QLabel(self.frame_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(43, 248, 140, 31))
        self.label_12.setStyleSheet(u"border-color: transparent;\n"
"font-size: 18px;\n"
"font-weight: 800;")
        self.lineEdit_7 = QLineEdit(self.frame_7)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(50, 360, 339, 33))
        self.lineEdit_7.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px;\n"
"	background-color: #F6F6F6;\n"
"	padding-left: 15px;\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover{\n"
"	border: .5px solid rgba(0, 0, 0, 1);\n"
"}")
        self.comboBox = QComboBox(self.frame_7)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(50, 130, 330, 30))
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	border-radius: 5px;\n"
"	background-color: #F6F6F6;\n"
"	padding-left: 15px;\n"
"}\n"
"\n"
"\n"
"QComboBox:hover{\n"
"	border: .5px solid rgba(0, 0, 0, 1);\n"
"}")
        self.pushButton_2 = QPushButton(self.frame_7)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(137, 427, 160, 44))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	border-color: transparent;\n"
"	background-color: rgba(61, 21, 21, .75);\n"
"	/*border-color: rgba(61, 21, 21, .75);*/\n"
"	color: white;\n"
"	font-weight: bold;\n"
"	padding: 5px;\n"
"	border-radius: 5px;\n"
"	font-size: 16px;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(61, 21, 21, 1);\n"
"	/*border-right: 5px solid rgba(0,0,0, .5);*/\n"
"}\n"
"\n"
"")
        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(52, 396, 44, 25))
        self.label_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_13.setStyleSheet(u"QLabel{\n"
"	border-color: transparent;\n"
"	font-size: 14px;\n"
"	font-weight: 500;\n"
"	font-weight:  100;\n"
"	border-bottom-color: rgba(0,0,0,.75);  \n"
"}\n"
"\n"
"QLabel:hover{\n"
"	color: rgba(61, 21, 21, .75);\n"
"	border-bottom-color: rgba(61, 21, 21, .75);  \n"
"}\n"
"")
        self.label_14 = QLabel(self.frame_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(183, 472, 64, 31))
        self.label_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_14.setStyleSheet(u"QLabel{\n"
"	border-color: transparent;\n"
"	font-size: 14px;\n"
"	font-weight: 800;\n"
"}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	color: rgba(61, 21, 21, .75);\n"
"}")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(186, 669, 321, 40))
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

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:36pt;\">D.W Coffee</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:22pt;\">REGISTER COMPANY</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Name Company", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Type it your company here", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"Type it your company here", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"cnpj", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:22pt;\">LOGIN COMPANY</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"cnpj", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Dialog", u"Type it your company here", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:22pt;\">REGISTER USER</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Type User", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("Dialog", u"Type it your username here", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("Dialog", u"Type it your password here", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Confirm Password", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("Dialog", u"Confirm your password here", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Administrador", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Usuario", None))

        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"REGISTER", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"LOGIN", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"RETURN", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"CONFIRM", None))
    # retranslateUi

