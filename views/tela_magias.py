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
            [sg.Text('Gerenciador de Magias', font=('Arial', 25))],
            [sg.Radio('Criar Magia',"RD1", key='1')],
            [sg.Radio('Excluir Magia',"RD1", key='2')],
            [sg.Radio('Listar Magias',"RD1", key='3')],
            [sg.Radio('Modificar Magia',"RD1", key='4')],
            [sg.Radio('Retornar',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Gerenciador de Magias').Layout(layout)

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

    def exibir_tabela(self, cabecalho: list, dados: list[list]):
        layout = [
            [sg.Text("Lista de Magias", font=("Arial", 16))],
            [sg.Table(values=dados,
                      headings=cabecalho,
                      auto_size_columns=True,
                      display_row_numbers=False,
                      justification='center',
                      num_rows=min(10, len(dados)),
                      key='-TABELA-')],
            [sg.Button("OK")]
        ]
        window = sg.Window("Magias Cadastradas", layout)
        button, _ = window.read()
        window.close()

    def selecionar_obj_por_cod(self, obj: str, total_codigos: list):
        layout = [
            [sg.Text('Digite o ID da magia desejada: ')],
            [sg.Text('ID: ', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Submit('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleção de Magia').Layout(layout)
        button, values = self.__window.Read()
        try:
            values['codigo'] = int(values['codigo'])
            if values['codigo'] not in total_codigos:
                raise Exception()
        except Exception as e:
            print(f'[ERRO INESPERADO] Erro ao selecionar entidade por código: {e}')
            self.close()
            return -1
        self.close()
        return values['codigo']