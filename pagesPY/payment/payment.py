from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtCore import QResource
import sys

import imagens

def openMenu():
    menu = payment.frame_15
    menu.setVisible(not menu.isVisible())

    payment.pushButton_10.setVisible(menu.isVisible())
    payment.pushButton_9.setVisible(not menu.isVisible())

app = QApplication([])
payment = uic.loadUi("C:/Users/danie/OneDrive/Área de Trabalho/PyQT/DWCoffee/pagesPY/payment.ui")

payment.pushButton_10.clicked.connect(openMenu)
payment.pushButton_9.clicked.connect(openMenu)    

payment.show()
payment.exec()
