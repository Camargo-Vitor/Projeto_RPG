from views.tela_pessoas import TelaPessoas
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller.controlador_sistema import ControladorSistema


class controlador_pessoas:
    def __init__(self, controlador_sistema: "ControladorSistema"):
        self.__controlador_sistema = controlador_sistema
        self.__tela_pessoas = TelaPessoas
        self.__mestres = dict()
        self.__jogadores = dict()
        self.__cod_mestres = 1
        self.__cod_jogadores = 1