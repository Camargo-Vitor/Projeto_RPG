from controller.controlador_itens import ControladorItens
from controller.controlador_especies import ControladorEspecies
from controller.controlador_magias import ControladorMagias
from controller.controlador_habilidades import ControladorHabilidades
from controller.controlador_pessoas import ControladorPessoas
from controller.controlador_classses import ControladorClasses
from controller.controlador_fichas import ControladorFichas
from views.tela_sistema import TelaSistema


class ControladorSistema:
    def __init__(self):
        self.__controlador_itens = ControladorItens(self)
        self.__controlador_especies = ControladorEspecies(self)
        self.__controlador_magias = ControladorMagias(self)
        self.__controlador_habilidades = ControladorHabilidades(self)
        self.__controlador_pessoas = ControladorPessoas(self)
        self.__controlador_classes = ControladorClasses(self)
        self.__controlador_fichas = ControladorFichas(self)
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

    def chama_pessoas(self):
        self.__controlador_pessoas.abre_tela()

    def chama_classe(self):
        self.__controlador_classes.abre_tela()

    def chama_fichas(self):
        self.__controlador_fichas.abre_tela()

    def encerra_sistema(self):
        self.__tela_sistema.mensagem('A aplicação falhou com sucesso!')
        exit(0)

    def abre_tela(self):
        opcoes = {
            1: self.chama_item,
            2: self.chama_magia,
            3: self.chama_habilidade,
            4: self.chama_especie,
            5: self.chama_classe,
            6: self.chama_pessoas,
            7: self.chama_fichas,
            0: self.encerra_sistema
        }

        while True:
            try:
                opc_escolhida = self.__tela_sistema.mostra_tela()
                funcao_escolhida = opcoes[opc_escolhida]
                funcao_escolhida()
            except Exception as e:
                self.__tela_sistema.mensagem(f'[ERRO INESPERADO] Erro interno: {e} ({type(e).__name__})')

    @property
    def controlador_itens(self):
        return self.__controlador_itens

    @property
    def controlador_especies(self):
        return self.__controlador_especies

    @property
    def controlador_magias(self):
        return self.__controlador_magias

    @property
    def controlador_habilidades(self):
        return self.__controlador_habilidades

    @property
    def controlador_pessoas(self):
        return self.__controlador_pessoas

    @property
    def controlador_classes(self):
        return self.__controlador_classes