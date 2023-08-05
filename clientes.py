from pessoa import pessoa
class clientes:
    def __init__ (self,nome,numero,endereco,formaPagamento):
        
        self._endereco = endereco        
        self._formaPagamento = formaPagamento

    
    
    @property
    def endereco(self):
        return  self._endereco
    
    @endereco.setter
    def endereco(self,endereco):
        self._endereco = endereco   
    

    @property
    def formaPagamento(self):
        return  self._formaPagamento
    
    @formaPagamento.setter
    def formaPagamento(self,formaPagamento):
        self._formaPagamento = formaPagamento

    def cadastro(self):          
        self._nome = input("nome do cliente: ")
        self._endereco = input("endereço do cliente")
        self._numero = int(input("numero do cliente: "))
        self._formaPagamento = input("forma de pagamento: ")
         