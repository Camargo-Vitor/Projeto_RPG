from especie import Especie
from habilidade import Habilidade

class Subespecie(Especie):
    def __init__(self, nome: str, nome_sub:str, deslocamento: float,\
                altura: int, especificacao: str, habilidades: list = [] ,\
                hab_especificas: list = []):
        super().__init__(nome, deslocamento, altura, habilidades)
        self.nome = nome + ' ' + nome_sub
        self.__especificao = especificacao.strip().lower()
        self.__hab_especificas = hab_especificas

    @property
    def especificao(self):
        return self.__especificao

    @especificao.setter
    def especificao(self, especificao: str):
        if isinstance(self.especificao, str):
            self.__especificao = especificao.strip().lower()

    @property
    def hab_especificas(self):
        return self.__hab_especificas
    
    def add_hab(self, habilidade: Habilidade):
        if isinstance(habilidade, Habilidade) and habilidade.origem == 'subespecie':
            self.__hab_especificas.append(habilidade)

    def rm_hab_esp(self, habilidade: Habilidade):
        if habilidade in self.hab_especificas:
            self.hab_especificas.remove(habilidade)
        else:
            return('Habilidade não encontrada')
