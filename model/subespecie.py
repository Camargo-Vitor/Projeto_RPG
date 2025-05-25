from model.especie import Especie
from model.habilidade import Habilidade


class Subespecie(Especie):
    def __init__(self,
                 nome: str,
                 nome_sub: str,
                 deslocamento: float,
                 altura: int,
                 habilidades: list[Habilidade]):
        super().__init__(nome, deslocamento, altura, habilidades)
        self.__nome_sub = nome_sub
        self.__habilidades = habilidades
        self.__hab_especificas: list[Habilidade] = []

    @property
    def nome(self):
        return f'{super().nome} {self.__nome_sub}'
    
    @property
    def nome_sub(self):
        return self.__nome_sub

    @property
    def habilidades(self):
        return self.__habilidades

    @nome_sub.setter
    def nome_sub(self, nome_sub: str):
        if isinstance(nome_sub, str):
            self.__nome_sub = nome_sub

    @property
    def hab_especificas(self):
        return self.__hab_especificas
    
    def add_hab_sub(self, habilidade: Habilidade):
        if isinstance(habilidade, Habilidade) and habilidade.origem == 'subespecie':
            self.__hab_especificas.append(habilidade)

    def rm_hab_sub(self, habilidade: Habilidade):
        if habilidade in self.hab_especificas:
            self.hab_especificas.remove(habilidade)
        else:
            return('Habilidade não encontrada')
