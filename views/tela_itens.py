from views.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaItens(TelaAbstrata):
    def __init__(self, nome_objeto='Item'):
        super().__init__(nome_objeto)

    def mostra_tela(self, nome_objeto = 'Item', layout_extra = None, indice_layout_extra = 0, crud=True):
        return super().mostra_tela(nome_objeto, layout_extra, indice_layout_extra, crud)

    def exibir_tabela(self, cabecalho, dados, nome_objeto='Item'):
        return super().exibir_tabela(cabecalho, dados, nome_objeto)

    def pegar_dados_item(self):
        layout = [
            [sg.Text('Dados Item', font=('Helvica', 25))],
            [sg.Text('Nome', size=(15, 1)), sg.InputText('', key='nome', enable_events=True)],
            [sg.Text('Raridade: ', size=(15, 1)),
            sg.InputCombo(('comum', 'incomum', 'raro', 'épico', 'lendário'),
                        size=(20, 1), readonly=True, enable_events=True, key='raridade')],
            [sg.Text('Pagina', size=(15, 1)),
            sg.Combo(values=[i for i in range(1, 385)], enable_events=True, readonly=True, key='pagina')],
            [sg.Text('Valor', size=(15, 1)), sg.InputText('', enable_events=True, key='valor')],
            [sg.Submit('Confirmar', disabled=True), sg.Cancel('Cancelar')]
        ]

        super().init_components('Novo Item', layout_extra=layout, crud=False)

        while True:
            button, values = self.open()

            if button in (sg.WIN_CLOSED, 'Confirmar'):
                self.close()
                values['nome'] = values['nome'].title().strip()
                values['raridade'] = values['raridade'].title().strip()
                values['valor'] = int(values['valor'])
                return values

            elif button == 'Cancelar':
                self.close()
                return 0

            check_nome = values['nome'].strip() != ''
            check_raridade = values['raridade'].strip() != ''
            check_pagina = values['pagina'] != ''
            check_valor = values['valor'] != ''

            if all([check_nome, check_raridade, check_pagina, check_valor]):
                self.window['Confirmar'].update(disabled=False)
            else:
                self.window['Confirmar'].update(disabled=True)
