from views.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaMagias(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_components('Magia')

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def init_components(self, nome_objeto):
        return super().init_components(nome_objeto)

    def mostra_tela(self, nome_objeto = 'Magia'):
        return super().mostra_tela(nome_objeto=nome_objeto)

    def exibir_tabela(self, cabecalho, dados, nome_objeto='Magia'):
        return super().exibir_tabela(cabecalho, dados, nome_objeto)

    def pegar_dados_magia(self):
        layout = [
            [sg.Text('Dados Magia')],
            [sg.Text('Nome', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Nivel', size=(15, 1)), sg.InputText('', key='nivel')],
            [sg.Text('Pagina', size=(15, 1)), sg.InputText('', key='pagina')],
            [sg.Submit('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Dados Magia').Layout(layout)
        button, values = self.__window.Read()
        try:
            values['nome'] = values['nome'].title().strip()
            values['nivel'] = int(values['nivel'])
            values['pagina'] = int(values['pagina'])
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
