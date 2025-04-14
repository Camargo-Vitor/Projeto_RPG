from classe import Classe
from especie import Especie
from item import Item
from magia import Magia
from random import randint


class Ficha:
    def __init__(self, nome: str, fisico: str, historia: str, \
                classe: Classe, especie: Especie, pericias_treinadas: list):
        self.__nome = nome
        self.__fisico = fisico
        self.__altura = especie.altura
        self.__historia = historia
        self.__pericias_treinadas = pericias_treinadas 
        if isinstance(classe, Classe) and isinstance(especie, Especie):
            self.__classe = classe
            self.__especie = especie


        self.__nivel = 1
        self.__bonus_pericia = 2 + (self.__nivel - 1)//4 
        self.__inventario = []
        self.__lista_magias = []
        self.__habilidades = []

        for hab in self.classe.habilidades:
            if hab.nivel <= self.__nivel:
                self.__habilidades.append(hab)

        for hab in self.especie.habilidades:
            if hab.nivel <= self.__nivel:
                self.__habilidades.append(hab)


        self.__atributos = {
            'forca': sum(sorted(([int(randint(1, 6)) for x in range(4)]))[1:]),
            'destreza': sum(sorted(([int(randint(1, 6)) for x in range(4)]))[1:]),
            'constituicao': sum(sorted(([int(randint(1, 6)) for x in range(4)]))[1:]),
            'inteligencia': sum(sorted(([int(randint(1, 6)) for x in range(4)]))[1:]),
            'sabedoria': sum(sorted(([int(randint(1, 6)) for x in range(4)]))[1:]),
            'carisma': sum(sorted(([int(randint(1, 6)) for x in range(4)]))[1:])
        }

        self.__vida = classe.dado_vida + (self.__atributos['constituicao'] - 10) // 2
        self.__vida_atual = self.__vida
        self.__dic_pericias = { 
            'forca':{
                'atletismo': [(self.atributos["forca"] - 10) // 2, False]},

            'destreza':{
                'prestidigitacao': [(self.atributos["destreza"] -10) //2, False],
                'acrobacia': [(self.atributos["destreza"] -10) //2, False],
                'furtividade': [(self.atributos["destreza"] -10) //2, False]},

            'inteligencia':{
                'arcanismo': [(self.atributos["inteligencia"] -10) //2, False],
                'historia': [(self.atributos["inteligencia"] -10) //2, False],
                'investigacao': [(self.atributos["inteligencia"] -10) //2, False],
                'natureza': [(self.atributos["inteligencia"] -10) //2, False],
                'religiao': [(self.atributos["inteligencia"] -10) //2, False]},

            'sabedoria':{
                'percepcao': [(self.atributos["sabedoria"] -10) //2, False],
                'lidar_animais': [(self.atributos["sabedoria"] -10) //2, False],
                'intuicao': [(self.atributos["sabedoria"] -10) //2, False],
                'sobrevivencia': [(self.atributos["sabedoria"] -10) //2, False],
                'medicina': [(self.atributos["sabedoria"] -10) //2, False],},

            'carisma':{
                'persuasao': [(self.atributos["carisma"] -10) //2, False],
                'intimidacao': [(self.atributos["carisma"] -10) //2, False],
                'performance': [(self.atributos["carisma"] -10) //2, False],
                'intimidacao': [(self.atributos["carisma"] -10) //2, False]}
            }

        for dic in self.__dic_pericias.values():
            for chave in dic.keys():
                if chave in self.__pericias_treinadas:
                    dic[chave][0] = self.__bonus_pericia + dic[chave][0]
                    dic[chave][1] = True

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def pericias_treinadas(self):
        return self.__pericias_treinadas
    
    @property
    def bonus_pericia(self):
        return self.__bonus_pericia
    
    @property
    def fisico(self):
        return self.__fisico
    
    @fisico.setter
    def fisico(self, fisico: str):
        self.__fisico = fisico

    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, altura: int):
        self.__altura = altura

    @property
    def historia(self):
        return self.__historia

    @historia.setter
    def historia(self, historia: str):
        self.__historia = historia

    @property
    def atributos(self):
        return self.__atributos

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
    
    @vida.setter
    def vida(self, vida: int):
        if isinstance(vida, int):
            self.__vida = vida

    @property
    def vida_atual(self):
        return self.__vida_atual

    @vida_atual.setter
    def vida_atual(self, nova_vida: int):
        self.__vida_atual = nova_vida

    @property
    def nivel(self):
        return self.__nivel

    @property
    def inventario(self):
        return self.__inventario

    def add_item_inventario(self, item: Item):
        if isinstance(item, Item):
            self.__inventario.append(item)

    def rm_item_inventario(self, item: Item):
        if item in self.inventario:
            self.inventario.remove(item)

    @property
    def lista_magias(self):
        return self.__lista_magias

    def add_magia(self, magia: Magia):
        if isinstance(magia, Magia):
            self.lista_magias.append(magia)

    def rm_magia(self, magia: Magia):
        if magia in self.__lista_magias:
            self.__lista_magias.remove(magia)

    @property
    def habilidades(self):
        return self.__habilidades

    def __str__(self):
        return '><' * 8 + 'Ficha de Personagem' + '><' * 8 + \
        f'\nNome: {self.nome}\
        \nVida: {self.vida}\
        \nNível: {self.nivel}\
        \nDeslocamento: {self.especie.deslocamento}\
        \nFisico: {self.fisico}\
        \nAltura: {self.altura}cm\
        \nHistória: {self.historia}\
        \nClasse: {self.classe.nome}\
        \nEspecie: {self.especie.nome}\n' + \
        '><' * 8 + 'Atributos' + '><' * 8 + f'\
        \nForça: {self.atributos["forca"]} ({(self.atributos["forca"] - 10) // 2})\
        \nDestreza: {self.atributos["destreza"]} ({(self.atributos["destreza"] - 10) // 2})\
        \nConstituição: {self.atributos["constituicao"]} ({(self.atributos["constituicao"] - 10) // 2})\
        \nInteligencia: {self.atributos["inteligencia"]} ({(self.atributos["inteligencia"] - 10) // 2})\
        \nSabedoria: {self.atributos["sabedoria"]} ({(self.atributos["sabedoria"] - 10) // 2})\
        \nCarisma: {self.atributos["carisma"]} ({(self.atributos["carisma"] - 10) // 2})\n' + \
        '><' * 8 + 'Utilitários' + '><' * 8 + f'\
        \nInventário: {"vazio" if self.inventario == [] else [str(x) for x in self.inventario]}\
        \nMagias: {"Nenhuma magia" if self.lista_magias == [] else [str(x) for x in self.lista_magias]}\
        \nHabilidades: {"Nenhuma habilidade" if self.habilidades == [] else [str(x) for x in self.habilidades]}'
    