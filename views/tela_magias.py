from views.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaMagias(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_components()

    def close(self):
        self.__window.Close()

    def init_components(self):
        sg.ChangeLookAndFeel('DarkBrown4')
        layout = [
            [sg.Text('===== Magias =====', font=('Arial', 25))],
            [sg.Radio('Criar Magia',"RD1", key='1')],
            [sg.Radio('Excluir Magia',"RD1", key='2')],
            [sg.Radio('Listar Magias',"RD1", key='3')],
            [sg.Radio('Modificar Magia',"RD1", key='4')],
            [sg.Radio('Retornar',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Gerenciamento de aventura de D&D').Layout(layout)

    def mostra_tela(self, opcoes=[1, 2, 3, 4, 0]):
        self.init_components()
        button, values = self.__window.Read()
        for key, opc in values.items():
            if opc:
                opcoes = int(key)
        if values['0'] or button in (None,'Cancelar'):
            opcoes = 0
        self.close()
        return opcoes

    def pegar_dados_magia(self):
        layout = [
            [sg.Text('==== Dados Magia ====')],
            [sg.Text('Nome', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Nivel', size=(15, 1)), sg.InputText('', key='nivel')],
            [sg.Text('Pagina', size=(15, 1)), sg.InputText('', key='pagina')],
            [sg.Submit('Confirmar'), sg.Cancel()]
        ]
        self.__window = sg.Window('Novo Item!').Layout(layout)
        button, values = self.__window.Read()
        try:
            values['nivel'] = int(values['nivel'])
            values['pagina'] = int(values['pagina'])
        except:
            self.close()
            return -1
        self.close()
        return values

    def mostra_magia(self, dados_magia: dict):
        print(f"{dados_magia['cod']:^4}", end=' | ')
        print(f"{dados_magia['nome']:^16}", end=' | ')
        print(f"{dados_magia['nivel']:^5}", end=' | ')
        print(f"{dados_magia['pagina']:^5}")
