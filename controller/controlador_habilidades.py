from model.habilidade import Habilidade
from model.exceptions.excpetion_habilidades import *
from views.tela_habilidades import TelaHabilidades
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller.controlador_sistema import ControladorSistema


class ControladorHabilidades:

    def __init__(self, controlador_sistema: "ControladorSistema"):
        self.__controlador_sistema = controlador_sistema
        # O dicionário de "Habilidades" iniciaria normalmente vazio, porém
        # para demonstração, utilzaremos alguns objetos já instanciados. 
        # Estes objetos receberão códigos acima de 999.
        self.__dict_habilidades: dict[int, Habilidade] = {
            1000: Habilidade('Hab_especie', 1, 45, 'especie'),
            1001: Habilidade('Hab_subespecie', 2, 46, 'subespecie'),
            1002: Habilidade('Hab_classe', 1, 67, 'classe'),
            1003: Habilidade('Hab_subclasse', 1, 68, 'subclasse')
        }
        self.__tela_habilidades = TelaHabilidades()
        self.__cod = 1

    def pega_habilidade_por_nome(self, nome: str):
        try:
            for hab in self.__dict_habilidades.values():
                if hab.nome == nome:
                    return hab
            return None
        except Exception as e:
            self.__tela_habilidades.mensagem(f'[ERRO INESPERADO] Erro ao selecionar habilidade: {str(e)}')
    
    def incluir_habilidade(self):
        try:
            dados_hab = self.__tela_habilidades.pegar_dados_habilidade()
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
                self.__dict_habilidades[self.__cod] = nova_habilidade
                self.__cod += 1
                self.__tela_habilidades.mensagem('Habilidade criada com sucesso!')
                return True
         
        except HabilidadeJahExiste as e:
            self.__tela_habilidades.mensagem(e)
        except KeyError as e:
            self.__tela_habilidades.mensagem(f"[ERRO] Dado ausente: {str(e)}")
        except Exception as e:
            self.__tela_habilidades.mensagem(f'[ERRO INESPERADO] Erro ao incluir habilidade: {str(e)}')
    
    def listar_habilidades(self, origem='todas'):
        try:
            self.__tela_habilidades.mensagem(f"{'cod':^4} | {'nome':^16} | {'nível':^5} | {'pagina':^6} | {'origem':^10}")
            if origem == 'todas':
                habilidades_filtradas = {
                    k: h for k, h in self.__dict_habilidades.items()
                }
            elif origem == 'classe':
                habilidades_filtradas = {
                    k: h for k, h in self.__dict_habilidades.items() if h.origem == 'classe'
                }
            elif origem == 'subclasse':
                habilidades_filtradas = {
                    k: h for k, h in self.__dict_habilidades.items() if h.origem == 'subclasse'
                }
            elif origem == 'especie':
                habilidades_filtradas = {
                    k: h for k, h in self.__dict_habilidades.items() if h.origem == 'especie'
                }
            elif origem == 'subespecie':
                habilidades_filtradas = {
                    k: h for k, h in self.__dict_habilidades.items() if h.origem == 'subespecie'
                }
            else:
                raise ValueError("[ERRO] Origem inválida")

            for key, habilidade in habilidades_filtradas.items():
                self.__tela_habilidades.mostra_habilidade(
                    {
                    'cod': key ,
                    'nome': habilidade.nome,
                    'nivel': habilidade.nivel,
                    'pagina': habilidade.pagina,
                    'origem': habilidade.origem
                    }
                )

        except Exception as e:
            self.__tela_habilidades.mensagem(f'[ERRO INESPERADO] Erro ao listar habilidades: {str(e)}')
    
    def excluir_habilidade(self):
        try:
            self.listar_habilidades()
            cod_validos = list(self.__dict_habilidades.keys()) + [0]
            identificador = self.__tela_habilidades.selecionar_obj_por_cod('habilidade', cod_validos)
            if identificador == 0:
                return
            else:
                del self.__dict_habilidades[identificador]
                self.__tela_habilidades.mensagem('Habilidade removida!')
                return True
            
        except KeyError as e:
            self.__tela_habilidades.mensagem(f'[ERRO DE CHAVE] Erro ao excluir habilidade, código não encontrado: {str(e)}')    
        except Exception as e:
            self.__tela_habilidades.mensagem(f'[ERRO INESPERADO] Erro ao excluir habilidade: {str(e)}')

    def alterar_habilidade_por_cod(self):
        self.listar_habilidades()
        try:
            cod_validos = list(self.__dict_habilidades.keys()) + [0]
            identificador = self.__tela_habilidades.selecionar_obj_por_cod('habilidades', cod_validos)
            if identificador == 0:
                return False
            habilidade = self.__dict_habilidades[identificador]
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
            self.tela_habilidade.mensagem(e)
        except KeyError as e:
            self.__tela_habilidades.mensagem(f'[ERRO] Dado ausente: {str(e)}')
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
    def tela_habilidade(self):
        return self.__tela_habilidades
    
    @property
    def dict_habilidades(self):
        return self.__dict_habilidades

    @property
    def cod(self):
        return self.__cod
