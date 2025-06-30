from abc import ABC, abstractmethod
import os
import PySimpleGUI as sg

class TelaAbstrata(ABC):
    @abstractmethod
    def __init__(self, nome_objeto: str):
        self.__window: sg.Window = None
        self.init_components(nome_objeto)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def init_components(self, nome_objeto: str, layout_extra:list[list]=None, indice_layout_extra: int=0, crud=True):
        sg.change_look_and_feel('DarkBrown4')
        layout = []
        if crud:
            layout = [
                [sg.Text(f'Gerenciador de {nome_objeto}', font = ('Arial', 25))],
                [sg.Text('Escolha uma opção', font=('Arial', 15))],
                [sg.Radio(f'Incluir {nome_objeto}', 'RD1', enable_events=True, key = '1')],
                [sg.Radio(f'Excluir {nome_objeto}', 'RD1', enable_events=True, key = '2')],
                [sg.Radio(f'Listar {nome_objeto}', 'RD1', enable_events=True, key = '3')],
                [sg.Radio(f'Alterar {nome_objeto}', 'RD1', enable_events=True, key = '4')],
                [sg.Radio('Retornar', "RD1", enable_events=True, key = '0')],
                [sg.Button('Confirmar', disabled=True), sg.Cancel('Cancelar')]
            ]
        elif layout_extra:
            layout.insert(indice_layout_extra, layout_extra)
        self.__window = sg.Window(f'Gerenciador de {nome_objeto}').Layout(layout)
    
    @abstractmethod
    def mostra_tela(self, nome_objeto: str = '', layout_extra:list[list]=None, indice_layout_extra: int=0, crud=True):
        self.init_components(nome_objeto, layout_extra, indice_layout_extra, crud=crud)
        while True:
            ret = self.logica_confirmacao()
            if ret or ret == 0:
                return ret

    def logica_confirmacao(self):       
        button, values = self.open()
        if button in (sg.WIN_CLOSED, 'Cancelar'):
            self.close()
            return 0
        elif any(values[key] for key in self.__window.key_dict.keys()):
            self.__window['Confirmar'].update(disabled=False)
        else:
            self.__window['Confirmar'].update(disabled=True)
        if button == 'Confirmar':
            for key, opc in values.items():
                if opc:
                    escolha = int(key)
                    self.close()
                    return escolha
        return None

    def selecionar_obj_por_cod(self, obj: str, total_codigos: list):
        layout = [
            [sg.Text(f'Digite o ID do(a) {obj} desejado(a)')],
            [sg.Text('ID: ', size=(15, 1)), sg.InputText(key='codigo', enable_events=True)],
            [sg.Submit('Confirmar', disabled=True), sg.Cancel('Cancelar')]
        ]

        self.init_components('Seleciona objeto por código', layout, crud=False)

        while True:
            button, values = self.open()
            if button in (sg.WIN_CLOSED, 'Cancelar'):
                self.close()
                return 0
            elif values['codigo'].isnumeric() and int(values['codigo']) in total_codigos:
                self.__window['Confirmar'].update(disabled=False)
            else:
                self.__window['Confirmar'].update(disabled=True)
            if button == 'Confirmar':
                self.close()
                return int(values['codigo'])


    def exibir_tabela(self, cabecalho: list, dados: list[list], nome_objeto: str):
        layout = [
            [sg.Text(f"Lista de {nome_objeto}", font=("Arial", 16))],
            [sg.Table(values=dados,
                    headings=cabecalho,
                    auto_size_columns=True,
                    justification='center',
                    num_rows=min(10, len(dados)),
                    key='tabela',
                    enable_events=True)],
            [sg.Button("Ver Detalhes da Última Coluna"), sg.Button("OK")]
        ]

        self.init_components(f"{nome_objeto} Cadastrados", layout, crud=False)

        while True:
            button, values = self.open()
            if button in (sg.WIN_CLOSED, "OK"):
                break
            elif button == "Ver Detalhes da Última Coluna":
                if values['tabela']:
                    linha = values['tabela'][0]
                    ultima_coluna = dados[linha][-1]
                    sg.popup_scrolled(f"{cabecalho[-1]}:\n\n{ultima_coluna}", title="Detalhes", size=(60, 20), )

        self.close()


    def mensagem(self, msg):
        sg.popup("", msg)

    @property
    def window(self):
        return self.__window