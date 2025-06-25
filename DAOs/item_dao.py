from model.item import Item
from DAOs.abstract_dao import DAO


class ItemDao(DAO):
    def __init__(self, datasource='item.pkl'):
        super().__init__(datasource)

    def add(self, item: Item):
        if((item is not None) and isinstance(item, Item)):
            super().add(item)

    def update(self, key, item: Item):
        if((item is not None) and isinstance(item, Item)):
            super().update(key, item)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)