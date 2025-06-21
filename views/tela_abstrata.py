from abc import ABC, abstractmethod
import os
import PySimpleGUI as sg

class TelaAbstrata(ABC):
    def init_components(self, nome_objeto: str):
       sg.change_look_and_feel('DarkBrown4')
       layout = [
           [sg.Text(f'Gerenciador de {nome_objeto}', font = ('Arial', 25))],
           [sg.Text('Escolha uma opção', font=('Arial', 15))],
           [sg.Radio(f'Incluir {nome_objeto}', 'RD1', key = '1')],
           [sg.Radio(f'Excluir {nome_objeto}', 'RD1', key = '2')],
           [sg.Radio(f'Listar {nome_objeto}', 'RD1', key = '3')],
           [sg.Radio(f'Alterar {nome_objeto}', 'RD1', key = '4')],
           [sg.Radio('Retornar', "RD1", key = '0')],
           [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
       self.window = sg.Window(f'Gerenciador de {nome_objeto}').Layout(layout)

    def mostra_tela(self, opcoes=[], nome_objeto: str = ''):
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
            self.init_components(nome_objeto)
            button, values = self.open()
            for key, opc in values.items():
                if opc:
                    opcoes = int(key)
            if values['0'] or button in (None,'Cancelar'):
                opcoes = 0
            self.close()
            return opcoes

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
            print(f'[ERRO INESPERADO] Erro ao selecionar entidade por código: {e}')
            self.close()
            return -1
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
        window = sg.Window(f"{nome_objeto} Cadastrados", layout)
        button, _ = window.read()
        window.close()

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
