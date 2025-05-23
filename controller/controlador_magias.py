from model.magia import Magia
from model.exceptions.excpetion_magias import *
from typing import TYPE_CHECKING
from views.tela_magias import TelaMagias

if TYPE_CHECKING:
    from controller.controlador_sistema import ControladorSistema


class ControladorMagias:
    def __init__(self, controlador_sistema: "ControladorSistema"):
        self.__controlador_sistema = controlador_sistema
        self.__dict_magias: dict[int, Magia] = dict()
        self.__tela_magias = TelaMagias()
        self.__cod = 1

    def pegar_magia_por_nome(self, nome: str):
        try:
            for magia in self.__dict_magias.values():
                if magia.nome == nome:
                    return magia
        except Exception as e:
            self.__tela_magias.mensagem(f'[ERRO INESPERADO] Erro ao selecionar magia: {e}')

    def listar_magias(self):
        try:
            self.__tela_magias.mensagem(f"{'Cod':^4} | {'Nome':^16} | {'Nivel':^5} | {'Pagina':^5}")
            for cod, magia in self.__dict_magias.items():
                self.__tela_magias.mostra_magia({
                    'cod': cod,
                    'nome': magia.nome,
                    'nivel': magia.nivel,
                    'pagina': magia.pagina
                })

        except Exception as e:
            self.__tela_magias.mensagem(f'[ERRO INESPERADO] Erro ao listar magias: {e}')

    def incluir_magia(self):
        try:
            dados_magia = self.__tela_magias.pegar_dados_magia()
            m = self.pegar_magia_por_nome(dados_magia['nome'])
            if m is None:
                magia = Magia(
                    dados_magia['nome'],
                    dados_magia['nivel'],
                    dados_magia['pagina']
                    )
                self.__dict_magias[self.__cod] = magia
                self.__cod += 1
                return True
            else:
                raise MagiaJahExisteException()

        except MagiaJahExisteException as e:
            self.__tela_magias.mensagem(e)
        except Exception as e:
            self.__tela_magias.mensagem(f'[ERRO INESPERADO] Erro ao selecionar habilidade: {e}')

    def excluir_magia(self):
        try:
            self.listar_magias()
            cod_validos = list(self.__dict_magias.keys()) + [0]
            codigo = self.__tela_magias.selecionar_obj_por_cod('Magia', total_codigos=cod_validos)
            if codigo == 0:
                return False
            else:
                del self.__dict_magias[codigo]
                self.__tela_magias.mensagem('Magia removida!')
                return True

        except KeyError as e:
            self.__tela_magias.mensagem(f'[ERRO DE CHAVE] Erro ao excluir magia, código não encontrado: {e}')
        except Exception as e:
            self.__tela_magias.mensagem(f'[ERRO INESPERADO] Erro ao excluir magia: {e}')

    def alterar_magia_por_cod(self):
        try:
            self.listar_magias()
            cod_validos = list(self.__dict_magias.keys()) + [0]
            codigo = self.__tela_magias.selecionar_obj_por_cod('Magia', total_codigos=cod_validos)
            if codigo == 0:
                return
            else:
                magia = self.__dict_magias[codigo]
                novos_dados = self.__tela_magias.pegar_dados_magia()
                magia.nome = novos_dados['nome']
                magia.nivel = novos_dados['nivel']
                magia.pagina = novos_dados['pagina']

        except Exception as e:
            self.__tela_magias.mensagem(f'[ERRO INESPERADO] Erro ao selecionar habilidade: {e}')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
               0: self.retornar,
               1: self.incluir_magia,
               2: self.excluir_magia,
               3: self.listar_magias,
               4: self.alterar_magia_por_cod
               }
   
        while True:
            opc = self.__tela_magias.mostra_tela()
            metodo = opcoes[opc]
            metodo()
