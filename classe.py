class Classe:
    def __init__(self, nome: str, dado_vida: int, nivel = 1):
        self.__nome = nome.strip().lower()
        self.__dado_vida = dado_vida
        self.__habilidades = dict()
        self.__nivel = nivel

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome= nome.strip().lower()

    @property
    def dado_vida(self):
        return self.__dado_vida

    @dado_vida.setter
    def dado_vida(self, dado: int):
        self.__dado_vida = dado

    @property
    def habilidades(self):
        return self.__habilidades

    def add_hab(self, nome: str, nivel_necessario: int):
        self.__habilidades[nome] = nivel_necessario    

