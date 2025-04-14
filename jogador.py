from pessoa import Pessoa
from ficha import Ficha


class Jogador(Pessoa):
    def __init__(self, nome: str, telefone: int, endereco: str, disponibilidade: list):
        super().__init__(nome, telefone, endereco, disponibilidade)
        self.__personagens = []

    @property
    def personagens(self):
        return self.__personagens
    
    def add_ficha(self, ficha: Ficha):
        if isinstance(ficha, Ficha):
            self.__personagens.append(ficha)

    def rm_ficha(self, ficha: Ficha):
            if ficha in self.__personagens:
                 self.__personagens.remove(ficha)
    
    def __str__(self):
        return super().__str__() + '\npersonagens do jogador: ' + str([per.nome for per in self.__personagens])

         
        