from views.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaSistema(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_components()
    
    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkBrown4') #procurar corzinha
        layout = [
            [sg.Text('Bem vindo ao sistema de gerenciamento de uma aventura de D&D!', font=('Arial', 25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Item',"RD1", enable_events=True,  key='1',)],
            [sg.Radio('Magia',"RD1", enable_events=True, key='2')],
            [sg.Radio('Habilidade',"RD1", enable_events=True, key='3')],
            [sg.Radio('Espécie',"RD1", enable_events=True, key='4')],
            [sg.Radio('Classe',"RD1", enable_events=True, key='5')],
            [sg.Radio('Pessoa',"RD1", enable_events=True, key='6')],
            [sg.Radio('Ficha',"RD1", enable_events=True, key='7')],
            [sg.Radio('Finalizar sistema',"RD1", enable_events=True, key='0')],
            [sg.Button('Confirmar', disabled=True), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Gerenciamento de aventura de D&D').Layout(layout)

    def mostra_tela(self, opcoes=[]):
        self.init_components()
        while True:
            button, values = self.open()
            if button in (sg.WIN_CLOSED, 'Cancelar'):
                self.close()
                return 0
            if any(values[key] for key in ['0','1','2','3','4','5','6','7']):
                self.__window['Confirmar'].update(disabled=False)
            else:
                self.__window['Confirmar'].update(disabled=True)

            if button == 'Confirmar':
                for key, opc in values.items():
                    if opc:
                        escolha = int(key)
                        self.close()
                        return escolha
   
    @property
    def window(self):
        pass

    @window.setter
    def window(self, window):
        pass