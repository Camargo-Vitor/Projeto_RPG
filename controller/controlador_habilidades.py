from model.habilidade import Habilidade
from views.tela_habilidades import TelaHabilidades
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from controller.controlador_sistema import ControladorSistema

class ControladorHabilidades:

    def __init__(self, controlador_sistema: "ControladorSistema"):
        self.__controlador_sistema = controlador_sistema
        self.__tela_habilidades = TelaHabilidades()
        self.__dict_habilidades: dict[int, Habilidade] = dict()
        self.__cod = 0

    def pega_habilidade_por_nome(self, nome: str):
        for hab in self.__dict_habilidades.values():
            if hab.nome == nome:
                return hab
        return None
    
    def incluir_habilidade(self):
        dados_hab = self.__tela_habilidades.pegar_dados_habilidade()
        hab = self.pega_habilidade_por_nome(dados_hab['nome'])
        if hab == None:
            nova_habilidade = Habilidade(
                dados_hab['nome'],
                dados_hab['nivel'],
                dados_hab['pagina'],
                dados_hab['origem']
            )
            self.__dict_habilidades[self.__cod] = nova_habilidade
            self.__cod += 1
            return nova_habilidade
        return False

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.incluir_habilidade,
            0: self.retornar
        }
        opc = self.__tela_habilidades.mostra_tela()
        metodo = opcoes[opc]
        metodo()
