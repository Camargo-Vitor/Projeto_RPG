from views.tela_especies import TelaEspecies
from model.especie import Especie
from model.subespecie import Subespecie
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller.controlador_sistema import ControladorSistema


class ControladorEspecies:
    def __init__(self, controlador_sistema: "ControladorSistema"):
        self.__controlador_sistema = controlador_sistema
        self.__dict_especie: dict[int, Especie] = dict()
        self.__dict_subespecie: dict[int, Subespecie] = dict()
        self.__tela_especies = TelaEspecies()
        self.__cod_esp = 1

    def pega_especie_por_nome(self, nome: str):
        for especie in self.__dict_especie.values():
            if especie.nome == nome:
                return especie
        return None
    
    def pega_subespecie_por_nome(self, nome: str):
        for subespecie in self.__dict_subespecie.values():
            if subespecie.nome == nome:
                return nome
        return None
    
    def incluir_especie(self):
        dados_especie = self.__tela_especies.pegar_especie_dados()
        e = self.pega_especie_por_nome(dados_especie['nome'])
        if e is None:
            especie = Especie(
                dados_especie['nome'],
                dados_especie['deslocamento'],
                dados_especie['altura'],
                dados_especie['habilidade(s)']
                    )
            self.__dict_especie[self.__cod_esp] = especie
            self.__cod_esp +=1
            self.__tela_especies.mensagem('Espécie criada com sucesso!')
        else:
            self.__tela_especies.mensagem('A espécie criada já existe')

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
