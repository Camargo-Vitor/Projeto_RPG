from views.tela_pessoas import TelaPessoas
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller.controlador_sistema import ControladorSistema


class ControladorPessoas:
    def __init__(self, controlador_sistema: "ControladorSistema"):
        self.__controlador_sistema = controlador_sistema
        self.__tela_pessoas = TelaPessoas()
        self.__mestres = dict()
        self.__jogadores = dict()
        self.__cod_mestres = 1
        self.__cod_jogadores = 1

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela_mestre(self):
        opcoes = {
            0: self.abre_tela
        }
        while True:
            opc = self.__tela_pessoas.mostra_tela_mestre()
            metodo = opcoes[opc]
            metodo()

    def abre_tela_jogador(self):
        opcoes = {
            0: self.abre_tela
        }
        while True:
            opc = self.__tela_pessoas.mostra_tela_jogador()
            metodo = opcoes[opc]
            metodo()

    def abre_tela(self):
        opcoes = {
            1: self.abre_tela_mestre,
            2: self.abre_tela_jogador,
            0: self.retornar
        }
        while True:
            opc = self.__tela_pessoas.mostra_tela()
            metodo = opcoes[opc]
            metodo()