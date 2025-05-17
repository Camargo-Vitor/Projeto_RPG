from controller.controlador_itens import ControladorItens
from controller.controlador_especies import ControladorEspecies
from controller.controlador_magias import ControladorMagias
from controller.controlador_habilidades import ControladorHabilidades
from views.tela_sistema import TelaSistema


class ControladorSistema:
    def __init__(self):
        self.__controlador_itens = ControladorItens(self)
        self.__controlador_especies = ControladorEspecies(self)
        self.__controlador_magias = ControladorMagias(self)
        self.__controlador_habilidades = ControladorHabilidades(self)
        self.__tela_sistema = TelaSistema()

    def inicializa_sistema(self):
        self.abre_tela()

    def chama_item(self):
        self.__controlador_itens.abre_tela()

    def chama_especie(self):
        self.__controlador_especies.abre_tela()

    def chama_magia(self):
        self.__controlador_magias.abre_tela()

    def chama_habilidade(self):
        self.__controlador_habilidades.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        opcoes = {
            1: self.chama_item,
            2: self.chama_magia,
            3: self.chama_habilidade,
            4: self.chama_especie,
            0: self.encerra_sistema
        }

        while True:
            opc_escolhida = self.__tela_sistema.mostra_tela()
            funcao_escolhida = opcoes[opc_escolhida]
            funcao_escolhida()
