from views.tela_item import TelaItem
from model.item import Item

class ControladorItem:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__lista_item = []
        self.__tela_item = TelaItem()
        self.__cod = 1
    
    def pega_item_por_nome(self, nome: str):
        for item in self.__lista_item:
            if item.nome == nome:
                return item
        return None

    def incluir_item(self):
        dados_item = self.__tela_item.pegar_dados_item()
        i = self.pega_item_por_nome(dados_item['nome'])
        if i is None:
            item = Item(self.__cod, dados_item['nome'], dados_item['valor'], dados_item['raridade'], dados_item['pagina'])
            self.__cod += 1
            self.__lista_item.append(item)
            self.__tela_item.mensagem('Item criado com sucesso!')
        else:
            self.__tela_item.mensagem('ATENÇÃO: O item já existe')

    def excluir_item(self):
        try:
            identificador = int(self.tela_item.selecionar_item_por_id())
            for item in self.__lista_item:
                if item.id == identificador:
                    self.__lista_item.remove(item)
                    self.tela_item.mensagem('Item removido!')
                    return True
                else:
                    return False
        except:
            return False

    def listar_itens(self):
        self.tela_item.mensagem('Id | Nome | Raridade | Pagina | Valor')
        for item in self.__lista_item:
            self.tela_item.mostra_item(
                {
                    'id': item.id,
                    'nome': item.nome,
                    'raridade': item.raridade,
                    'pagina': item.pagina,
                    'valor': item.valor
                }
            )
    def abre_tela(self):
        opcoes = {
            1: self.incluir_item,
            2: self.excluir_item,
            3: self.listar_itens
        }
        while True:
            opc = self.__tela_item.mostra_tela()
            metodo = opcoes[opc]
            metodo()

    @property
    def tela_item(self):
        return self.__tela_item
    
    @property
    def lista_item(self):
        return self.__lista_item
