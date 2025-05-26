from views.tela_pessoas import TelaPessoas
from model.mestre import Mestre
from model.jogador import Jogador
from model.exceptions.exception_pessoas import *
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller.controlador_sistema import ControladorSistema
    


class ControladorPessoas:
    def __init__(self, controlador_sistema: "ControladorSistema"):
        self.__controlador_sistema = controlador_sistema
        self.__tela_pessoas = TelaPessoas()
        # O dicionário de "Jogadores" iniciaria normalmente vazio, porém
        # para demonstração, utilzaremos alguns objetos já instanciados. 
        # Estes objetos receberão códigos acima de 999.
        self.__jogadores: dict[int, Jogador] = dict()
        self.__mestre: Mestre = Mestre('[VAZIO]', 0, '[VAZIO]', 'VAZIO', 0, 0)
        self.__cod = 1
    
    def pega_pessoa_por_nome(self, nome: str):
        for pessoa in self.__jogadores.values():
            if pessoa.nome == nome:
                return pessoa
        return None
    
    def incluir_jogador(self):
        try:
            dados_pessoa = self.__tela_pessoas.pegar_dados_pessoa()
            m = self.pega_pessoa_por_nome(dados_pessoa['nome'])
            if m:
                raise JogadorJahExisteException(dados_pessoa['nome']) 
            else:
                jogador = Jogador(
                    dados_pessoa['nome'],
                    dados_pessoa['telefone'],
                    dados_pessoa['cidade'],
                    dados_pessoa['bairro'],
                    dados_pessoa['numero'],
                    dados_pessoa['cep'],
                )
                self.__jogadores[self.__cod] = jogador
                self.__cod +=1
                self.__tela_pessoas.mensagem('Jogador criado com sucesso')
                return True 
        except JogadorJahExisteException as e:
            self.__tela_pessoas.mensagem(e)
        except KeyError as e:
            self.__tela_pessoas.mensagem(f"[ERRO] Dado ausente: {str(e)}")
        except Exception as e:
            self.__tela_pessoas.mensagem(f'[ERRO INESPERADO] Erro ao incluir jogador: {str(e)}')
    
    def listar_jogador(self):
        try:
            self.__tela_pessoas.mensagem(f'{"Cod":^4} | {"Nome":^16} | {"Telefone":^13} | {"Cidade":^16} | {"Bairro":^12} | {"Numero":^6} | {"Cep":^10} | {"Personagens":^12}')
            for cod, jogador in self.__jogadores.items():
                self.__tela_pessoas.mostra_jogador(
                    {
                    'cod': cod,
                    'nome': jogador.nome,
                    'telefone': jogador.telefone,
                    'cidade': jogador.endereco.cidade,
                    'bairro': jogador.endereco.bairro,
                    'numero': jogador.endereco.numero,
                    'cep': jogador.endereco.cep,
                    'personagens': [jogador.nome for jogador in jogador.personagens]
                }
                )

        except Exception as e:
            self.__tela_pessoas.mensagem(f'[ERRO INESPERADO] Erro ao listar as jogador: {str(e)}')

    def excluir_jogador(self):
        try:
            self.listar_jogador()
            cod_validos = list(self.__jogadores.keys()) + [0]
            identificador = self.__tela_pessoas.selecionar_obj_por_cod('jogador', cod_validos)
            if identificador == 0:
                return False
            else:
                del self.__jogadores[identificador]
                self.__tela_pessoas.mensagem('Jogador Removido')
                return True
        except KeyError as e:
            self.__tela_pessoas.mensagem(f'[ERRO DE CHAVE] Erro ao excluir jogador, código não encontrado: {str(e)}')
        except Exception as e:
            self.__tela_pessoas.mensagem(f'[ERRO INESPERADO] Erro ao excluir jogador: {e}')

    def alterar_jogador_por_cod(self):
        try:
            self.listar_jogador()
            codigo_validos = list(self.__jogadores.keys()) + [0]
            identificador = self.__tela_pessoas.selecionar_obj_por_cod('jogador', codigo_validos)
            if identificador == 0:
                return False
            else:
                jogador = self.__jogadores[identificador]
                dados_novos = self.__tela_pessoas.pegar_dados_pessoa()
                j = self.pega_pessoa_por_nome(dados_novos['nome'])
                if j is None:
                    jogador.nome = dados_novos['nome']
                    jogador.telefone = dados_novos['telefone']
                    jogador.endereco.cidade = dados_novos['cidade']
                    jogador.endereco.bairro = dados_novos['bairro']
                    jogador.endereco.numero = dados_novos['numero']
                    jogador.endereco.cep = dados_novos['cep']
                    return True
                else:
                    raise JogadorJahExisteException
        except JogadorJahExisteException as e:
            self.__tela_pessoas.mensagem(e)
        except KeyError as e:
            self.__tela_pessoas.mensagem(f'[ERRO DE CHAVE] Dado ausente: {str(e)}')
        except Exception as e:
            self.__tela_pessoas.mensagem(f'[ERRO INESPERADO] Erro ao alterar jogador: {e}')

    def add_ficha(self):
        try:
            self.listar_jogador()
            cod_validos = list(self.__jogadores.keys()) + [0]
            identificador = self.__tela_pessoas.selecionar_obj_por_cod('jogadores', cod_validos)
            if identificador == 0:
                return False
            else:
                fichas = self.__controlador_sistema.controlador_fichas.dict_fichas
                cod_validos_fichas = list(fichas.keys()) + [0]
                self.__controlador_sistema.controlador_fichas.listar_fichas(selecao=False)
                identificador_ficha = self.__tela_pessoas.selecionar_obj_por_cod('fichas', cod_validos_fichas)
                if identificador_ficha == 0:
                    return False
                else:
                    jogador = self.__jogadores[identificador]
                    if fichas[identificador_ficha].nome in [fic.nome for fic in jogador.personagens]:
                        raise FichaJahExisteException(fichas[identificador_ficha])
                    jogador.add_ficha(fichas[identificador_ficha])
                    self.__tela_pessoas.mensagem('Ficha adicionada!')
                    return True
        except FichaJahExisteException as e:
            self.__tela_pessoas.mensagem(e)
        except KeyError as e:
            self.__tela_pessoas.mensagem(f'[ERRO DE CHAVE] Algum elemento não foi encontrado: {e}')
        except Exception as e:
            self.__tela_pessoas.mensagem(f'[ERRO INESPERADO] Erro ao adicionar ficha em jogador: {e}')

    def remove_ficha(self):
        try:
            self.listar_jogador()
            cod_validos = list(self.__jogadores.keys()) + [0]
            identificador = self.__tela_pessoas.selecionar_obj_por_cod('jogadores', cod_validos)
            jogador = self.__jogadores[identificador]
            if identificador == 0:
                return False
            else:
                fichas = self.__controlador_sistema.controlador_fichas.dict_fichas
                self.__controlador_sistema.controlador_fichas.listar_fichas(selecao=False)
                cod_validos_fichas = list(fichas.keys()) + [0]
                identificador_ficha = self.__tela_pessoas.selecionar_obj_por_cod('fichas', cod_validos_fichas)
                if identificador_ficha == 0:
                    return False
                else:
                    jogador.rm_ficha(fichas[identificador_ficha])
                    self.__tela_pessoas.mensagem('Ficha Removida!')
                    return True
                
        except KeyError as e:
            self.__tela_pessoas.mensagem(f'[ERRO DE CHAVE] Elemento não excluido, código não encontado.: {e}')
        except Exception as e:
            self.tela_pessoas.mensagem(f'[ERRO INESPERADO] Erro ao remover ficha {e}')   

    def acessar_mestre(self, alterar=False):
        try:
            infos_mestre = {
                'cod': 0,
                'nome': self.__mestre.nome,
                'cidade': self.__mestre.endereco.cidade,
                'bairro': self.__mestre.endereco.bairro,
                'numero': self.__mestre.endereco.numero,
                'cep': self.__mestre.endereco.cep,
                'telefone': self.__mestre.telefone
            }
            self.__tela_pessoas.mensagem(
                f'{"Cod":^4} | {"Nome":^16} | {"Telefone":^13} | {"Cidade":^16} | {"Bairro":^12} | {"Numero":^6} | {"Cep":^10} |')
            self.__tela_pessoas.mostra_pessoa(infos_mestre)
            self.__tela_pessoas.mensagem('')
            alterar = self.__tela_pessoas.le_int_ou_float('Deseja alterar mestre? Sim(1), Não(0): ', conjunto_alvo=[0, 1])
            if alterar:
                dados_novos = self.__tela_pessoas.pegar_dados_pessoa()
                self.__mestre = Mestre(
                    dados_novos['nome'],
                    dados_novos['telefone'],
                    dados_novos['cidade'],
                    dados_novos['bairro'],
                    dados_novos['numero'],
                    dados_novos['cep']
                    )
                self.__tela_pessoas.mensagem('Mestre alterado com sucesso!')
                return True
            else:
                return False
        except Exception as e:
            self.tela_pessoas.mensagem(f'[ERRO INESPERADO] Erro ao alterar mestre: {e}')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.incluir_jogador,
            2: self.excluir_jogador,
            3: self.listar_jogador,
            4: self.alterar_jogador_por_cod,
            5: self.add_ficha,
            6: self.remove_ficha,
            7: self.acessar_mestre,
            0: self.retornar
        }
        while True:
            opc = self.__tela_pessoas.mostra_tela()
            metodo = opcoes[opc]
            metodo()

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
    
    @property
    def tela_pessoas(self):
        return self.__tela_pessoas
    
    @property
    def jogadores(self):
        return self.__jogadores

    @property
    def mestre(self):
        return self.__mestre
