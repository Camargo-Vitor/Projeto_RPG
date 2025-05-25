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
        self.__pessoas: dict[int, Jogador] = dict()
        self.__cod = 1
    
    def pega_pessoa_por_nome(self, nome: str):
        for pessoa in self.__pessoas.values():
            if pessoa.nome == nome:
                return pessoa
            return None
    
    def incluir_jogador(self):
        dados_pessoa = self.__tela_pessoas.pegar_dados_pessoa()
        m = self.pega_pessoa_por_nome(dados_pessoa['nome'])
        if m is None:
            jogador = Jogador(
                dados_pessoa['nome'],
                dados_pessoa['telefone'],
                dados_pessoa['cidade'],
                dados_pessoa['bairro'],
                dados_pessoa['numero'],
                dados_pessoa['cep'],
            )
            self.__pessoas[self.__cod] = jogador
            self.__cod +=1
            self.__tela_pessoas.mensagem('Jogador criado com sucesso')
        else:
            self.__tela_pessoas.mensagem('Esse jogador já existe')

    def listar_jogador(self):
        self.__tela_pessoas.mensagem(f'{"Cod":^4} | {"Nome":^16} | {"Telefone":^13} | {"Cidade":^16} | {"Bairro":^12} | {"Numero":^6} | {"Cep":^10} | {"Personagens":^12}')
        for cod, pessoa in self.__pessoas.items():
            self.__tela_pessoas.mostra_jogador(
                {
                'cod': cod,
                'nome': pessoa.nome,
                'telefone': pessoa.telefone,
                'cidade': pessoa.endereco.cidade,
                'bairro': pessoa.endereco.bairro,
                'numero': pessoa.endereco.numero,
                'cep': pessoa.endereco.cep,
                'personagens': pessoa.personagens
            }
            )
    def excluir_jogador(self):
        try:
            self.listar_jogador()
            cod_validos = list(self.__pessoas.keys()) + [0]
            identificador = self.__tela_pessoas.selecionar_obj_por_cod('jogador', cod_validos)
            if identificador == 0:
                return False
            else:
                del self.__pessoas[identificador]
                self.__tela_pessoas.mensagem('Jogador Removido')
                return True
        except Exception as e:
            self.__tela_pessoas.mensagem(f'[ERRO INESPERADO] Erro ao excluir classe: {e}')

    def alterar_jogador_por_cod(self):
        try:
            self.listar_jogador()
            codigo_validos = list(self.__pessoas.keys()) + [0]
            identificador = self.__tela_pessoas.le_int_ou_float(
                'Digite o código da jogador: (0 para cancelar) ',
                conjunto_alvo=codigo_validos
            )
            if identificador == 0:
                return False
            else:
                jogador = self.__pessoas[identificador]
                novos_dados = self.__tela_pessoas.pegar_dados_pessoa()
                jogador.nome = novos_dados['nome']
                jogador.telefone = novos_dados['telefone']
                jogador.endereco.cidade = novos_dados['cidade']
                jogador.endereco.bairro = novos_dados['bairro']
                jogador.endereco.numero = novos_dados['numero']
                jogador.endereco.cep = novos_dados['cep']
        except Exception as e:
            self.__tela_pessoas.mensagem(f'[ERRO INESPERADO] Erro ao modificar dados base de classe: {e}')

    def add_ficha(self):
        try:
            self.listar_jogador()
            cod_validos = list(self.__pessoas.keys()) + [0]
            identificador = self.__tela_pessoas.selecionar_obj_por_cod('jogadores',cod_validos)
            if identificador == 0:
                return False
            else:
                fichas = self.__controlador_sistema.controlador_fichas.dict_fichas
                self.__controlador_sistema.controlador_fichas.listar_fichas()
                cod_validos_fichas = list(fichas.keys()) + [0]
                identificador_ficha = self.__tela_pessoas.selecionar_obj_por_cod('fichas', cod_validos_fichas)
                if identificador_ficha == 0:
                    return
                else:
                    pessoa = self.__pessoas[identificador]
                    pessoa.add_ficha(fichas[identificador_ficha])
                    return True
        except KeyError as e:
            self.__tela_pessoas.mensagem(f'[ERRO DE CHAVE] Algum elemento não foi encontrado: {e}')
        except Exception as e:
            self.__tela_pessoas.mensagem(f'[ERRO INESPERADO] Erro ao adicionar ficha para jogador: {e}')

    def remove_ficha(self):
        try:
            self.listar_jogador()
            cod_validos = list(self.__pessoas.keys()) + [0]
            identificador = self.__tela_pessoas.selecionar_obj_por_cod('jogadores',cod_validos)
            jogador = self.__pessoas[identificador]
            if identificador == 0:
                return False
            else:
                fichas = self.__controlador_sistema.controlador_fichas.dict_fichas
                self.__controlador_sistema.controlador_fichas.listar_fichas('fichas')
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
            self.tela_pessoas.mensagem(f'[ERRO INESPERADO] Erro ao adicionar habilidade em espécie: {e}')   

    def alterar_mestre(self):
        pass

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
            7: self.alterar_mestre,
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
    def dict_pessoas(self):
        return self.__pessoas
