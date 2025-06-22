from views.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaEspecies(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_components('Especie')
    
    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def mostra_tela(self, opcoes = [], nome_objeto = '', layout_extra = None, indice_layout_extra = 0, crud=False):
        layout_extra = [
            [sg.Text(f'Gerenciador de Especies e Subespecies', font = ('Arial', 25))],
            [sg.Text('Escolha uma opção', font=('Arial', 15))],
            [sg.Radio(f'Incluir Especie', 'RD1', enable_events=True, key = '1')],
            [sg.Radio(f'Excluir Especie ', 'RD1', enable_events=True, key = '2')],
            [sg.Radio(f'Listar Especie', 'RD1', enable_events=True, key = '3')],
            [sg.Radio(f'Alterar Especie', 'RD1', enable_events=True, key = '4')],
            [sg.Radio(f'Incluir Habilidade em Especie', 'RD1', enable_events=True, key = '5')],
            [sg.Radio(f'Excluir Habilidade de Especie', 'RD1', enable_events=True, key = '6')],
            [sg.Radio(f'Incluir Subespecie', 'RD1', enable_events=True, key = '7')],
            [sg.Radio(f'Excluir Subespecie', 'RD1', enable_events=True, key = '8')],
            [sg.Radio(f'Listar Subespecie', 'RD1', enable_events=True, key = '9')],
            [sg.Radio(f'Alterar Subespecie', 'RD1', enable_events=True, key = '10')],
            [sg.Radio(f'Incluir Habilidade em Subespecie', 'RD1', enable_events=True, key = '11')],
            [sg.Radio(f'Excluir Habilidade de Subespecie', 'RD1', enable_events=True, key = '12')],
            [sg.Radio('Retornar', "RD1", enable_events=True, key = '0')],
            [sg.Button('Confirmar', disabled=True), sg.Cancel('Cancelar')]
        ]
        return super().mostra_tela(opcoes, nome_objeto, layout_extra, indice_layout_extra, crud=False)

    def exibir_tabela(self, cabecalho, dados, nome_objeto='Especie'):
        return super().exibir_tabela(cabecalho, dados, nome_objeto)
    '''
    def mostra_tela_especie(self, opcoes = [1, 2, 3, 4, 5, 6, 0]):
        print('===== Especie =====')
        print('1. Criar Especie')
        print('2. Excluir Especie')
        print('3. Listar Especies')
        print('4. Modificar Especie')
        print('5. Adicionar Habilidade')
        print('6. Remover Habilidade')
        print('0. Retornar')
        return super().mostra_tela(opcoes)
    
    def mostra_tela_subespecie(self, opcoes = [1, 2, 3, 4, 5, 6, 0]):
        print('===== Subespecie =====')
        print('1. Criar Subespecie')
        print('2. Excluir Subespecie')
        print('3. Listar Subespecie')
        print('4. Modidicar Subespecie')    
        print('5. Adicionar Habilidade')
        print('6. Remover Habilidade')
        print('0. Retornar')
        return super().mostra_tela(opcoes)
    '''
    def pegar_dados_especie(self):
        layout = [
            [sg.Text('Dados Especie', font = ('Helvica', 25))],
            [sg.Text('Nome', size = (15, 1)), sg.InputText('', key='nome', enable_events=True)],
            [sg.Text('Deslocamento', size=(15, 1)),
            sg.Combo(values=[i/10 for i in range(60, 600, 15)], enable_events=True, readonly=True, key='deslocamento')],
            [sg.Text('Altura (cm)', size = (15, 1)), 
            sg.Slider(range = (60, 240), default_value= 85, orientation= 'h', key='altura')],
            [sg.Submit('Confirmar', disabled=True), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Dados Especie').Layout(layout)

        while True:
            button, values = self.__window.read()

            if button in (sg.WIN_CLOSED, 'Confirmar'):
                break
            elif button == 'Cancelar':
                self.close()
                return 0
            
            check_nome = values['nome'].strip() != ''
            check_deslocamento = values['deslocamento'] != ''
            check_altura = values['altura'] != ''
            

            if all([check_nome, check_deslocamento, check_altura]):
                self.__window['Confirmar'].update(disabled=False)
            else:
                self.__window['Confirmar'].update(disabled=True)


    def pegar_dados_subespecie(self, especie: str):
        print('===== Dados Subespecie =====')
        nome = self.le_str(f'Nome: {especie} ')
        return {'nome': nome}
    
    def mostra_especie(self, dados_especie: dict):
        print(' Especie '.center(60,'='))
        print(f'{"Cod":^4} | {"Nome":^16} | {"Deslocamento":^16} | {"Altura média(cm)":^18}')
        print(f"{dados_especie['cod']:^4}", end=' | ')
        print(f"{dados_especie['nome']:^16}", end=' | ')
        print(f"{dados_especie['deslocamento']:^16}", end=' | ')
        print(f"{dados_especie['altura']:^18}")
        print(f'===== Habilidades ====='.center(60, '='))
        print(f"{str(dados_especie['habilidades'])}")

    def mostra_subespecie(self, dados_subespecie: dict):
        self.mostra_especie(dados_subespecie)
        print(f'===== Habilidades específicas ====='.center(60, '='))
        print(f"{str(dados_subespecie['habilidades_esp'])}")

    @property
    def window(self):
        return self.__window

    @window.setter
    def window(self, window):
        self.__window = window