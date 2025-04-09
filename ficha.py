from classe import Classe
from especie import Especie
from item import Item
from magia import Magia
from random import randint


class Ficha:
    def __init__(self, nome: str, fisico: str, historia: str, \
                classe: Classe, especie: Especie):
        self.__nome = nome
        self.__fisico = fisico
        self.__historia = historia
        self.__atributos = {
            'forca': sum(sorted(([int(randint(1, 6)) for x in range(4)]))[1:]),
            'destreza': sum(sorted(([int(randint(1, 6)) for x in range(4)]))[1:]),
            'constituicao': sum(sorted(([int(randint(1, 6)) for x in range(4)]))[1:]),
            'inteligencia': sum(sorted(([int(randint(1, 6)) for x in range(4)]))[1:]),
            'sabedoria': sum(sorted(([int(randint(1, 6)) for x in range(4)]))[1:]),
            'carisma': sum(sorted(([int(randint(1, 6)) for x in range(4)]))[1:])
        }
        if isinstance(classe, Classe) and isinstance(especie, Especie):
            self.__classe = classe
            self.__especie = especie

        self.__vida = classe.dado_vida + self.__atributos['constituicao'] // 5
        self.__nivel = 1
        self.__inventario = []
        self.__lista_magias = []
        self.__habilidades = []

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def fisico(self):
        return self.__fisico
    
    @fisico.setter
    def fisico(self, fisico: str):
        self.__fisico = fisico

    @property
    def historia(self):
        return self.__historia

    @historia.setter
    def historia(self, historia: str):
        self.__historia = historia

    @property
    def atributos(self):
        return self.__atributos
    
    #precisa de setter?

    @property
    def classe(self):
        return self.__classe
    
    @classe.setter
    def classe(self, classe: Classe):
        if isinstance(classe, Classe):
            self.__classe = classe

    @property
    def especie(self):
        return self.__especie
    
    @especie.setter
    def especie(self, especie: Especie):
        if isinstance(especie, Especie):
            self.__especie = especie

    @property
    def vida(self):
        return self.__vida
    
    #precisa de setter?

    @property
    def nivel(self):
        return self.__nivel
    
    #precisa de setter?

    @property
    def inventario(self):
        return self.__inventario
    
    #precisa de setter?

    @property
    def lista_magias(self):
        return self.__lista_magias
    
    #precisa de setter?

    @property
    def habilidades(self):
        return self.__habilidades
    
    #precisa de setter?

    def add_item_inventario(self, item: Item):
        if isinstance(item, Item):
            self.__inventario.append(item)

    def add_magia(self, magia: Magia):
        if isinstance(magia, Magia):
            self.lista_magias.append(magia)

    def add_hab(self, nome: str):
        for hab, niv in self.classe.habilidades.items():
            if nome == hab and self.nivel >= niv:
                self.habilidades.append(self.classe.habilidades[nome])

