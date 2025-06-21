from views.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaItens(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_components()

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def init_components(self):
       sg.change_look_and_feel('DarkBrown4')
       layout = [
           [sg.Text('Gerenciador de Itens', font = ('Arial', 25))],
           [sg.Text('Escolha uma opção', font=('Arial', 15))],
           [sg.Radio(f'Incluir Item', 'RD1', key = '1')],
           [sg.Radio(f'Excluir Item', 'RD1', key = '2')],
           [sg.Radio(f'Listar Item', 'RD1', key = '3')],
           [sg.Radio(f'Alterar Item', 'RD1', key = '4')],
           [sg.Radio('Retornar', "RD1", key = '0')],
           [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
       self.__window = sg.Window('Gerenciador de Itens').Layout(layout)

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
        layout = [
            [sg.Text('Dados Itens', font = ('Helvica', 25))],
            [sg.Text('Nome:', size = (15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Raridade:', size = (15, 1)), sg.InputText('', key='raridade')],
            [sg.Text('Pagina:', size = (15, 1)), sg.InputText('', key='pagina')],
            [sg.Text('Valor:', size = (15, 1)), sg.InputText('', key='valor')],
            [sg.Submit('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Novo Item!').Layout(layout)
        button, values = self.open()
        try:
            values['nome'] = values['nome'].title().strip()
            values['raridade'] = values['raridade'].title().strip()
            values['pagina'] = int(values['pagina'])
            values['valor'] = int(values['valor'])
        except:
            self.close()
            return -1            
        self.close()
        return values
    
    def exibir_tabela(self, cabecalho: list, dados: list[list]):
        layout = [
            [sg.Text("Lista de Itens", font=("Arial", 16))],
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

    def selecionar_obj_por_cod(self, obj: str, total_codigos: list):
        layout = [
            [sg.Text('Digite o ID da magia desejada: ')],
            [sg.Text('ID: ', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Submit('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleção de Magia').Layout(layout)
        button, values = self.__window.Read()
        try:
            values['codigo'] = int(values['codigo'])
            if values['codigo'] not in total_codigos:
                raise Exception()
        except Exception as e:
            print(f'[ERRO INESPERADO] Erro ao selecionar entidade por código: {e}')
            self.close()
            return -1
        self.close()
        return values['codigo']
        

