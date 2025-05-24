from model.classe import Classe
from model.especie import Especie
from model.item import Item
from model.magia import Magia
from random import randint


class Ficha:
    def __init__(self,
                 nome_personagem: str,
                 descricao_fisica: str,
                 historia: str,
                 classe: Classe,
                 especie: Especie,
                 pericias_treinadas: list[str],
                 atributos: list[int]):
        self.__nome = nome_personagem
        self.__fisico = descricao_fisica
        self.__altura = especie.altura
        self.__historia = historia
        self.__pericias_treinadas = pericias_treinadas 
        if isinstance(classe, Classe) and isinstance(especie, Especie):
            self.__classe = classe
            self.__especie = especie


        self.__nivel = 1
        self.__bonus_pericia = 2 + (self.__nivel - 1)//4 
        self.__deslocamento = especie.deslocamento
        self.__inventario = []
        self.__lista_magias = []
        self.__habilidades = []

        for hab in self.classe.habilidades:
            if hab.nivel <= self.__nivel:
                self.__habilidades.append(hab)

        if type(classe) == 'subclasse':
            for hab in self.classe.hab_especificas:
                if hab.nivel <= self.__nivel:
                    self.__habilidades.append(hab)

        for hab in self.especie.habilidades:
            if hab.nivel <= self.__nivel:
                self.__habilidades.append(hab)
        
        for hab in self.especie.hab_especificas:
            if hab.nivel <= self.__nivel:
                self.__habilidades.append(hab)



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
        self.__dic_pericias = { 
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
        self.__nome = nome.strip().lower()

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
        self.__fisico = fisico.strip().lower()

    @property
    def altura(self):
        return self.__altura
    
    @property
    def historia(self):
        return self.__historia

    @historia.setter
    def historia(self, historia: str):
        self.__historia = historia.strip().lower()

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
    def deslocamento(self):
        return self.__deslocamento

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

    def subir_nivel(self):
        self.__nivel += 1
        self.__bonus_pericia = 2 + (self.__nivel - 1)//4 
        vida_adicional = randint(1, self.classe.dado_vida) + ((self.__atributos['constituicao'] - 10 ) // 2)
        self.__vida += vida_adicional
        self.__vida_atual += vida_adicional

        for hab in self.classe.habilidades:
            if hab.nivel == self.__nivel:
                self.__habilidades.append(hab)

        if type(self.classe) == 'subclasse':
            for hab in self.classe.hab_especificas:
                if hab.nivel <= self.__nivel:
                    self.__habilidades.append(hab)

        for hab in self.especie.habilidades:
            if hab.nivel == self.__nivel:
                self.__habilidades.append(hab)
        
        for hab in self.especie.hab_especificas:
            if hab.nivel == self.__nivel:
                self.__habilidades.append(hab)

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
        \nForça: {self.__atributos["forca"]} ({(self.__atributos["forca"] - 10) // 2})\
        \nDestreza: {self.__atributos["destreza"]} ({(self.__atributos["destreza"] - 10) // 2})\
        \nConstituição: {self.__atributos["constituicao"]} ({(self.__atributos["constituicao"] - 10) // 2})\
        \nInteligencia: {self.__atributos["inteligencia"]} ({(self.__atributos["inteligencia"] - 10) // 2})\
        \nSabedoria: {self.__atributos["sabedoria"]} ({(self.__atributos["sabedoria"] - 10) // 2})\
        \nCarisma: {self.__atributos["carisma"]} ({(self.__atributos["carisma"] - 10) // 2})\n' + \
        '><' * 8 + 'Utilitários' + '><' * 8 + f'\
        \nInventário: {"vazio" if self.inventario == [] else [str(x) for x in self.inventario]}\
        \nMagias: {"Nenhuma magia" if self.lista_magias == [] else [str(x) for x in self.lista_magias]}\
        \nHabilidades: {"Nenhuma habilidade" if self.habilidades == [] else [str(x) for x in self.habilidades]}'
