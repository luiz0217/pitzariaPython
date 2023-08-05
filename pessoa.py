from abc import ABC,abstractmethod

class pessoa(ABC):
    def __init__(self,nome,numero):
        self._nome =  nome
        self._numero = numero
    
    @property
    def nome(self):
        return  self._nome
    
    @nome.setter
    def nome(self,nome):
        self._nome = nome

    @property
    def numero(self):
        return  self._numero
    
    @numero.setter
    def numero(self,numero):
        self._numero = numero
    
    @abstractmethod
    def cadastro(self):
        pass