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
        self.__jogadores: dict[int, Jogador] = {
            1000: Jogador('João', 92222222221, 'americana', 'americos', 231, 87312432),
            1001: Jogador('Victor', 4896703241, 'Florianópolis', 'centro', 261, 88031483),
            1002: Jogador('Elias', 25123456789, 'joinville', 'cinza', 981, 86135098),
            1003: Jogador('Sofia', 21849021435, 'jaraguá', 'amizade', 784, 98099876)}
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
                self.__jogadores[self.__cod] = jogador
                self.__cod +=1
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
            for cod, jogador in self.__jogadores.items():
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
        except Exception as e:
            self.__tela_pessoas.mensagem(f'[ERRO INESPERADO] Erro ao listar os jogadores: {str(e)}')

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
        except TypeError as e:
            self.__tela_pessoas.mensagem(f'[ERRO] Algum valor de entrada não foi inserido como esperado.')
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
                        raise FichaJahExisteException(fichas[identificador_ficha].nome)
                    jogador.add_ficha(fichas[identificador_ficha])
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
            cod_validos = list(self.__jogadores.keys()) + [0]
            identificador = self.__tela_pessoas.selecionar_obj_por_cod('jogadores', cod_validos)
            if identificador == 0:
                return False
            else:
                jogador = self.__jogadores[identificador]
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
        except TypeError as e:
            self.__tela_pessoas.mensagem(f'[ERRO] Algum valor de entrada não foi inserido como esperado.')
        except KeyError as e:
            self.__tela_pessoas.mensagem(f'[ERRO DE CHAVE] Elemento não excluido, código não encontado.: {e}')
        except Exception as e:
            self.__tela_pessoas.mensagem(f'[ERRO INESPERADO] Erro ao remover ficha {e}')   

    def acessar_mestre(self, alterar=False):
        try:
            if alterar:
                # Tela retorna apenas os dados preenchidos, como dicionário
                dados_novos = self.__tela_pessoas.exibir_mestre(self.__mestre)

                if dados_novos:
                    self.__mestre = Mestre(
                        nome=dados_novos["nome"],
                        telefone=dados_novos["telefone"],
                        cidade=dados_novos["cidade"],
                        bairro=dados_novos["bairro"],
                        numero=dados_novos["numero"],
                        cep=dados_novos["cep"]
                    )
                    self.__tela_pessoas.mensagem("Mestre alterado com sucesso!")
                    return True
                else:
                    return False
            else:
                return False
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
    
    @property
    def jogadores(self):
        return self.__jogadores

    @property
    def mestre(self):
        return self.__mestre
