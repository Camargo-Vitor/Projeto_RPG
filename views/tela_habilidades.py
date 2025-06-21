from views.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaHabilidades(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_components('Habilidade')

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def init_components(self, nome_objeto):
        return super().init_components(nome_objeto)

    def mostra_tela(self, nome_objeto = 'Habilidade'):
        return super().mostra_tela(nome_objeto=nome_objeto)

    def pegar_dados_habilidade(self):
        layout = [
            [sg.Text('Dados Habilidade')],
            [sg.Text('Nome', size=(15, 1)), sg.InputText('', key='nome', enable_events=True)],
            [sg.Text('Nivel', size = (15, 1)), sg.Combo(values=([i for i in range(1, 21)]), enable_events=True, readonly=True, key='nivel')],
            [sg.Text('Pagina', size = (15, 1)), sg.Combo(values=([i for i in range(1, 385)]), enable_events=True, readonly=True, key='pagina')],
            [sg.Text('Origem', size = (15, 1)), sg.InputCombo(('classe', 'subclasse', 'especie', 'subespecie'), size=(20, 1), readonly=True, key='origem', enable_events=True)],
            [sg.Submit('Confirmar', disabled=True), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Dados Habilidade').Layout(layout)
        while True:
            button, values = self.__window.read()
            if button in (sg.WIN_CLOSED, "Cancelar", 'Confirmar'):
                break
            check_nome = values['nome'].strip() != ''
            check_nivel = values['nivel'] != ''
            check_pagina = values['pagina'] != ''
            check_origem = values['origem'].strip() != ''
            if all([check_nome, check_nivel, check_pagina, check_origem]):
                self.__window['Confirmar'].update(disabled=False)
            else:
                self.__window['Confirmar'].update(disabled=True)
            values['nome'] = values['nome'].title().strip()
        self.close()
        if button == 'Confirmar':
            return values
        else:
            return
    
    def exibir_tabela(self, cabecalho, dados, nome_objeto='Habilidade'):
        return super().exibir_tabela(cabecalho, dados, nome_objeto)

    @property
    def window(self):
        return self.__window

    @window.setter
    def window(self, window):
        if isinstance(window, sg.Window):
            self.__window = window
