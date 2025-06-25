from model.especie import Especie
from DAOs.abstract_dao import DAO


class EspecieDao(DAO):
    def __init__(self, datasource='especie.pkl'):
        super().__init__(datasource)

    def add(self, especie: Especie):
        if((especie is not None) and isinstance(especie, Especie)):
            super().add(especie)

    def update(self, key, especie: Especie):
        if((especie is not None) and isinstance(especie, Especie)):
            super().update(key, especie)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)
