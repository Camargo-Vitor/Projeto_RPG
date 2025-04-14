from classe import Classe

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

    @property
    def hab_especificas(self):
        return self.__hab_espeficicas
