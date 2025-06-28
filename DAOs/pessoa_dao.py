from model.pessoa import Pessoa
from DAOs.abstract_dao import DAO


class PessoaDao(DAO):
    def __init__(self, datasource='pessoa.pkl'):
        super().__init__(datasource)

    def add(self, pessoa: Pessoa):
        if((pessoa is not None) and isinstance(pessoa, Pessoa)):
            super().add(pessoa)

    def update(self, key, pessoa: Pessoa):
        if((pessoa is not None) and isinstance(pessoa, Pessoa)):
            super().update(key, pessoa)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)