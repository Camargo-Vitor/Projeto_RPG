from views.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaSistema(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_components()

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
    
    def close(self):
        self.__window.Close()

    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkBrown4') #procurar corzinha
        layout = [
            [sg.Text('Bem vindo ao sistema de gerenciamento de uma aventura de D&D!', font=('Arial', 25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Item',"RD1", key='1')],
            [sg.Radio('Magia',"RD1", key='2')],
            [sg.Radio('Habilidade',"RD1", key='3')],
            [sg.Radio('Espécie',"RD1", key='4')],
            [sg.Radio('Classe',"RD1", key='5')],
            [sg.Radio('Pessoa',"RD1", key='6')],
            [sg.Radio('Ficha',"RD1", key='7')],
            [sg.Radio('Finalizar sistema',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Gerenciamento de aventura de D&D').Layout(layout)
        
    @property
    def window(self):
        pass

    @window.setter
    def window(self, window):
        pass