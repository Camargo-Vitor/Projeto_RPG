from model.habilidade import Habilidade
from DAOs.abstract_dao import DAO


class HabilidadeDao(DAO):
    def __init__(self, data_source='habilidade.pkl'):
        super().__init__(data_source)

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
