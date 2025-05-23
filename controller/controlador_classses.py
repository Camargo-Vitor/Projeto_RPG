from model.classe import Classe
from model.subclasse import Subclasse
from views.tela_classes import TelaClasses
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controlador_sistema import ControladorSistema


class ControladorClasses:
    def __init__(self, controlador_sistema: "ControladorSistema"):
        self.__controlador_sistema = controlador_sistema
        self.__tela_classes = TelaClasses()
        self.__dict__classes : dict[int, Classe] = dict()
        self.__cod = 1

    def pega_classe_por_nome(self, nome: str):
        for classe in self.__dict__classes.values():
            if classe.nome== nome:
                return classe
        return None
    
    def incluir_classe(self):
        dados_classe = self.tela_classes.pegar_dados_classes()
        c = self.pega_classe_por_nome(dados_classe['nome'])
        if c is None:
            for a in range(3):
                classe = Classe(
                    dados_classe['nome'],
                    dados_classe['dado'],
                    dados_classe['nome sub'][a]
                )
            self.__dict__classes[self.__cod] = classe
            self.__cod += 1
            self.tela_classes.mensagem('Classe criada com sucesso!')
        else:
            self.tela_classes.mensagem('A classe criada ja existe!')
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.incluir_classe,
        }

        while True:
            opc = self.__tela_classes.mostra_tela()
            metodo = opcoes[opc]
            metodo()

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
    
    @property
    def tela_classes(self):
        return self.__tela_classes
    
    @property
    def dict_classes(self):
        return self.__dict__classes
            
        