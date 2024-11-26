import sqlite3 

class database:
    def __init__(self, de_name) :
        self.db_name = de_name
        self.conn = None
        self.cursor = None
    def connector(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def commit(self):
        if self.conn:
            self.conn.commit()

    def executar(self, query,parametros = None):
        if parametros:
            self.cursor.execute(query, parametros)
        else:
            self.cursor.execute(query)    

    def fetchAll(self):
        query = "SELECT * FROM usuario"
        self.db.executar(query)
# db = database('teste.db')
# db.connector()            