from model.habilidade import Habilidade
from model.subclasse import Subclasse


class Classe():
    def __init__(self, nome: str, dado_vida: int, nomes_sub: list[str], habilidades = []):
        self.__nome: str = nome
        self.__dado_vida: int = dado_vida
        self.__habilidades: list[Habilidade] = habilidades
        self.__subclasses: list[Subclasse] = []
        for a in range(3):
            self.__subclasses.append(Subclasse(nomes_sub[a]))
                 
    @property
    def nome(self):
        return self.__nome

    @property
    def dado_vida(self):
        return self.__dado_vida

    @property
    def habilidades(self):
        return self.__habilidades
    
    @property
    def subclasses(self):
        return self.__subclasses

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome= nome.strip().lower()
        else:
            raise ValueError("[ERRO] Nome não alterado, valor inválido")

    @dado_vida.setter
    def dado_vida(self, dado: int):
        if isinstance(dado, int):
            self.__dado_vida = dado
        else:
            raise ValueError("[ERRO] Dado de vida não alterado, valor inválido")

    def add_hab(self, habilidade: Habilidade):
        if isinstance(habilidade, Habilidade) and habilidade.origem == 'classe':
            self.__habilidades.append(habilidade)
        else:
            raise ValueError("[ERRO] Habilidade não adicionada, valor inválido")

    def rm_hab(self, habilidade: Habilidade):
        if habilidade in self.habilidades:
            self.__habilidades.remove(habilidade)
        else:
            raise KeyError("[ERRO] Habilidade não encontrada")
