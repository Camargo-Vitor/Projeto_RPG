from model.pessoa import Pessoa


class Mestre(Pessoa):
    def __init__(self, nome: str, telefone: int, endereco: str, disponibilidade: list):
        super().__init__(nome, telefone, endereco, disponibilidade)
