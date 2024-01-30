import sqlite3

class Database:
    def __init__(self, name = "system.db"):
        self.name = name
        self.connection = None
        self.cursor = self.connection.cursor()

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

    def create_table_coffee(self):
        self.cursor.execute(
        """CREATE TABLE IF NOT EXISTS users (
            id_coffee int PRIMARY KEY AUTOINCREMENT NOT NULL,
            name_user varchar(40) UNIQUE NOT NULL,
            name_company varchar(40),
            cnpj int(11),
            password varchar(30),
            type_user varchar(15),
            price FLOAT; 
        )""")

    def register_coffee(self, fullDataSet):
        buys_table = ('name','price')
        qntd = ("?, ?")

        try:
            self.cursor.execute(
            f"""
                INSERT INTO Coffee {buys_table} VALUES ({qntd})  
            """, fullDataSet)

            return "DEU BOM!!"
        except: 
            return "DEU RUIM!!"

