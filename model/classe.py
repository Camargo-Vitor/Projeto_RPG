from model.habilidade import Habilidade
from model.subclasse import Subclasse


class Classe():
    def __init__(self, nome: str, dado_vida: int, nome_sub: str, habilidades = [], hab_especificas = []):
         self.__nome = nome
         self.__dado_vida = dado_vida
         self.__habilidades = habilidades
         self.__subclasses: list[Subclasse] = [Subclasse(nome_sub, hab_especificas)]
                 
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
    def subclasse(self):
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
            self.habilidades.remove(habilidade)
        else:
            raise KeyError("[ERRO] Habilidade não encontrada")
