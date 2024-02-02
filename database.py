import sqlite3

class Database:
    def __init__(self, name = "system.db"):
        self.name = name
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

    def create_table_users(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS users(
                id_user INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                fullname varchar(255) NOT NULL,
                name_company varchar(255) NOT NULL,
                cnpj int(14) NOT NULL,
                email varchar(100),
                password varchar(40) NOT NULL,
                phone int(14),
                type_user varchar(40) NOT NULL
            );"""
        )

    def create_table_coffee(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS coffee(
                id_coffee INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name_coffee varchar(255) NOT NULL,
                price FLOAT NOT NULL,
                litters FLOAT NOT NULL
            );"""
        )
        
    def register_user(self, fullDataSet):
        buys_table = ('fullname','name_company','cnpj','password','type_user')
        qntd = ("?, ?, ?, ?, ?")

        try:
            self.cursor.execute(
            f"""
                INSERT INTO users (fullname, name_company, cnpj,password, type_user) VALUES (?,?,?,?,?)  
            """, fullDataSet)
            self.connection.commit()
            return "DEU BOM!!"
        except: 
            return "DEU RUIM!!"
        
    def register_coffee(self, fullDataSet):
        # try:
        self.cursor.execute(
        f"""
            INSERT INTO coffee (name_coffee, price, litters) VALUES (?,?,?)  
        """, fullDataSet)
        self.connection.commit()
            # return "DEU BOM!!"
        # except: 
            # return "DEU RUIM!!"

    def select_all_coffee(self):
        try:
            self.cursor.execute("SELECT * FROM coffee ORDER BY name_coffee")
            coffee = self.cursor.fetchall() 
            return coffee
        except:
            pass


    # def select_all_livros(self):
    #     try:
    #         cursor = self.connection.cursor()
    #         cursor.execute("SELECT * FROM livros ORDER BY TITULO")
    #         livros = cursor.fetchall() # traz todos os dados que encontrar de livros
    #         return livros
    #     except:
    #       pass

    # def buscar_livros(self):
    #     db = Data_base()
    #     db.connect()
    #     result = db.select_all_livros()
       
    #     self.tabLivros.clearContents() #limpar todos os dados e recriar toda vez q chamo essa função
    #     self.tabLivros.setRowCount(len(result)) # Mostra o tamanho do meu registro(linhas q vai ter)...
    #                                              #se tiver 10 linhas ele mostra as 10.
 
    #     for row, text in enumerate(result):
    #         for column, data in enumerate(text):
    #             self.tabLivros.setItem(row, column, QTableWidgetItem(str(data)))
 
    #     db.close_connection()

if __name__ == "__main__":
    db = Database()
    db.connect()
    #db.create_table_coffee()

    name_coffee = input("Enter the coffee name: ")
    price = float(input("Enter the price of the coffee: "))
    litters = float(input("Enter the litters of the coffee: "))

    fulldataset = (
        name_coffee, price, litters
    )

    db.register_coffee(fulldataset)
    # print(response)