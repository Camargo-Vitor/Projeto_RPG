from model.habilidade import Habilidade
from DAOs.abstract_dao import DAO


class HabilidadeDao(DAO):
    def __init__(self, datasource='habilidade.pkl'):
        super().__init__(datasource)

    def add(self, habilidade: Habilidade):
        if((habilidade is not None) and isinstance(habilidade, Habilidade)):
            super().add(habilidade)

    def update(self, key, habilidade: Habilidade):
        if((habilidade is not None) and isinstance(habilidade, Habilidade)):
            super().update(key, habilidade)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)
