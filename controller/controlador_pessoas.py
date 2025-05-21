from views.tela_pessoas import TelaPessoas
from model.pessoa import Pessoa
from model.mestre import Mestre
from model.jogador import Jogador
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller.controlador_sistema import ControladorSistema
    


class ControladorPessoas:
    def __init__(self, controlador_sistema: "ControladorSistema"):
        self.__controlador_sistema = controlador_sistema
        self.__tela_pessoas = TelaPessoas()
        self.__pessoas: dict[int, Pessoa] = dict()
        self.__cod = 1

    def listar_pessoas(self):
        self.__tela_pessoas.mensagem(f'{"Cod":^4} | {"Nome":^16} | {"Telefone":^13} | {"Cidade":^16} | \
                                       {"Bairro":^12} | {"Numero":^6} | {"Cep":^10} | {"Personagens":^12}')
        for cod, pessoa in self.__pessoas.items():
            dados_pessoa = {
                'cod': cod,
                'nome': pessoa.nome,
                'telefone': pessoa.telefone,
                'cidade': pessoa.endereco.cidade,
                'bairro': pessoa.endereco.bairro,
                'numero': pessoa.endereco.numero,
                'cep': pessoa.endereco.cep
                
            }

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