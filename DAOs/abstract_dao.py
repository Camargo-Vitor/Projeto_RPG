import pickle
from abc import ABC, abstractmethod

class DAO(ABC):
    @abstractmethod
    def __init__(self, data_source=''):
        self.__data_source = data_source
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__data_source, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__data_source,'rb'))

    #esse método precisa chamar o self.__dump()
    @abstractmethod
    def add(self, obj):
        try:
            cod = max([key for key in self.__cache.keys()]) + 1
        except Exception:
            cod = 1
        self.__cache[cod] = obj
        self.__dump()  #atualiza o arquivo depois de add novo amigo

    @abstractmethod
    def update(self, key, obj):
        try:
            if(self.__cache[key] != None):
                self.__cache[key] = obj #atualiza a entrada
                self.__dump()  #atualiza o arquivo
        except KeyError:
            pass  # implementar aqui o tratamento da exceção

    @abstractmethod
    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            pass #implementar aqui o tratamento da exceção

    # esse método precisa chamar o self.__dump()
    @abstractmethod
    def remove(self, key):
        self.__cache.pop(key)
        self.__dump() #atualiza o arquivo depois de remover um objeto

    def get_all(self):
        return self.__cache.values()

    def get_keys(self):
        if self.__cache:
            return self.__cache.keys()

    @property
    def cache(self):
        return self.__cache