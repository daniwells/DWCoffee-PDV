from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem)
from pages.initial import initial
from pages.login import login
from pages.register import register
from pages.order import orderPage
import sys
from database import Database

class Order(QMainWindow, orderPage.Ui_Dialog):
    def __init__(self):
        super(Order, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Order Page")

class Login(QMainWindow, login.Ui_Dialog):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login")
        self.pushButton.clicked.connect(self.login_finish)

    def login_finish(self):
        self.close()        
        order.show()

class Register(QMainWindow, register.Ui_Dialog):
    def __init__(self):
        super(Register, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Register")
        self.pushButton_2.clicked.connect(self.register_finish)  

    def register_finish(self):
        self.register_user()
        self.close()        
        order.show()


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
        #appIcon = QIcon(u"icons/logo4.png")
        appIcon = QIcon(u"") #ainda nao selecionamos o item
        self.setWindowIcon(appIcon) # colocar icon na janela  
        #Botão Inicial para abrir o menu.
        self.pushButton.clicked.connect(self.login)  
        self.pushButton_2.clicked.connect(self.register)

    def login(self):
        self.close()        
        login.show()

    def register(self):
        self.close()        
        register.show()


#############################  CRUD FUNCTIONS  #############################

if __name__ == "__main__":
    db = Database()
    db.connect()
    db.create_table_users()
    db.close_connection()

    app = QApplication(sys.argv)
    window = MainWindow()
    login = Login()
    register = Register()
    order = Order()

    window.show()
    app.exec()



 
 
