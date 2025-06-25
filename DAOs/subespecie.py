from model.subespecie import Subespecie
from DAOs.abstract_dao import DAO


class SubepecieDao(DAO):
    def __init__(self, datasource='subespecie.pkl'):
        super().__init__(datasource)

    def add(self, subespecie: Subespecie):
        if((subespecie is not None) and isinstance(subespecie, Subespecie)):
            super().add(subespecie)

    def update(self, key, subespecie: Subespecie):
        if((subespecie is not None) and isinstance(subespecie, Subespecie)):
            super().update(key, subespecie)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)
