from model.magia import Magia
from model.exceptions.excpetion_magias import *
from typing import TYPE_CHECKING
from views.tela_magias import TelaMagias

if TYPE_CHECKING:
    from controller.controlador_sistema import ControladorSistema


class ControladorMagias:
    def __init__(self, controlador_sistema: "ControladorSistema"):
        self.__controlador_sistema = controlador_sistema
        # O dicionário de "Magias" iniciaria normalmente vazio, porém
        # para demonstração, utilzaremos alguns objetos já instanciados. 
        # Estes objetos receberão códigos acima de 999.
        self.__dict_magias: dict[int, Magia] = {
            1000: Magia('Bola de fogo', 5, 221),
            1001: Magia('Benção', 1, 221),
            1002: Magia('Desejo', 17, 234),
            1003: Magia('Raio de Gelo', 0, 273),
            1004: Magia('Truque de Corda', 3, 286),
            1005: Magia('Zona da Verdade', 3, 288)
        }
        self.__tela_magias = TelaMagias()
        self.__cod = 1

    def pegar_magia_por_nome(self, nome: str):
        for magia in self.__dict_magias.values():
            if magia.nome == nome:
                return magia

    def incluir_magia(self):
        try:
            dados_magia = self.__tela_magias.pegar_dados_magia()
            if dados_magia == 0:
                return False
            m = self.pegar_magia_por_nome(dados_magia['nome'])
            if m:
                raise MagiaJahExisteException(dados_magia['nome'])
            else:
                magia = Magia(
                    dados_magia['nome'],
                    dados_magia['nivel'],
                    dados_magia['pagina']
                    )
                self.__dict_magias[self.__cod] = magia
                self.__cod += 1
                self.__tela_magias.mensagem('Magia criada com sucesso!')
                return True
            
        except MagiaJahExisteException as e:
            self.__tela_magias.mensagem(e)
        except TypeError as e:
            self.__tela_magias.mensagem(f'[ERRO] Algum valor de entrada não foi inserido como esperado.')
        except KeyError as e:
            self.__tela_magias.mensagem(f"[ERRO] Dado ausente: {str(e)}")
        except Exception as e:
            self.__tela_magias.mensagem(f'[ERRO INESPERADO] Erro ao criar magia: {e}')
            
    def listar_magias(self):
        try:
            dados_para_tabela = []
            for cod, magia in self.__dict_magias.items():
                dados_para_tabela.append([
                    cod,
                    magia.nome,
                    magia.nivel,
                    magia.pagina,
                ])

            cabecalho = ['Cód', 'Nome', 'Nivel', 'Pág.']
            self.__tela_magias.exibir_tabela(cabecalho, dados_para_tabela)
        except Exception as e:
            self.__tela_magias.mensagem(f'[ERRO INESPERADO] Erro ao listar as magias: {str(e)}')

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
            self.__tela_magias.mensagem(f'[ERRO DE CHAVE] Erro ao excluir magia, código não encontrado: {str(e)}')
        except TypeError as e:
            self.__tela_magias.mensagem(f'[ERRO] Algum valor de entrada não foi inserido como esperado.')
        except Exception as e:
            self.__tela_magias.mensagem(f'[ERRO INESPERADO] Erro ao excluir magia: {str(e)}')

    def alterar_magia_por_cod(self):
        self.listar_magias()
        try:
            cod_validos = list(self.__dict_magias.keys()) + [0]
            identificador = self.__tela_magias.selecionar_obj_por_cod('Magia', cod_validos)
            if identificador == 0:
                return
            magia = self.__dict_magias[identificador]
            dados_novos = self.__tela_magias.pegar_dados_magia()
            i = self.pegar_magia_por_nome(dados_novos['nome'])
            if i is None:
                magia.nome = dados_novos['nome']
                magia.nivel = dados_novos['nivel']
                magia.pagina = dados_novos['pagina']
                self.__tela_magias.mensagem('Magia alterada com sucesso')
                return True
            else:
                raise MagiaJahExisteException(dados_novos['nome'])
        except MagiaJahExisteException  as e:
            self.__tela_magias.mensagem(e)
        except TypeError as e:
            self.__tela_magias.mensagem(f'[ERRO] Algum valor de entrada não foi inserido como esperado.')
        except KeyError as e:
            self.__tela_magias.mensagem(f'[ERRO DE CHAVE] Erro ao buscar magia, código não encontrado: {str(e)}')
        except Exception as e:
            self.__tela_magias.mensagem(f'[ERRO INESPERADO] Erro inesperado ao alterar magia por código: {str(e)}')

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

    @property
    def dict_magias(self):
        return self.__dict_magias