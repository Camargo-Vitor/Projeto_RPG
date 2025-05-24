from model.ficha import Ficha
from views.tela_fichas import TelaFichas
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller.controlador_sistema import ControladorSistema


class ControladorFichas:
    def __init__(self, controlador_sistema: "ControladorSistema"):
        self.__controlador_sistema = controlador_sistema
        self.__tela_fichas = TelaFichas()
        self.__cod = 1
        self.__dict_fichas: dict[int, Ficha] = dict()

    def incluir_ficha(self):
        try:

            #atributos
            atributos = self.__tela_fichas.pegar_dados_atributos()
            #dados basicos
            dados__basicos_ficha = self.__tela_fichas.pegar_dados_basicos_ficha()

            #classe
            self.__controlador_sistema.controlador_classes.listar_classes()
            codigos_validos = list(self.__controlador_sistema.controlador_classes.dict_classes.keys()) + [0]
            codigo_classe = self.__tela_fichas.le_int_ou_float(
                'Digite o código da classe (0 para cancelar): ',
                conjunto_alvo = codigos_validos
                )
            if codigo_classe == 0:
                return False
            else:
                classe = self.__controlador_sistema.controlador_classes.dict_classes[codigo_classe]

            #subespecie
            self.__controlador_sistema.controlador_especies.listar_subespecies()
            codigos_validos = list(self.__controlador_sistema.controlador_especies.dict_subespecie.keys()) + [0]
            codigo_subespecie = self.__tela_fichas.le_int_ou_float(
                'Digite o código da subespecie (0 para cancelar): ',
                conjunto_alvo = codigos_validos
                )
            if codigo_subespecie == 0:
                return False
            else:
                subespecie = self.__controlador_sistema.controlador_especies.dict_subespecie[codigo_subespecie]
            
            #pericias
            pericias_treinadas = self.__tela_fichas.pegar_dados_pericias()

            nova_ficha = Ficha(
                dados__basicos_ficha['nome_personagem'],
                dados__basicos_ficha['descricao_fisica'],
                dados__basicos_ficha['historia'],
                classe,
                subespecie,
                pericias_treinadas,
                atributos)
            
            self.__dict_fichas[self.__cod] = nova_ficha
            print(nova_ficha)
            return True

        except Exception as e:
            self.__tela_fichas.mensagem(f'[ERRO INESPERADO] Erro ao criar Ficha: {e} ({type(e).__name__})')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.incluir_ficha,
            0: self.retornar
        }
        opc = self.__tela_fichas.mostra_tela()
        metodo = opcoes[opc]
        metodo()

    @property
    def tela_fichas(self):
        return self.__tela_fichas

    @property
    def cod(self):
        return self.__cod

    @property
    def dict_fichas(self):
        return self.__dict_fichas
