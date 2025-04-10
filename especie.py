from abc import ABC, abstractclassmethod
 
class Especie(ABC):
    abstractclassmethod
    def __init__(self, nome: str, deslocamento: float, \
                  altura: int, habilidades: list):
        self.__nome = nome.strip().lower()
        self.__deslocamento = deslocamento
        self.__altura = altura
        self.__habilidades = []


    @property
    def nome(self):     
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome.strip().lower()

    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, altura):
        if isinstance(altura, int):
            self.__altura = altura
        
    @property
    def deslocamento(self):
        return self.__deslocamento 

    @deslocamento.setter
    def deslocamento(self, deslocamento):
        if isinstance(deslocamento, float):
            self.__deslocamento = deslocamento


    @property
    def habilidades(self):
        return self.__habilidades
    


        
