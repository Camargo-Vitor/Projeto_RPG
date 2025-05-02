from model.habilidade import Habilidade


class Classe:
    def __init__(self, nome: str, dado_vida: int):
        self.__nome = nome.strip().lower()
        self.__dado_vida = dado_vida
        self.__habilidades = []

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

    def add_hab(self, habilidade: Habilidade):
        if isinstance(habilidade, Habilidade) and habilidade.origem == 'classe':
            self.__habilidades.append(habilidade)

    def rm_hab(self, habilidade: Habilidade):
        if habilidade in self.habilidades:
            self.habilidades.remove(habilidade)
        else:
            return('Habilidade não encontrada')
