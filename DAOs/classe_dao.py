from model.classe import Classe
from DAOs.abstract_dao import DAO


class ClasseDao(DAO):
    def __init__(self, datasource='classe.pkl'):
        super().__init__(datasource)

    def add(self, classe: Classe):
        if((classe is not None) and isinstance(classe, Classe)):
            super().add(classe)

    def update(self, key, classe: Classe):
        if((classe is not None) and isinstance(classe, Classe)):
            super().update(key, classe)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)
