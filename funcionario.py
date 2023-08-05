from pessoa import pessoa

class funcionario(pessoa):
    def __init__(self,nome,numero):
        super().__init__(nome, numero)
       
    def cadastro(self):
      self._nome = input("LOGIN: ")
      self._numero = int(input("SENHA: "))