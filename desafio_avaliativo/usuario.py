from Db import database
class usuario:
    def __init__(self, db_name): 
        self.db = database(db_name)
        self.db.connector()
    ### CREATE

    def criarusuario(self, nome, email):
        query = "INSERT INTO usuario(nome,email) VALUES (?,?)"
        self.db.executar(query,(nome,email))
        self.db.commit()
    ### README

    def listarusuario(self):
        query = "SELECT * FROM USUARIO"
        self.db.executar(query)
        dados = self.db.fetchAll()
        return dados

    ### UPDATE

    def atualizarusuario(self,id,novoNome,novoEmail):
        query = 'UPDATE usuario SET nome = ?, email = ? WHERE id = ?'
        self.db.executar(query,(novoNome, novoEmail, id))
        self.db.commit()
        
usuario2 = usuario('bancodados.db')
# usuario = ('Ricardo','ricardo@gmail.com')           
lista = usuario2.listarusuario()
print(lista)