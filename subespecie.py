from especie import Especie

class Subespecie(Especie):
    def __init__(self, nome: str, deslocamento: float, altura: int, habilidades: str, especificacao: str, hab_especifica: list):
        super().__init__(nome, deslocamento, altura, habilidades)
        self.__especificao = especificacao.strip().lower()
        self.__hab_especifica = []

    @property
    def especificao(self):
        return self.__especificao

    @especificao.setter
    def especificao(self, especificao):
        self.__especificao = especificao.strip().lower()


    @property
    def hab_especifica(self):
        return self.__hab_especifica




