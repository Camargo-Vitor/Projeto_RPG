from model.magia import Magia
from DAOs.abstract_dao import DAO


class MagiaDao(DAO):
    def __init__(self, data_source='magia.pkl'):
        super().__init__(data_source)

    def add(self, magia: Magia):
        if((magia is not None) and isinstance(magia, Magia)):
            super().add(magia)

    def update(self, key, magia: Magia):
        if((magia is not None) and isinstance(magia, Magia)):
            super().update(key, magia)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)
