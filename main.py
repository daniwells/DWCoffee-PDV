from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem,QStackedWidget)
from pages.initial import initial
from pages.login import login
from pages.register import register
from pages.order import orderPage
import sys
from database import Database
import time

class Order(QMainWindow, orderPage.Ui_Dialog):
    def __init__(self):
        super(Order, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Order Page")
        self.pushButton_10.clicked.connect(self.openMenu)
        self.addComboBoxCoffee()

        #Buttons Coffee --------------------------------------------------------

        

    def openMenu(self):
        start_geometry = self.frame_22.geometry()
        
        if start_geometry.getRect() == (0, 141, 111, 641):
            end_geometry = start_geometry.translated(-120, 0)
        else:
            end_geometry = start_geometry.translated(120, 0)

        self.animation = QtCore.QPropertyAnimation(self.frame_22, b"geometry")
        self.animation.setDuration(500)
        self.animation.setStartValue(start_geometry)
        self.animation.setEndValue(end_geometry)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

        self.moveBottomMenu()

    def moveBottomMenu(self):
        start_geometry = self.pushButton_10.geometry()
        
        if start_geometry.getRect() == (110, 140, 16, 641):
            end_geometry = start_geometry.translated(-112, 0)
        else:
            end_geometry = start_geometry.translated(112, 0)

        self.animation2 = QtCore.QPropertyAnimation(self.pushButton_10, b"geometry")
        self.animation2.setDuration(500)
        self.animation2.setStartValue(start_geometry)
        self.animation2.setEndValue(end_geometry)
        self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation2.start()

    def addComboBoxCoffee(self):
        db = Database()
        db.connect()

        listCoffee = db.select_all_coffee()

        for item in listCoffee:
            name_coffe = item[1]
            self.comboBox.addItem(name_coffe)

    def addToKart(self, name, price):
        item = f"{name}     {price}"

        self.listWidget.addItem(item)
    
        

class Login(QMainWindow, login.Ui_Dialog):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login")
        self.pushButton.clicked.connect(self.login_finish)

    def login_finish(self):
        order = Order()
        widget.addWidget(order)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Register(QMainWindow, register.Ui_Dialog):
    def __init__(self):
        super(Register, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Register")
        self.pushButton_2.clicked.connect(self.register_finish)  

    def register_finish(self):
        order = Order()
        self.register_user()
        widget.addWidget(order)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def register_user(self):
        db = Database()
        db.connect()

        
        type_user = 'comum_user'
        if self.lineEdit_5.text() == "admim" and self.lineEdit_6.text() == "admin":
            type_user = "admin"

        fullDataSet = (
            self.lineEdit_5.text(), self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_6.text(), type_user
        )

        response = db.register_user(fullDataSet)

        if response == "DEU BOM!!":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro Realizado")
            msg.setText("Cadastro Realizado com sucesso")
            msg.exec()
            db.close_connection()
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText("Erro ao cadastrar, verifique se as informações foram preenchidadas corretamente!")
            msg.exec()
            db.close_connection()
            return


class MainWindow(QMainWindow, initial.Ui_Dialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("DWCoffee - PDV")
    
        self.pushButton.clicked.connect(self.gotologin)  
        self.pushButton_2.clicked.connect(self.register)

    def gotologin(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def register(self):
        register = Register()
        widget.addWidget(register)
        widget.setCurrentIndex(widget.currentIndex()+1)


#############################  CRUD FUNCTIONS  #############################

if __name__ == "__main__":
    db = Database()
    db.connect()
    db.create_table_users()
    db.close_connection()

    app = QApplication(sys.argv)
    window = MainWindow()

    widget = QStackedWidget()
    widget.addWidget(window)
    widget.setFixedHeight(768)
    widget.setFixedWidth(1160)
    widget.show()

    window.show()
    app.exec()



 
 
