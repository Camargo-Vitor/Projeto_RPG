from model.endereco import Endereco
from abc import ABC, abstractmethod


class Pessoa(ABC):
    @abstractmethod
    def __init__(self,
                 nome: str,
                 telefone: int,
                 cidade: str,
                 bairro: str,
                 numero: int,
                 cep: int):
        self.__nome = nome
        self.__endereco = Endereco(cidade, bairro, numero, cep)
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @property
    def telefone(self):
        return self.__telefone

    @property 
    def endereco(self):
        return self.__endereco

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise ValueError("[ERRO] Nome não alterado, valor inválido")

    @telefone.setter
    def telefone(self, telefone: int):
        if isinstance(telefone, int):
            self.__telefone = telefone
        else:
            raise ValueError("[ERRO] Telefone não alterado, valor inválido")

    @endereco.setter
    def endereco(self,
                 cidade: str, 
                 bairro: str,
                 numero: int,
                 cep: int):
        try:
            self.__endereco = Endereco(cidade, bairro, numero, cep)
        except:
            raise ValueError("[ERRO] Endereço não alterado, valor inválido")
