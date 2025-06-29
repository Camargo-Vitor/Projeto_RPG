from model.classe import Classe
from model.subespecie import Subespecie
from model.item import Item
from model.magia import Magia
from random import randint


class Ficha:
    def __init__(self,
                 nome_personagem: str,
                 descricao_fisica: str,
                 historia: str,
                 moedas: int,
                 classe: Classe,
                 especie: Subespecie,
                 pericias_treinadas: list[str],
                 atributos: list[int]):
        if isinstance(classe, Classe) and isinstance(especie, Subespecie):
            self.__nome = nome_personagem
            self.__fisico = descricao_fisica
            self.__historia = historia
            self.__moedas = moedas
            self.__pericias_treinadas = pericias_treinadas 
            self.__classe = classe
            self.__subclasse = None
            self.__especie = especie
            self.__nivel = 1
            self.__bonus_pericia = 2 + (self.__nivel - 1)//4 
            self.__altura = especie.altura
            self.__deslocamento = especie.deslocamento
            self.__atributos = {
                'forca': atributos[0],
                'destreza': atributos[1],
                'constituicao': atributos[2],
                'inteligencia': atributos[3],
                'sabedoria': atributos[4],
                'carisma': atributos[5]
            }
            self.__vida = classe.dado_vida + (self.__atributos['constituicao'] - 10) // 2
            self.__vida_atual = self.__vida
            self.__inventario: list[Item] = []
            self.__lista_magias: list[Magia] = []
            self.__dict_pericias = { 
                'forca':{
                    'atletismo': [(self.__atributos["forca"] - 10) // 2, False]},

                'destreza':{
                    'prestidigitacao': [(self.__atributos["destreza"] -10) //2, False],
                    'acrobacia': [(self.__atributos["destreza"] -10) //2, False],
                    'furtividade': [(self.__atributos["destreza"] -10) //2, False]},

                'inteligencia':{
                    'arcanismo': [(self.__atributos["inteligencia"] -10) //2, False],
                    'historia': [(self.__atributos["inteligencia"] -10) //2, False],
                    'investigacao': [(self.__atributos["inteligencia"] -10) //2, False],
                    'natureza': [(self.__atributos["inteligencia"] -10) //2, False],
                    'religiao': [(self.__atributos["inteligencia"] -10) //2, False]},

                'sabedoria':{
                    'percepcao': [(self.__atributos["sabedoria"] -10) //2, False],
                    'lidar_animais': [(self.__atributos["sabedoria"] -10) //2, False],
                    'intuicao': [(self.__atributos["sabedoria"] -10) //2, False],
                    'sobrevivencia': [(self.__atributos["sabedoria"] -10) //2, False],
                    'medicina': [(self.__atributos["sabedoria"] -10) //2, False],},

                'carisma':{
                    'persuasao': [(self.__atributos["carisma"] -10) //2, False],
                    'intimidacao': [(self.__atributos["carisma"] -10) //2, False],
                    'performance': [(self.__atributos["carisma"] -10) //2, False],
                    'enganacao': [(self.__atributos["carisma"] -10) //2, False]}
                }

            for dic in self.__dict_pericias.values():
                for chave in dic.keys():
                    if chave in self.__pericias_treinadas:
                        dic[chave][0] = self.__bonus_pericia + dic[chave][0]
                        dic[chave][1] = True

    @property
    def nome(self):
        return self.__nome

    @property
    def fisico(self):
        return self.__fisico

    @property
    def historia(self):
        return self.__historia

    @property
    def moedas(self):
        return self.__moedas

    @property
    def pericias_treinadas(self):
        return self.__pericias_treinadas

    @property
    def bonus_pericia(self):
        return self.__bonus_pericia
    
    @property
    def classe(self):
        return self.__classe

    @property
    def especie(self):
        return self.__especie

    @property
    def nivel(self):
        return self.__nivel

    @property
    def bonus_pericia(self):
        return self.__bonus_pericia

    @property
    def altura(self):
        return self.__altura

    @property
    def deslocamento(self):
        return self.__deslocamento

    @property
    def atributos(self):
        return self.__atributos

    @property
    def vida(self):
        return self.__vida

    @property
    def vida_atual(self):
        return self.__vida_atual

    @property
    def inventario(self):
        return self.__inventario

    @property
    def lista_magias(self):
        return self.__lista_magias

    @property
    def dict_pericias(self):
        return self.__dict_pericias

    @property
    def subclasse(self):
        return self.__subclasse

    @subclasse.setter
    def subclasse(self, subclasse):
        self.__subclasse = subclasse

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
    
    @fisico.setter
    def fisico(self, fisico: str):
        self.__fisico = fisico

    @moedas.setter
    def moedas(self, moedas: int):
        if isinstance(moedas, int):
            self.__moedas = moedas

    @historia.setter
    def historia(self, historia: str):
        self.__historia = historia
    
    @classe.setter
    def classe(self, classe: Classe):
        if isinstance(classe, Classe):
            self.__classe = classe

    @especie.setter
    def especie(self, especie: Subespecie):
        if isinstance(especie, Subespecie):
            self.__especie = especie
    
    @vida.setter
    def vida(self, vida: int):
        if isinstance(vida, int):
            self.__vida = vida

    @vida_atual.setter
    def vida_atual(self, nova_vida: int):
        self.__vida_atual = nova_vida

    def add_item_inventario(self, item: Item):
        if isinstance(item, Magia) and not sum([item.nome == item_lista.nome for item_lista in self.__inventario]):
            self.__inventario.append(item)

    def rm_item_inventario(self, item: Item):
        for item_lista in self.inventario:
            if item.nome == item_lista.nome:
                self.inventario.remove(item_lista)
                return True
        raise Exception('Magia não está na ficha')

    def add_magia(self, magia: Magia):
        if isinstance(magia, Magia) and not sum([magia.nome == magia_lista.nome for magia_lista in self.__lista_magias]):
            self.lista_magias.append(magia)
        else:
            raise Exception('Magia já está na ficha')

    def rm_magia(self, magia: Magia):
        for magia_lista in self.__lista_magias:
            if magia.nome == magia_lista.nome:
                self.__lista_magias.remove(magia_lista)
                return True
        raise Exception('Magia não está na ficha')

    def subir_nivel(self):
        self.__nivel += 1
        self.__bonus_pericia = 2 + (self.__nivel - 1)//4 
        vida_adicional = randint(1, self.classe.dado_vida) + ((self.__atributos['constituicao'] - 10 ) // 2)
        self.__vida += vida_adicional
        self.__vida_atual += vida_adicional
        if self.__vida_atual > self.__vida:
            self.__vida_atual = self.__vida

        for dic in self.__dict_pericias.values():
            for chave in dic.keys():
                if chave in self.__pericias_treinadas:
                    dic[chave][0] = self.__bonus_pericia + dic[chave][0]
                    dic[chave][1] = True
