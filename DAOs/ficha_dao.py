from model.ficha import Ficha
from DAOs.abstract_dao import DAO


class FichaDao(DAO):
    def __init__(self, datasource='ficha.pkl'):
        super().__init__(datasource)

    def add(self, ficha: Ficha):
        if((ficha is not None) and isinstance(ficha, Ficha)):
            super().add(ficha)

    def update(self, key, ficha: Ficha):
        if((ficha is not None) and isinstance(ficha, Ficha)):
            super().update(key, ficha)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)
