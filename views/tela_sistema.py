from views.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaSistema(TelaAbstrata):
    def __init__(self, nome_objeto='Sistema'):
        super().__init__(nome_objeto)

    def mostra_tela(self, nome_objeto = 'Sistema', layout_extra = None, indice_layout_extra = 0, crud=True):
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

        return super().mostra_tela(nome_objeto='Sistema', layout_extra=layout, indice_layout_extra=0, crud=False)

