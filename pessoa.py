from abc import ABC, abstractclassmethod

class Pessoa(ABC):
    @abstractclassmethod
    def __init__(self, nome: str, telefone: int,  endereco: str, disponibilidade: list):
        self.__nome = nome.strip().lower()
        self.__endereco = endereco.strip().lower()
        self.__telefone = telefone
        self.__disponibilidade = disponibilidade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property 
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def disponibilidade(self):
        return self.__disponibilidade
    
    def __str__(self):
        return f'nome: {self.nome} \
        \ntelefone: {self.telefone} \
        \nendereco: {self.endereco} \
        \ndias disponíveis: {self.disponibilidade}'
