from controller.controlador_item import ControladorItem
from views.tela_sistema import TelaSistema

class ControladorSistema:
    def __init__(self):
        self.__controlador_item = ControladorItem(self)
        self.__tela_sistema = TelaSistema()

    def inicializa_sistema(self):
        self.abre_tela()

    def chama_item(self):
        self.__controlador_item.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        opcoes = {
            1: self.chama_item,
            0: self.encerra_sistema
        }

        while True:
            opc_escolhida = self.__tela_sistema.mostra_tela()
            funcao_escolhida = opcoes[opc_escolhida]
            funcao_escolhida()
