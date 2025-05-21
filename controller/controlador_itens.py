from views.tela_itens import TelaItens
from model.item import Item
from model.exceptions.exception_itens import *
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller.controlador_sistema import ControladorSistema


class ControladorItens:
    def __init__(self, controlador_sistema: "ControladorSistema"):
        self.__controlador_sistema = controlador_sistema
        self.__dict_item: dict[int, Item] = dict()
        self.__tela_itens = TelaItens()
        self.__cod = 1

    def pega_item_por_nome(self, nome: str):
        for item in self.__dict_item.values():
            if item.nome == nome:
                return item
        return None

    def incluir_item(self):
        try:
            dados_item = self.__tela_itens.pegar_dados_item()
            i = self.pega_item_por_nome(dados_item['nome'])
            if i:
                raise ItemJahExisteException()
            else:
                item = Item(
                            dados_item['nome'],
                            dados_item['valor'],
                            dados_item['raridade'],
                            dados_item['pagina']
                            )
                self.__dict_item[self.__cod] = item
                self.__cod += 1
                self.__tela_itens.mensagem('Item criado com sucesso!')

        except ItemJahExisteException as e:
            self.__tela_itens.mensagem(e)
        except KeyError as e:
            self.__tela_itens.mensagem(f"[ERRO] Dado ausente: {str(e)}")
        except Exception as e:
            self.__tela_itens.mensagem(f"[ERRO INESPERADO] Ocorreu um erro inesperado: {str(e)}")

    def listar_itens(self):
        try:
            self.__tela_itens.mensagem(f'{"Cod":^4} | {"Nome":^16} | {"Raridade":^10} | {"Pag":^5} | {"Valor":^9}')
            for key, item in self.__dict_item.items():
                self.__tela_itens.mostra_item(
                    {
                        'cod': key,
                        'nome': item.nome,
                        'raridade': item.raridade,
                        'pagina': item.pagina,
                        'valor': item.valor
                    }
                )

        except Exception as e:
            self.__tela_itens.mensagem(f"Ocorreu um erro ao listar os itens: {str(e)}")

    def excluir_item(self):
        self.listar_itens()
        try:
            cod_validos = list(self.__dict_item.keys()) + [0]
            identificador = self.__tela_itens.selecionar_obj_por_cod('item', cod_validos)
            if identificador == 0:
                return False

            del self.__dict_item[identificador]
            self.__tela_itens.mensagem('Item removido!')
            return True

        except Exception as e:
            self.__tela_itens.mensagem(f'[ERRO INESPERADO] Ocorreu um erro inesperado: {str(e)}')

    def alterar_item_por_cod(self):
        self.listar_itens()
        try:
            cod_validos = list(self.__dict_item.keys()) + [0]
            identificador = self.__tela_itens.selecionar_obj_por_cod('item', cod_validos)
            if identificador == 0: 
                return

            item = self.__dict_item[identificador]
            dados_novos = self.__tela_itens.pegar_dados_item()

            item.nome = dados_novos['nome']
            item.raridade = dados_novos['raridade']
            item.pagina = dados_novos['pagina']
            item.valor = dados_novos['valor']
            self.__tela_itens.mensagem('Item alterado com sucesso!')

        except KeyError as e:
            self.__tela_itens.mensagem(f"[ERRO] Dado ausente: {str(e)}")
        except Exception as e:
            self.__tela_itens.mensagem(f'[ERRO INESPERADO] Erro inesperado ao alterar item por código: {str(e)}')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.incluir_item,
            2: self.excluir_item,
            3: self.listar_itens,
            4: self.alterar_item_por_cod,
            0: self.retornar
        }
        while True:
            opc = self.__tela_itens.mostra_tela()
            metodo = opcoes[opc]
            metodo()

    @property
    def tela_itens(self):
        return self.__tela_itens

    @property
    def dict_item(self):
        return self.__dict_item

    @property
    def cod(self):
        return self.__cod
