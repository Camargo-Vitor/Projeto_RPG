from classe import Classe
from habilidade import Habilidade

class Subclasse(Classe):
    def __init__(self, nome: str, nome_sub: str, dado_vida: int, hab_especificas: list = []):
        super().__init__(nome, dado_vida)
        self.__nome = nome.strip().lower() + ' ' + nome_sub.strip().lower()
        self.__hab_espeficicas = hab_especificas

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome_sub(self, nome: str, nome_sub: str):
        if isinstance(nome_sub, str):
            self.__nome = nome.strip().lower() + nome_sub.strip().lower

    def add_hab(self, habilidade: Habilidade):
        if isinstance(habilidade, Habilidade) and habilidade.origem == 'subclasse':
            self.__habilidades.append(habilidade)
            
    @property
    def hab_especificas(self):
        return self.__hab_espeficicas
