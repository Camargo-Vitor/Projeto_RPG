from abc import ABC, abstractmethod
import os
import PySimpleGUI as sg

class TelaAbstrata(ABC):
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
        self.window = sg.Window(f'Gerenciador de {nome_objeto}').Layout(layout)

    def mostra_tela(self, opcoes:list = [], nome_objeto: str = '', layout_extra:list[list]=None, indice_layout_extra: int=0, crud=True):
        if opcoes != []:        
            opc = self.le_int_ou_float(
                'Digite a opção: ',
                conjunto_alvo = opcoes
                        )

            if os.name == 'posix':
                os.system('clear')  
            else:
                os.system('cls')

            return opc
        else:
            self.init_components(nome_objeto, layout_extra, indice_layout_extra, crud=crud)
            while True:
                button, values = self.open()
                if button in (sg.WIN_CLOSED, 'Cancelar'):
                    self.close()
                    return 0
                elif any(values[key] for key in self.window.key_dict.keys()):
                    self.window['Confirmar'].update(disabled=False)
                else:
                    self.window['Confirmar'].update(disabled=True)
                if button == 'Confirmar':
                    for key, opc in values.items():
                        if opc:
                            escolha = int(key)
                            self.close()
                            return escolha

    def le_int_ou_float(self, mensagem: str, conjunto_alvo: list=None, positivo: bool=False, tipo: str='int'):
        while True:
            try:
                if tipo not in ('int', 'float'):
                    raise ValueError("[ERRO] Tipo inválido. Esperado 'int' ou 'float'.")

                entrada = input(mensagem)

                try:
                    num = int(entrada) if tipo == 'int' else float(entrada)
                except ValueError:
                    if tipo == 'int':
                        raise ValueError('[ERRO] O valor digitado deve ser um número inteiro')
                    else:
                        raise ValueError('[ERRO] O valor digitado deve ser um número (utilize "." para decimais)')

                if (conjunto_alvo is not None) and (num not in conjunto_alvo):
                    raise ValueError("[ERRO] O valor digitado não está dentro do conjunto de valores válidos.")
                elif positivo and num < 0:
                    raise ValueError("[ERRO] O valor digitado deve ser positivo")

                return num

            except ValueError as e:
                print(e)
            except Exception as e :
                print(f'[ERRO INESPERADO] Ocorreu um erro inesperado: {str(e)}')

    def le_str(self, mensagem:str, formato='title'):
        entrada = ''
        while True:
            entrada = input(mensagem).strip()
            if not entrada.isnumeric() and not entrada == '':
                break
            print(f'[ERRO] Entrada inválida, não digite números ou espaços vazios.')

        if formato == 'title':
            return entrada.title()
        else:
            return entrada.capitalize()

    def selecionar_obj_por_cod(self, obj: str, total_codigos: list):
        layout = [
            [sg.Text(f'Digite o ID do(a) {obj} desejado(a)')],
            [sg.Text('ID: ', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Submit('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Seleção de Magia').Layout(layout)
        button, values = self.window.Read()
        try:
            values['codigo'] = int(values['codigo'])
            if values['codigo'] not in total_codigos:
                raise Exception()
        except Exception as e:
            self.close()
            if button == 'Cancelar':
                return 0
            else:
                print(f'[ERRO INESPERADO] Erro ao selecionar entidade por código: {e}')
        self.close()
        return values['codigo']

    def exibir_tabela(self, cabecalho: list, dados: list[list], nome_objeto: str):
        layout = [
            [sg.Text(f"Lista de {nome_objeto}", font=("Arial", 16))],
            [sg.Table(values=dados,
                      headings=cabecalho,
                      auto_size_columns=True,
                      display_row_numbers=False,
                      justification='center',
                      num_rows=min(10, len(dados)),
                      key='-TABELA-')],
            [sg.Button("OK")]
        ]
        self.window = sg.Window(f"{nome_objeto} Cadastrados", layout)
        button, _ = self.window.read()
        self.window.close()

    @property
    @abstractmethod
    def window(self):
        pass

    @window.setter
    @abstractmethod
    def window(self, window):
        pass

    def mensagem(self, msg):
        sg.popup("", msg)
