from views.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaItens(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_components('Item')

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def init_components(self, objeto):
        return super().init_components(objeto)

    def mostra_tela(self, objeto='Item'):
        return super().mostra_tela(nome_objeto=objeto)

    def exibir_tabela(self, cabecalho, dados, nome_objeto='Item'):
        return super().exibir_tabela(cabecalho, dados, nome_objeto)

    def pegar_dados_item(self):
        layout = [
            [sg.Text('Dados Item', font = ('Helvica', 25))],
            [sg.Text('Nome', size = (15, 1)), sg.InputText('', key='nome', enable_events=True)],
            [sg.Text('Raridade: ', size = (15, 1)),
             sg.InputCombo(('comum', 'raro', 'épico', 'lendário'), size=(20, 1), readonly=True, enable_events=True, key='raridade')],
            [sg.Text('Pagina', size = (15, 1)), sg.Combo(values=([i for i in range(1, 385)]), enable_events=True, readonly=True, key='pagina')],
            [sg.Text('Valor', size = (15, 1)), sg.InputText('PO', enable_events=True, key='valor')],
            [sg.Submit('Confirmar', disabled=True), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Novo Item!').Layout(layout)
        while True:
            button, values = self.__window.read()
            if button in (sg.WIN_CLOSED, "Cancelar", 'Confirmar'):
                break
            check_nome = values['nome'].strip() != ''
            check_raridade = values['raridade'].strip() != ''
            check_pagina = values['pagina'] != None
            check_valor = values['valor'] != None
            if all([check_nome, check_raridade, check_pagina, check_valor]):
                self.__window['Confirmar'].update(disabled=False)
            else:
                self.__window['Confirmar'].update(disabled=True)
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

    @property
    def window(self):
        return self.__window

    @window.setter
    def window(self, window):
        if isinstance(window, sg.Window):
            self.__window = window
