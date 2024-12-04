class Livros():
    def __init__(self, titulo, autor, genero, cod_livro):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.cod_livro = cod_livro

        self.status = "Disponivel"
        self.usuario = None

    def create(self):
        return f'insert into livro(titulo, autor, genero, status, codigo) values("{self.titulo}", "{self.autor}", "{self.genero}", "{self.status}", {self.cod_livro});'

    # def read(self):
    #     return f'select * from livro where codigo = {self.cod_livro};'
    
    # def delete(self):
    #     return f'delete from livro where titulo= "Dom Casmurgo";'
  
    
    # def update(self):
    #     return f'update livro set autor = "Ricardo" where autor= Machado de Assis;'


Livros.__name__*"Livros"



    
