from views.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaHabilidades(TelaAbstrata):
    def __init__(self, nome_objeto='Habilidade'):
        super().__init__(nome_objeto)

    def mostra_tela(self, nome_objeto = 'Habilidade', layout_extra = None, indice_layout_extra = 0, crud=True):
        return super().mostra_tela(nome_objeto, layout_extra, indice_layout_extra, crud)

    def exibir_tabela(self, cabecalho, dados, nome_objeto='Habilidade'):
        return super().exibir_tabela(cabecalho, dados, nome_objeto)
    
    def pegar_dados_habilidade(self):
        layout = [
            [sg.Text('Dados Habilidade')],
            [sg.Text('Nome', size=(15, 1)), sg.InputText('', key='nome', enable_events=True)],
            [sg.Text('Nivel', size = (15, 1)), sg.Combo(values=([i for i in range(1, 21)]), enable_events=True, readonly=True, key='nivel')],
            [sg.Text('Pagina', size = (15, 1)), sg.Combo(values=([i for i in range(1, 385)]), enable_events=True, readonly=True, key='pagina')],
            [sg.Text('Origem', size = (15, 1)), sg.InputCombo(('classe', 'subclasse', 'especie', 'subespecie'), size=(20, 1), readonly=True, key='origem', enable_events=True)],
            [sg.Submit('Confirmar', disabled=True), sg.Cancel('Cancelar')]
        ]

        super().init_components('Nova Habilidade', layout, crud=False)
        while True:
            button, values = self.open()
            if button in (sg.WIN_CLOSED, 'Cancelar'):
                self.close()
                return 0
            elif button == 'Confirmar':
                self.close()
                values['nome'] = values['nome'].title().strip()
                return values
            check_nome = values['nome'].title().strip() != ''
            check_nivel = values['nivel'] != ''
            check_pagina = values['pagina'] != ''
            check_origem = values['origem'].title().strip() != ''
            if all([check_nome, check_nivel, check_pagina, check_origem]):
                self.window['Confirmar'].update(disabled=False)
            else:
                self.window['Confirmar'].update(disabled=True)
