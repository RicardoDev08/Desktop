# crie uma exceção personalizada (subclasse de Exception)
# com uma mensagem especifica.use essa exceção em um 
# contexto relevante.
# class compra:
#   valor=float(input("digite o seu valor: "))
#   if valor >= 50:
#     total=valor+valor*0.20
#   else:
#     total=valor+valor*0.10
  
# class taxa(Exception):
#   def __init__(self,valor):
#     taxa=
#     super().__init__(conta)
#     self.valor=valor
#     try:
#      valor=  
#     except:
class CompraInvalida(Exception):
    def __init__(self,mensagem):
        super().__init__(mensagem)
class Compra:
    def __init__(self, valor):
        if valor < 0:
            raise CompraInvalida("Compra não aprovada\nFavor conferir valor!")
        self.valor = valor
        self.taxa = self.calcular_taxa()
        self.total = self.valor + self.taxa

    def calcular_taxa(self):
        if self.valor >=50:
            return self.valor *0.20
        else:
            return self.valor *0.10

    def comprovante(self):
        print("\n---Comprovante de Compra---")
        print(f"Valor da compra: R$ {self.valor:.2f}")
        print(f"Valor da taxa: R$ {self.taxa:.2f}")
        print(f"Total a pagar: R$ {self.total:.2f}")
while True:
    try:
        valor = float(input("Digite o valor da sua compra: "))
        compra = Compra(valor)
        compra.comprovante() 
        break   
    except CompraInvalida as e:
        print(f"Erro: {e}")
    except ValueError:
        print("Entrada inválida.por favor, digite um número.")            

        