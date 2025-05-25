from model.pessoa import Pessoa
from model.ficha import Ficha


class Jogador(Pessoa):
    def __init__(self,
                 nome: str,
                 telefone: int,
                 cidade: str,
                 bairro: str,
                 numero: int,
                 cep: int,):
        super().__init__(nome, telefone, cidade, bairro, numero, cep)
        self.__personagens: list[Ficha] = []

    @property
    def personagens(self):
        return self.__personagens
    
    def add_ficha(self, ficha: Ficha):
        if isinstance(ficha, Ficha):
            self.__personagens.append(ficha)
        else:
            raise ValueError("[ERRO] Ficha não adicionada, valor inválido")

    def rm_ficha(self, ficha: Ficha):
        if ficha in self.__personagens:
            self.__personagens.remove(ficha)
        else:
            raise KeyError("[ERRO] Ficha não encontrada")
