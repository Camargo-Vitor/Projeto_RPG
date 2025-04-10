from especie import Especie

class Subespecie(Especie):
    def __init__(self, nome: str, deslocamento: float, altura: int, habilidades: str, especificacao: str, hab_especifica: list):
        super().__init__(nome, deslocamento, altura, habilidades)
        self.__especificao = especificacao

@property
def especificao(self):
    return self.__especificao

@especificao.setter
def especificao(self, especificao):
    self.__especificao = especificao


@property
def hab_especifica(self):
    return self.__hab_especifica

@hab_especifica.setter
def hab_especifica(self, hab_especifica):
    self.__hab_especifica = hab_especifica


