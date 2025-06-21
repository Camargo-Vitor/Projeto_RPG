from views.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaItens(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
       sg.change_look_and_feel('Black')
       layout = [
           [sg.Text('===== Item =====', font = ('Arial', 25))],
           [sg.Text('Escolha uma opção', font=('Arial', 15))],
           [sg.Radio(f'Incluir Item', 'RD1', key = '1')],
           [sg.Radio(f'Excluir Item', 'RD1', key = '2')],
           [sg.Radio(f'Listar Item', 'RD1', key = '3')],
           [sg.Radio(f'Alterar Item', 'RD1', key = '4')],
           [sg.Radio('Retornar', "RD1", key = '0')],
           [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
       self.__window = sg.Window('Sistema de Gerenciamento de aventura de D&D').Layout(layout)

    def mostra_tela(self, opcoes=[]):
        self.init_components()
        button, values = self.__window.Read()
        for key, opc in values.items():
            if opc:
                opcoes = int(key)
        if values['0'] or button in (None,'Cancelar'):
            opcoes = 0
        self.close()
        return opcoes

    def pegar_dados_item(self):
        sg.change_look_and_feel('DarkBrown4')
        layout = [
            [sg.Text('Dados Itens', font = ('Helvica', 25))],
            [sg.Text('Nome:', size = (15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Raridade:', size = (15, 1)), sg.InputText('', key='raridade')],
            [sg.Text('Pagina:', size = (15, 1)), sg.InputText('', key='pagina')],
            [sg.Text('Valor:', size = (15, 1)), sg.InputText('', key='valor')],
            [sg.Submit('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Novo Itemm').Layout(layout)
        button, values = self.open()
        try:
            values['pagina'] = int(values['pagina'])
            values['valor'] = int(values['valor'])
        except:
            self.close()
            return -1            
        self.close()
        return values
    
    def exibir_tabela(self, cabecalho: list, dados: list[list]):
        layout = [
            [sg.Text("Lista de Magias", font=("Arial", 16))],
            [sg.Table(values=dados,
                      headings=cabecalho,
                      auto_size_columns=True,
                      display_row_numbers=False,
                      justification='center',
                      num_rows=min(10, len(dados)),
                      key='-TABELA-')],
            [sg.Button("OK")]
        ]
        window = sg.Window("Itens Cadastrados", layout)
        button, _ = window.read()
        window.close()
        
    def mostra_item(self, dados_item: dict):
        string_todos_itens = ""
        for dado in dados_item:
            string_todos_itens = string_todos_itens + "NOME DO ITEM: " + dado["nome"] + '\n'
            string_todos_itens = string_todos_itens + "RARIDADE DO ITEM: " + str(dado["raridade"]) + '\n'
            string_todos_itens = string_todos_itens + "PAGINA DO ITEM: " + str(dado["pagina"]) + '\n'            
            string_todos_itens = string_todos_itens + "VALOR DO ITEM: " + str(dado["valor"]) + '\n\n'

        sg.Popup('-------- LISTA DE AMIGOS ----------', string_todos_itens)
    
    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
