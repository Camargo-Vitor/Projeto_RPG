from views.tela_pessoas import TelaPessoas
from model.mestre import Mestre
from model.jogador import Jogador
from model.exceptions.exception_pessoas import *
from model.exceptions.exception_dict_vazio import *
from model.exceptions.excpetion_ficha import *
from DAOs.pessoa_dao import PessoaDao
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller.controlador_sistema import ControladorSistema
    


class ControladorPessoas:
    def __init__(self, controlador_sistema: "ControladorSistema"):
        self.__controlador_sistema = controlador_sistema
        self.__tela_pessoas = TelaPessoas()
        self.__pesssoa_dao = PessoaDao()
        if not self.__pesssoa_dao.cache:
            self.__pesssoa_dao.add(Mestre('Nome', 0, 'Cidade', 'Bairro', 0, 0))
    
    def pega_pessoa_por_nome(self, nome: str):
        for pessoa in self.__pesssoa_dao.get_all():
            if pessoa.nome == nome:
                return pessoa
        return None
    
    def incluir_jogador(self):
        try:
            dados_pessoa = self.__tela_pessoas.pegar_dados_pessoa()
            if dados_pessoa == 0:
                return False
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
                self.__pesssoa_dao.add(jogador)
                self.__tela_pessoas.mensagem('Jogador criado com sucesso')
                return True 
        except JogadorJahExisteException as e:
            self.__tela_pessoas.mensagem(e)
        except TypeError as e:
            self.__tela_pessoas.mensagem(f'[ERRO] Algum valor de entrada não foi inserido como esperado.')
        except KeyError as e:
            self.__tela_pessoas.mensagem(f"[ERRO] Dado ausente: {str(e)}")
        except Exception as e:
            self.__tela_pessoas.mensagem(f'[ERRO INESPERADO] Erro ao incluir jogador: {str(e)}')

    def listar_jogador(self):
        try:
            dados = []
            if self.__pesssoa_dao.cache:
                for cod, jogador in self.__pesssoa_dao.cache.items():
                    if isinstance(jogador, Jogador):
                        linha = [
                            cod,
                            jogador.nome,
                            jogador.telefone,
                            jogador.endereco.cidade,
                            jogador.endereco.bairro,
                            jogador.endereco.numero,
                            jogador.endereco.cep,
                            ', '.join(p.nome for p in jogador.personagens)
                        ]
                        dados.append(linha)
                HEADER = ["Cod", "Nome", "Telefone", "Cidade", "Bairro", "Número", "CEP", "Personagens"]
                self.__tela_pessoas.exibir_tabela(cabecalho=HEADER, dados=dados, nome_objeto='Persoangem')
            else:
                raise DictVazioException()
        except DictVazioException as e:
            self.__tela_pessoas.mensagem(e)
        except Exception as e:
            self.__tela_pessoas.mensagem(f'[ERRO INESPERADO] Erro ao listar os jogadores: {str(e)}')

    def excluir_jogador(self):
        try:
            self.listar_jogador()
            cod_validos = list(self.__pesssoa_dao.get_keys()) + [0] - [1]
            identificador = self.__tela_pessoas.selecionar_obj_por_cod('jogador', cod_validos)
            if identificador == 0:
                return False
            else:
                self.__pesssoa_dao.remove(identificador)
                self.__tela_pessoas.mensagem('Jogador Removido')
                return True
        except KeyError as e:
            self.__tela_pessoas.mensagem(f'[ERRO DE CHAVE] Erro ao excluir jogador, código não encontrado: {str(e)}')
        except TypeError as e:
            self.__tela_pessoas.mensagem(f'[ERRO] Algum valor de entrada não foi inserido como esperado.')
        except Exception as e:
            self.__tela_pessoas.mensagem(f'[ERRO INESPERADO] Erro ao excluir jogador: {e}')

    def alterar_jogador_por_cod(self):
        try:
            self.listar_jogador()
            codigo_validos = list(self.__pesssoa_dao.get_keys()) + [0]
            identificador = self.__tela_pessoas.selecionar_obj_por_cod('jogador', codigo_validos)
            if identificador == 0:
                return False
            else:
                jogador = self.__pesssoa_dao.cache[identificador]
                dados_novos = self.__tela_pessoas.pegar_dados_pessoa()
                j = self.pega_pessoa_por_nome(dados_novos['nome'])
                if j is None:
                    jogador.nome = dados_novos['nome']
                    jogador.telefone = dados_novos['telefone']
                    jogador.endereco.cidade = dados_novos['cidade']
                    jogador.endereco.bairro = dados_novos['bairro']
                    jogador.endereco.numero = dados_novos['numero']
                    jogador.endereco.cep = dados_novos['cep']
                    self.__pesssoa_dao.update(identificador, jogador)
                    self.__tela_pessoas.mensagem('Jogador Alterado com sucesso')
                    return True
                else:
                    raise JogadorJahExisteException(dados_novos['nome'])
        except JogadorJahExisteException as e:
            self.__tela_pessoas.mensagem(e)
        except KeyError as e:
            self.__tela_pessoas.mensagem(f'[ERRO DE CHAVE] Dado ausente: {str(e)}')
        except TypeError as e:
            self.__tela_pessoas.mensagem(f'[ERRO] Algum valor de entrada não foi inserido como esperado.')
        except Exception as e:
            self.__tela_pessoas.mensagem(f'[ERRO INESPERADO] Erro ao alterar jogador: {e}')

    def add_ficha(self):
        try:
            self.listar_jogador()
            cod_validos = list(self.__pesssoa_dao.get_keys()) + [0]
            identificador = self.__tela_pessoas.selecionar_obj_por_cod('jogadores', cod_validos)
            if identificador == 0:
                return False
            else:
                fichas = self.__controlador_sistema.controlador_fichas.ficha_dao.cache
                cod_validos_fichas = list(fichas.keys()) + [0]
                self.__controlador_sistema.controlador_fichas.listar_fichas(selecao=False)
                identificador_ficha = self.__tela_pessoas.selecionar_obj_por_cod('fichas', cod_validos_fichas)
                if identificador_ficha == 0:
                    return False
                else:
                    jogador = self.__pesssoa_dao.cache[identificador]
                    if fichas[identificador_ficha].nome in [fic.nome for fic in jogador.personagens]:
                        raise FichaJahExisteException(fichas[identificador_ficha].nome)
                    jogador.add_ficha(fichas[identificador_ficha])
                    self.__pesssoa_dao.update(identificador, jogador)
                    self.__tela_pessoas.mensagem('Ficha adicionada!')
                    return True
        except FichaJahExisteException as e:
            self.__tela_pessoas.mensagem(e)
        except KeyError as e:
            self.__tela_pessoas.mensagem(f'[ERRO DE CHAVE] Algum elemento não foi encontrado: {e}')
        except TypeError as e:
            self.__tela_pessoas.mensagem(f'[ERRO] Algum valor de entrada não foi inserido como esperado.')
        except Exception as e:
            self.__tela_pessoas.mensagem(f'[ERRO INESPERADO] Erro ao adicionar ficha em jogador: {e}')

    def remove_ficha(self):
        try:
            self.listar_jogador()
            cod_validos = list(self.__pesssoa_dao.get_keys()) + [0]
            identificador = self.__tela_pessoas.selecionar_obj_por_cod('jogadores', cod_validos)
            if identificador == 0:
                return False
            else:
                jogador = self.__pesssoa_dao.cache[identificador]
                fichas = self.__controlador_sistema.controlador_fichas.ficha_dao.cache
                self.__controlador_sistema.controlador_fichas.listar_fichas(selecao=False)
                cod_validos_fichas = list(fichas.keys()) + [0]
                identificador_ficha = self.__tela_pessoas.selecionar_obj_por_cod('fichas', cod_validos_fichas)
                if identificador_ficha == 0:
                    return False
                else:
                    jogador.rm_ficha(fichas[identificador_ficha])
                    self.__pesssoa_dao.update(identificador, jogador)
                    self.__tela_pessoas.mensagem('Ficha Removida!')
                    return True
        except TypeError as e:
            self.__tela_pessoas.mensagem(f'[ERRO] Algum valor de entrada não foi inserido como esperado.')
        except KeyError as e:
            self.__tela_pessoas.mensagem(f'[ERRO DE CHAVE] Elemento não excluido, código não encontado.: {e}')
        except Exception as e:
            self.__tela_pessoas.mensagem(f'[ERRO INESPERADO] Erro ao remover ficha {e}')   

    def acessar_mestre(self):
        try:
            mestre:Mestre = self.__pesssoa_dao.get(1)
            dados_mestre = {
                'nome': mestre.nome,
                'telefone': mestre.telefone,
                'cidade': mestre.endereco.cidade,
                'bairro': mestre.endereco.bairro,
                'numero': mestre.endereco.numero,
                'cep': mestre.endereco.cep
            }
            dados_novos = self.__tela_pessoas.exibir_mestre(dados_mestre)
            if dados_novos == 0:
                return False
            else:
                novo_mestre = Mestre(
                    nome=dados_novos["nome"],
                    telefone=dados_novos["telefone"],
                    cidade=dados_novos["cidade"],
                    bairro=dados_novos["bairro"],
                    numero=dados_novos["numero"],
                    cep=dados_novos["cep"]
                )
                self.__pesssoa_dao.update(1, novo_mestre)
                self.__tela_pessoas.mensagem("Mestre alterado com sucesso!")
                return True
        except Exception as e:
            self.__tela_pessoas.mensagem(f"[ERRO INESPERADO] Erro ao acessar mestre: {e}")

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