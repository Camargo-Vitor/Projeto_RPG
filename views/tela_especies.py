from views.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaEspecies(TelaAbstrata):
    def __init__(self, nome_objeto='Especie'):
        super().__init__(nome_objeto)

    def mostra_tela(self, nome_objeto = '', layout_extra = None, indice_layout_extra = 0, crud=False):
        layout = [
            [sg.Text(f'Gerenciador de Especies e Subespecies', font = ('Arial', 25))],
            [sg.Text('Escolha uma opção', font=('Arial', 15))],
            [sg.Radio(f'Incluir Especie', 'RD1', enable_events=True, key = '1')],
            [sg.Radio(f'Excluir Especie ', 'RD1', enable_events=True, key = '2')],
            [sg.Radio(f'Listar Especie', 'RD1', enable_events=True, key = '3')],
            [sg.Radio(f'Alterar Especie', 'RD1', enable_events=True, key = '4')],
            [sg.Radio(f'Incluir Habilidade em Especie', 'RD1', enable_events=True, key = '5')],
            [sg.Radio(f'Excluir Habilidade de Especie', 'RD1', enable_events=True, key = '6')],
            [sg.Radio(f'Incluir Subespecie', 'RD1', enable_events=True, key = '7')],
            [sg.Radio(f'Excluir Subespecie', 'RD1', enable_events=True, key = '8')],
            [sg.Radio(f'Listar Subespecie', 'RD1', enable_events=True, key = '9')],
            [sg.Radio(f'Alterar Subespecie', 'RD1', enable_events=True, key = '10')],
            [sg.Radio(f'Incluir Habilidade em Subespecie', 'RD1', enable_events=True, key = '11')],
            [sg.Radio(f'Excluir Habilidade de Subespecie', 'RD1', enable_events=True, key = '12')],
            [sg.Radio('Retornar', "RD1", enable_events=True, key = '0')],
            [sg.Button('Confirmar', disabled=True), sg.Cancel('Cancelar')]
        ]
        return super().mostra_tela(nome_objeto, layout, indice_layout_extra, crud=False)

    def exibir_tabela(self, cabecalho, dados, nome_objeto='Especie'):
        return super().exibir_tabela(cabecalho, dados, nome_objeto)

    def pegar_dados_especie(self):
        layout = [
            [sg.Text('Dados Especie', font = ('Helvica', 25))],
            [sg.Text('Nome', size = (15, 1)), sg.InputText('', key='nome', enable_events=True)],
            [sg.Text('Deslocamento', size=(15, 1)),
            sg.Combo(values=[i/10 for i in range(60, 600, 15)], enable_events=True, readonly=True, key='deslocamento')],
            [sg.Text('Altura (cm)', size = (15, 1)), 
            sg.Slider(range = (60, 240), default_value= 85, orientation= 'h', key='altura')],
            [sg.Submit('Confirmar', disabled=True), sg.Cancel('Cancelar')]
        ]

        self.init_components('Nova especie', layout, crud=False)

        while True:
            button, values = self.open()

            if button in (sg.WIN_CLOSED, 'Confirmar'):
                self.close()
                values['nome'] = values['nome'].strip().title()
                values['altura'] = int(values['altura'])
                return values
            elif button == 'Cancelar':
                self.close()
                return 0
            
            check_nome = values['nome'].strip() != ''
            check_deslocamento = values['deslocamento'] != ''
            check_altura = values['altura'] != ''
            

            if all([check_nome, check_deslocamento, check_altura]):
                self.window['Confirmar'].update(disabled=False)
            else:
                self.window['Confirmar'].update(disabled=True)

    def pegar_dados_subespecie(self, especie: str):
        layout = [
            [sg.Text('Dados Subespecie', font = ('Helvica', 25))],
            [sg.Text(f'Nome {especie}...', size = (15, 1)), sg.InputText(key='nome', enable_events=True)],
            [sg.Submit('Confirmar', disabled=True), sg.Cancel('Cancelar')]
        ]

        self.init_components('Nova Supespecie', layout, crud=False)

        while True:
            button, values = self.open()

            if button in (sg.WIN_CLOSED, 'Confirmar'):
                self.close()
                values['nome'] = values['nome'].strip().title()
                return values
            elif button == 'Cancelar':
                self.close()
                return 0

            if values['nome'].strip() != '':
                self.window['Confirmar'].update(disabled=False)
            else:
                self.window['Confirmar'].update(disabled=True)
