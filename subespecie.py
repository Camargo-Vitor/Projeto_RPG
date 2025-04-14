from especie import Especie
from habilidade import Habilidade


class Subespecie(Especie):
    def __init__(self, nome: str, nome_sub:str, deslocamento: float,
                altura: int, habilidades = [],
                hab_especificas = []):
        super().__init__(nome, deslocamento, altura, habilidades)
        self.__nome = nome.strip().lower() + ' ' + nome_sub.strip().lower()
        self.__hab_especificas = hab_especificas

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome_sub(self, nome: str, nome_sub: str):
        if isinstance(nome_sub, str):
            self.__nome = nome.strip().lower() + nome_sub.strip().lower

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
