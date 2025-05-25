from model.pessoa import Pessoa


class Mestre(Pessoa):
    def __init__(self,
                 nome: str,
                 telefone: int,
                 cidade: str,
                 bairro: str,
                 numero: int,
                 cep: int):
        super().__init__(nome, telefone, cidade, bairro, numero, cep)
