from views.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaClasses(TelaAbstrata):
    def __init__(self, nome_objeto='classe'):
        super().__init__(nome_objeto)

    def mostra_tela(self, nome_objeto = '', layout_extra = None, indice_layout_extra = 0, crud=False):
        layout = [
            [sg.Text(f'Gerenciador de Especies e Subespecies', font = ('Arial', 25))],
            [sg.Text('Escolha uma opção', font=('Arial', 15))],
            [sg.Radio(f'Incluir Classe', 'RD1', enable_events=True, key = '1')],
            [sg.Radio(f'Excluir Classe ', 'RD1', enable_events=True, key = '2')],
            [sg.Radio(f'Listar Classe', 'RD1', enable_events=True, key = '3')],
            [sg.Radio(f'Alterar Classe', 'RD1', enable_events=True, key = '4')],
            [sg.Radio(f'Listar Subclasse', 'RD1', enable_events=True, key = '9')],
            [sg.Radio(f'Incluir Habilidade em Classe', 'RD1', enable_events=True, key = '5')],
            [sg.Radio(f'Excluir Habilidade de Classe', 'RD1', enable_events=True, key = '6')],
            [sg.Radio(f'Incluir Habilidade em Subclasse', 'RD1', enable_events=True, key = '7')],
            [sg.Radio(f'Excluir Habilidade de Subclasse', 'RD1', enable_events=True, key = '8')],
            [sg.Radio('Retornar', "RD1", enable_events=True, key = '0')],
            [sg.Button('Confirmar', disabled=True), sg.Cancel('Cancelar')]
        ]
        return super().mostra_tela(nome_objeto, layout, indice_layout_extra, crud=False)
    
    def exibir_tabela(self, cabecalho, dados, nome_objeto='Classe'):
        return super().exibir_tabela(cabecalho, dados, nome_objeto)
    
    def pegar_dados_classes(self):
        layout = [
            [sg.Text('Dados Classe', font = ('Helvica', 25))],
            [sg.Text('Nome', size = (15, 1)), sg.InputText('', key='nome', enable_events=True)],
            [sg.Text('Dado de vida', size=(15, 1)),
            sg.Combo(values=[i for i in range(4, 13, 2)], enable_events=True, readonly=True, key='dado')],
            [sg.Text('1ª Opção Subclasse', size = (15, 1)), sg.InputText('', key='nome_sub1', enable_events=True)],
            [sg.Text('2ª Opção Subclasse', size = (15, 1)), sg.InputText('', key='nome_sub2', enable_events=True)],
            [sg.Text('3ª Opção Subclasse', size = (15, 1)), sg.InputText('', key='nome_sub3', enable_events=True)],
            [sg.Submit('Confirmar', disabled=True), sg.Cancel('Cancelar')]
            ]
        
        self.init_components('Nova classe', layout, crud=False)

        while True:
            button, values = self.open()

            if button in (sg.WIN_CLOSED, 'Cancelar'):
                self.close()
                return 0
            elif button == 'Confirmar':
                self.close()
                values['nome'] = values['nome'].strip().title()
                dados = {
                    'nome': values['nome'],
                    'dado': values['dado'],
                    'nomes_sub': [values['nome_sub1'], values['nome_sub2'], values['nome_sub3']]
                }
                return dados
            
            check_nome = values['nome'].title().strip() != ''
            check_dado = str(values['dado']) != ''
            check_nome_sub1 = values['nome_sub1'].title().strip() != ''
            check_nome_sub2 = values['nome_sub2'].title().strip() != ''
            check_nome_sub3 = values['nome_sub3'].title().strip() != ''
            

            if all([check_nome, check_dado, check_nome_sub1, check_nome_sub2, check_nome_sub3]):
                self.window['Confirmar'].update(disabled=False)
            else:
                self.window['Confirmar'].update(disabled=True)

    def ler_subclasse(self):
        layout = [
            [sg.Text("Escolher Subclasse", font=('Arial', 20))],
            [sg.Text('Subclasses:', size=(15, 1)),
            sg.Combo(values=[a for a in range(1, 4)], key="cod_subclasse", readonly=True)],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]

        self.init_components('Nova subclasse', layout, crud=False)

        while True:
            button, values = self.open()

            if button in (sg.WIN_CLOSED, 'Confirmar'):
                self.close()
                return values['cod_subclasse']
            elif button == 'Cancelar':
                self.close()
                return 0
