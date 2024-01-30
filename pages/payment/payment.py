# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'payment.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import imagens_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1171, 768)
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
        self.frame_3.setGeometry(QRect(100, 200, 301, 311))
        self.frame_3.setStyleSheet(u"background-color: #FFFFFF;\n"
"border: .5px solid black")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 0, 301, 50))
        self.frame_6.setStyleSheet(u"border: transparent;\n"
"background-color: transparent;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(0, 241, 301, 70))
        self.frame_8.setStyleSheet(u"border: transparent;\n"
"background-color: transparent;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 8, 131, 51))
        self.label_3.setStyleSheet(u"")
        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(90, 40, 131, 51))
        self.label_10.setStyleSheet(u"")
        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(0, 49, 301, 204))
        self.frame_7.setStyleSheet(u"border: transparent;\n"
"background-color: transparent;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.frame_7)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 20, 231, 31))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	border: .5px solid rgba(0, 0, 0, .5);\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"	padding: 7px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border-color: rgba(0, 0, 0, 1);\n"
"}")
        self.lineEdit_2 = QLineEdit(self.frame_7)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(30, 113, 231, 31))
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"	border: .5px solid rgba(0, 0, 0, .5);\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"	padding: 7px;\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover{\n"
"	border-color:  rgba(0, 0, 0, 1);\n"
"}")
        self.lineEdit_3 = QLineEdit(self.frame_7)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(30, 160, 231, 31))
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"	border: .5px solid rgba(0, 0, 0, .5);\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"	padding: 7px;\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover{\n"
"	border-color:  rgba(0, 0, 0, 1);\n"
"}")
        self.comboBox = QComboBox(self.frame_7)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(30, 66, 121, 31))
        self.comboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	border: .5px solid rgba(0, 0, 0, .5);\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"	padding: 7px\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"	border-color: rgba(0, 0, 0, 1);\n"
"}")
        self.checkBox = QCheckBox(self.frame_7)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(180, 74, 70, 17))
        self.checkBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBox.setStyleSheet(u"font-size: 12px;")
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 260, 131, 31))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: #D4A26F;\n"
"	border: transparent;\n"
"	color: white;\n"
"	font-weight: bold;	\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(61, 21, 21, .75);\n"
"}\n"
"\n"
"")
        self.frame_4 = QFrame(Dialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(440, 200, 301, 214))
        self.frame_4.setStyleSheet(u"background-color: white;\n"
"border: .5px solid black")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(1, 50, 299, 163))
        self.frame_9.setStyleSheet(u"border-color: transparent;\n"
"background-color: #FFFFFF;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.pushButton_2 = QPushButton(self.frame_9)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(100, 19, 171, 31))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	border: .5px solid rgba(0, 0, 0, .5);\n"
"	background-color: #F1F1F1;\n"
"	border-radius: 5px;\n"
"	padding: 7px;\n"
"	font-size: 13px;\n"
"	font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(0, 0, 0, .5);\n"
"	color: white;\n"
"}\n"
"\n"
"")
        self.pushButton_5 = QPushButton(self.frame_9)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(156, 110, 51, 31))
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"	background-color: #4BB8A9;\n"
"	image: url(:/imagens/transferir (2) 1.png);\n"
"	border-radius: 5px;\n"
"	padding: 7px;\n"
"	border: .5px solid rgba(0, 0, 0, .5);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(75, 184, 169, .7);\n"
"}\n"
"\n"
"")
        self.label_7 = QLabel(self.frame_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(53, 67, 41, 21))
        self.label_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_7.setStyleSheet(u"border-color: transparent;\n"
"image: url(:/imagens/icone-do-cartao-de-pagamento_419328-1911 2 (1).png);\n"
"")
        self.pushButton_4 = QPushButton(self.frame_9)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(87, 110, 51, 31))
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	background-color: #D4A26F;\n"
"	image: url(:/imagens/transferir (1) (1) 1.png);\n"
"	border-radius: 5px;\n"
"	padding: 7px;\n"
"	border: transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(212, 162, 111, .7);\n"
"}\n"
"\n"
"\n"
"")
        self.label_4 = QLabel(self.frame_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 19, 70, 31))
        self.label_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_4.setStyleSheet(u"border: .5px solid rgba(0, 0, 0, .5);\n"
"background-color: #F1F1F1;\n"
"padding: 7px;\n"
"font-size: 13px;\n"
"font-weight: 500;\n"
"")
        self.label_5 = QLabel(self.frame_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(53, 25, 41, 21))
        self.label_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_5.setStyleSheet(u"image: url(:/imagens/icone-do-cartao-de-credito_910989-1537 2.png);\n"
"border-color: transparent;\n"
"background-color: transparent;")
        self.pushButton_3 = QPushButton(self.frame_9)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(100, 61, 171, 31))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	border: .5px solid rgba(0, 0, 0, .5);\n"
"	background-color: #F1F1F1;\n"
"	border-radius: 5px;\n"
"	padding: 7px;\n"
"	font-size: 13px;\n"
"	font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(0, 0, 0, .5);\n"
"	color: white;\n"
"}")
        self.label_6 = QLabel(self.frame_9)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 61, 70, 31))
        self.label_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_6.setStyleSheet(u"border: .5px solid rgba(0, 0, 0, .5);\n"
"background-color: #F1F1F1;\n"
"\n"
"padding: 7px;\n"
"font-size: 13px;\n"
"font-weight: 500;\n"
"")
        self.pushButton_2.raise_()
        self.pushButton_5.raise_()
        self.pushButton_4.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.pushButton_3.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.frame_10 = QFrame(self.frame_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(1, 1, 299, 49))
        self.frame_10.setStyleSheet(u"background-color: #FFFFFF;\n"
"border-color: transparent;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.frame_10)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(36, 10, 137, 51))
        self.label_8.setStyleSheet(u"")
        self.frame_5 = QFrame(Dialog)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(780, 200, 291, 251))
        self.frame_5.setStyleSheet(u"background-color: #FFFFFF;\n"
"border: .5px solid black")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_11 = QFrame(self.frame_5)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(0, 0, 292, 51))
        self.frame_11.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.frame_11)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(36, 10, 137, 51))
        self.label_9.setStyleSheet(u"")
        self.frame_12 = QFrame(self.frame_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(0, 50, 292, 65))
        self.frame_12.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(0, 70, 292, 130))
        self.frame_13.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.pushButton_6 = QPushButton(self.frame_12)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(41, 18, 205, 31))
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"	border: .5px solid rgba(0, 0, 0, .5);\n"
"	background-color: rgba(61, 21, 21, .75);\n"
"	border-radius: 5px;\n"
"	padding: 7px;\n"
"	font-size: 13px;\n"
"	font-weight: bold;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(61, 21, 21, .95);\n"
"}\n"
"\n"
"")
        self.frame_14 = QFrame(self.frame_5)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(44, 130, 203, 100))
        self.frame_14.setStyleSheet(u"border-right-color: transparent;\n"
"border-left-color: transparent;\n"
"border-top-color:  rgba(0, 0, 0, .5);\n"
"border-bottom-color:  rgba(0, 0, 0, .5);\n"
"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.label_11 = QLabel(self.frame_14)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 26, 77, 51))
        self.label_11.setStyleSheet(u"border-color: transparent;\n"
"font-weight: bold;")
        self.frame_16 = QFrame(Dialog)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(0, 669, 1171, 101))
        self.frame_16.setStyleSheet(u"background-color: rgba(0, 0, 0, .11);")
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
        self.pushButton_9.setGeometry(QRect(-1, 140, 25, 631))
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"	image: url(:/imagens/Arrow 1.png);\n"
"	background-color: rgba(0, 0, 0, .1);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(0, 0, 0, .2);\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:36pt;\">D.W Coffee</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt;\">Personal Datas</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt;\">Personal Datas</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.frame_7.setWhatsThis(QCoreApplication.translate("Dialog", u"<html>\n"
" <head>\n"
"</head>\n"
"<body>\n"
"   <p>OPAAAAAAAAAA</p>\n"
"</body>\n"
"</html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Client Name", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"Client Email", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Dialog", u"Client Cellphone", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"table1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"table2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"table3", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"table4", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"table5", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Dialog", u"table6", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Dialog", u"table7", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Dialog", u"table8", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("Dialog", u"table9", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("Dialog", u"table10", None))

        self.checkBox.setText(QCoreApplication.translate("Dialog", u"To Carry", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"ADD ORDER", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Credit", None))
        self.pushButton_5.setText("")
        self.label_7.setText("")
        self.pushButton_4.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Debit", None))
        self.label_6.setText("")
        self.label_8.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt;\">Payment Forms</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt;\">Payment Forms</span></p></body></html>", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"Credit", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt;\">TOTAL:</span></p></body></html>", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"New Order", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"Payment", None))
        self.pushButton_9.setText("")
    # retranslateUi

