from views.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaMagias(TelaAbstrata):
    def __init__(self, nome_objeto='Magia'):
        super().__init__(nome_objeto)

    def mostra_tela(self, nome_objeto = 'Magia', layout_extra = None, indice_layout_extra = 0, crud=True):
        return super().mostra_tela(nome_objeto, layout_extra, indice_layout_extra, crud)

    def exibir_tabela(self, cabecalho, dados, nome_objeto='Magia'):
        return super().exibir_tabela(cabecalho, dados, nome_objeto)

    def pegar_dados_magia(self):
        layout = [
            [sg.Text('Dados Magia', font = ('Helvica', 25))],
            [sg.Text('Nome', size=(15, 1)), sg.InputText('', key='nome', enable_events=True)],
            [sg.Text('Nivel', size = (15, 1)), sg.Combo(values=([i for i in range(1, 21)]), enable_events=True, readonly=True, key='nivel')],
            [sg.Text('Pagina', size = (15, 1)), sg.Combo(values=([i for i in range(1, 385)]), enable_events=True, readonly=True, key='pagina')],
            [sg.Submit('Confirmar', disabled=True), sg.Cancel('Cancelar')]
        ]
        self.init_components('Nova Magia', layout, crud=False)
        while True:
            button, values = self.open()
            if button in (sg.WIN_CLOSED, "Cancelar", 'Confirmar'):
                break
            check_nome = values['nome'].strip() != ''
            check_nivel = values['nivel'] != ''
            check_pagina = values['pagina'] != ''
            if all([check_nome, check_nivel, check_pagina]):
                self.window['Confirmar'].update(disabled=False)
            else:
                self.window['Confirmar'].update(disabled=True)
            values['nome'] = values['nome'].title().strip()      
        self.close()
        if button == 'Confirmar':
            return values
        else:
            return False
