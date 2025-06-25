from model.habilidade import Habilidade
from model.exceptions.excpetion_habilidades import *
from views.tela_habilidades import TelaHabilidades
from DAOs.habilidade_dao import HabilidadeDao
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller.controlador_sistema import ControladorSistema


class ControladorHabilidades:

    def __init__(self, controlador_sistema: "ControladorSistema"):
        self.__controlador_sistema = controlador_sistema
        self.__habilidade_DAO = HabilidadeDao()
        self.__tela_habilidades = TelaHabilidades()

    def pega_habilidade_por_nome(self, nome: str):
        try:
            for hab in self.__habilidade_DAO.get_all():
                if hab.nome == nome:
                    return hab
            return None
        except Exception as e:
            self.__tela_habilidades.mensagem(f'[ERRO INESPERADO] Erro ao selecionar habilidade: {str(e)}')
    
    def incluir_habilidade(self):
        try:
            dados_hab = self.__tela_habilidades.pegar_dados_habilidade()
            if dados_hab == 0:
                return False
            hab = self.pega_habilidade_por_nome(dados_hab['nome'])
            if hab:
                raise HabilidadeJahExiste(dados_hab['nome'])
            else:
                nova_habilidade = Habilidade(
                    dados_hab['nome'],
                    dados_hab['nivel'],
                    dados_hab['pagina'],
                    dados_hab['origem']
                )
                self.__habilidade_DAO.add(nova_habilidade)
                self.__tela_habilidades.mensagem('Habilidade criada com sucesso!')
                return True
         
        except HabilidadeJahExiste as e:
            self.__tela_habilidades.mensagem(e)
        except TypeError as e:
            self.__tela_habilidades.mensagem(f'[ERRO] Algum valor de entrada não foi inserido como esperado.')
        except KeyError as e:
            self.__tela_habilidades.mensagem(f"[ERRO] Dado ausente: {str(e)}")
        except Exception as e:
            self.__tela_habilidades.mensagem(f'[ERRO INESPERADO] Erro ao incluir habilidade: {str(e)}')
    
    def listar_habilidades(self, origem='todas'):
        try:
            if origem == 'todas':
                habilidades_filtradas = {
                    k: h for k, h in self.__habilidade_DAO.cache.items()
                }
            elif origem == 'classe':
                habilidades_filtradas = {
                    k: h for k, h in self.__habilidade_DAO.cache.items() if h.origem == 'classe'
                }
            elif origem == 'subclasse':
                habilidades_filtradas = {
                    k: h for k, h in self.__habilidade_DAO.cache.items() if h.origem == 'subclasse'
                }
            elif origem == 'especie':
                habilidades_filtradas = {
                    k: h for k, h in self.__habilidade_DAO.cache.items() if h.origem == 'especie'
                }
            elif origem == 'subespecie':
                habilidades_filtradas = {
                    k: h for k, h in self.__habilidade_DAO.cache.items() if h.origem == 'subespecie'
                }
            else:
                raise ValueError("[ERRO] Origem inválida")

            dados_para_tabela = []
            for cod, habilidade in habilidades_filtradas.items():
                dados_para_tabela.append([
                    cod,
                    habilidade.nome,
                    habilidade.nivel,
                    habilidade.pagina,
                    habilidade.origem,
                ])

            cabecalho = ['Cód', 'Nome', 'Nivel', 'Pagina', 'Tipo']
            self.__tela_habilidades.exibir_tabela(cabecalho, dados_para_tabela)

        except Exception as e:
            self.__tela_habilidades.mensagem(f'[ERRO INESPERADO] Erro ao listar habilidades: {str(e)}')
    
    def excluir_habilidade(self):
        try:
            self.listar_habilidades()
            cod_validos = list(self.__habilidade_DAO.get_keys()) + [0]
            identificador = self.__tela_habilidades.selecionar_obj_por_cod('habilidade', cod_validos)
            if identificador == 0:
                return
            else:
                del self.__habilidade_DAO.remove(identificador)
                self.__tela_habilidades.mensagem('Habilidade removida!')
                return True
            
        except KeyError as e:
            self.__tela_habilidades.mensagem(f'[ERRO DE CHAVE] Erro ao excluir habilidade, código não encontrado: {str(e)}')
        except TypeError as e:
            self.__tela_habilidades.mensagem(f'[ERRO] Algum valor de entrada não foi inserido como esperado.')
        except Exception as e:
            self.__tela_habilidades.mensagem(f'[ERRO INESPERADO] Erro ao excluir habilidade: {str(e)}')

    def alterar_habilidade_por_cod(self):
        self.listar_habilidades()
        try:
            cod_validos = list(self.__habilidade_DAO.get_keys()) + [0]
            identificador = self.__tela_habilidades.selecionar_obj_por_cod('habilidades', cod_validos)
            if identificador == 0:
                return False
            habilidade = self.__habilidade_DAO[identificador]
            dados_novos = self.__tela_habilidades.pegar_dados_habilidade()
            i = self.pega_habilidade_por_nome(dados_novos['nome'])
            if i is None:
                habilidade.nome = dados_novos['nome']
                habilidade.nivel = dados_novos['nivel']
                habilidade.pagina = dados_novos['pagina']
                habilidade.origem = dados_novos['origem']
                self.__tela_habilidades.mensagem(f'Habilidade de código {identificador} alterada com sucesso!')
                return True
            else:
                raise HabilidadeJahExiste(dados_novos['nome'])
        except HabilidadeJahExiste as e:
            self.__tela_habilidades.mensagem(e)
        except TypeError as e:
            self.__tela_habilidades.mensagem(f'[ERRO] Algum valor de entrada não foi inserido como esperado.')
        except KeyError as e:
            self.__tela_habilidades.mensagem(f'[ERRO DE CHAVE] Erro ao buscar habilidade, código não encontrado: {str(e)}')
        except Exception as e:
            self.__tela_habilidades.mensagem(f'[ERRO INESPERADO] Erro inesperado ao alterar habilidade por código: {e}')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.incluir_habilidade,
            2: self.excluir_habilidade,
            3: self.listar_habilidades,
            4: self.alterar_habilidade_por_cod,
            0: self.retornar
        }
        while True:
            opc = self.__tela_habilidades.mostra_tela()
            metodo = opcoes[opc]
            metodo()

    @property
    def habilidade_DAO(self):
        return self.__habilidade_DAO
