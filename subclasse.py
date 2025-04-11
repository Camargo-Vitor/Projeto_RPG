from classe import Classe

class Subclasse(Classe):
    def __init__(self, nome: str, nome_sub: str, hab_especifica: list, nivel=1):
        super().__init__(nome, nivel)
        self.__nome_sub = nome_sub.strip().lower()
        self.__hab_espeficica = hab_especifica


    @property
    def nome_sub(self):
        return self.__nome_sub

    @nome_sub.setter
    def nome_sub(self,nome_sub):
        if isinstance(nome_sub, int):
            self.__nome_sub = nome_sub.strip().lower()


    @property
    def hab_especifica(self):
        return self.__hab_espeficica



    
