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
        if isinstance(ficha, Ficha) and not sum([ficha.nome == ficha_lista.nome for ficha_lista in self.__personagens]):
            self.__personagens.append(ficha)
        else:
            raise KeyError ("[ERRO] Ficha já está associada.")

    def rm_ficha(self, ficha: Ficha):
        for ficha_lista in self.__personagens:
            if ficha.nome == ficha_lista.nome:
                self.__personagens.remove(ficha_lista)
                return True
        raise KeyError("Ficha não encontrada")
