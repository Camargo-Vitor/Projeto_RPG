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
        self.__cod_classe = 1
        