import mysql.connector
from mysql.connector import Error
class Database: 
    def __init__(self, host, user, password, database):
        self.host = host 
        self.user = user 
        self.password = password 
        self.database = database 

    def conectar(self):
        self.conexao = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database

        )
        self.cursor = self.conexao.cursor()

    def desconectar(self):
        self.conexao.close()
        