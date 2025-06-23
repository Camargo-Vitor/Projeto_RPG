from views.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaClasses(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_components('Classe')
    
    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
    """
    def mostra_tela(self, opcoes=[1, 2, 3, 4, 5, 6, 7, 8, 0]):
        print('===== Classes =====')
        print('1. Adicionar Classe')
        print('2. Excluir Classe')
        print('3. Listar Classes')
        print('4. Modificar dados básicos Classe')
        print('5. Adiconar habilidade Classe')
        print('6. Remover habilidade Classe')
        print('7. Adicionar habilidade Subclasse')
        print('8. Remover habilidade subclasse')
        print('0. Retornar ')
        return super().mostra_tela(opcoes)
        """
    def mostra_tela(self, opcoes = [], nome_objeto = '', layout_extra = None, indice_layout_extra = 0, crud=False):
        layout = [
            [sg.Text(f'Gerenciador de Especies e Subespecies', font = ('Arial', 25))],
            [sg.Text('Escolha uma opção', font=('Arial', 15))],
            [sg.Radio(f'Incluir Classe', 'RD1', enable_events=True, key = '1')],
            [sg.Radio(f'Excluir Classe ', 'RD1', enable_events=True, key = '2')],
            [sg.Radio(f'Listar Classe', 'RD1', enable_events=True, key = '3')],
            [sg.Radio(f'Alterar Classe', 'RD1', enable_events=True, key = '4')],
            [sg.Radio(f'Listar Subclasse', 'RD1', enable_events=True, key = '9')],
            [sg.Radio(f'Incluir Habilidade em Classe', 'RD1', enable_events=True, key = '5')],
            [sg.Radio(f'Excluir Habilidade de Classe', 'RD1', enable_events=True, key = '6')],
            [sg.Radio(f'Incluir Habilidade em Subclasse', 'RD1', enable_events=True, key = '7')],
            [sg.Radio(f'Excluir Habilidade de Subclasse', 'RD1', enable_events=True, key = '8')],
            [sg.Radio('Retornar', "RD1", enable_events=True, key = '0')],
            [sg.Button('Confirmar', disabled=True), sg.Cancel('Cancelar')]
        ]
        return super().mostra_tela(opcoes, nome_objeto, layout, indice_layout_extra, crud=False)
    
    def exibir_tabela(self, cabecalho, dados, nome_objeto='Classe'):
        return super().exibir_tabela(cabecalho, dados, nome_objeto)
    
    def pegar_dados_classes(self):
        layout = [
            [sg.Text('Dados Classe', font = ('Helvica', 25))],
            [sg.Text('Nome', size = (15, 1)), sg.InputText('', key='nome', enable_events=True)],
            [sg.Text('Dado de vida', size=(15, 1)),
            sg.Combo(values=[i for i in range(4, 13, 2)], enable_events=True, readonly=True, key='dado')],
            [sg.Text('1ª Opção Subclasse', size = (15, 1)), sg.InputText('', key='nome_sub1', enable_events=True)],
            [sg.Text('2ª Opção Subclasse', size = (15, 1)), sg.InputText('', key='nome_sub2', enable_events=True)],
            [sg.Text('3ª Opção Subclasse', size = (15, 1)), sg.InputText('', key='nome_sub3', enable_events=True)],
            [sg.Submit('Confirmar', disabled=True), sg.Cancel('Cancelar')]
            ]
        
        self.__window = sg.Window('Dados Especie').Layout(layout)

        while True:
            button, values = self.__window.read()

            if button in (sg.WIN_CLOSED, 'Confirmar'):
                self.close()
                values['nome'] = values['nome'].strip().title()
                dados = {
                    'nome': values['nome'],
                    'dado': values['dado'],
                    'nomes_sub': [values['nome_sub1'], values['nome_sub2'], values['nome_sub3']]
                }
                return dados
            elif button == 'Cancelar':
                self.close()
                return 0
            
            check_nome = values['nome'].strip() != ''
            check_dado = values['dado'] != ''
            check_nome_sub1 = values['nome_sub1'].strip() != ''
            check_nome_sub2 = values['nome_sub2'].strip() != ''
            check_nome_sub3 = values['nome_sub3'].strip() != ''
            

            if all([check_nome, check_dado, check_nome_sub1, check_nome_sub2, check_nome_sub3]):
                self.__window['Confirmar'].update(disabled=False)
            else:
                self.__window['Confirmar'].update(disabled=True)

    def ler_subclasse(self):
        layout = [
            [sg.Text("Escolher Subclasse", font=('Arial', 20))],
            [sg.Text('Subclasses:', size=(15, 1)),
            sg.Combo(values=[str(a) for a in range(1, 4)], key="subclasse", readonly=True)],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]

        self.__window = sg.Window('Selecionar Subclasse', layout)

        while True:
            button, values = self.open()

            if button in (sg.WIN_CLOSED, 'Confirmar'):
                self.close()
                return values
            elif button == 'Cancelar':
                self.close()
                return 0


    def mostra_classe_e_subclasse(self, dados_classe: dict, classe=True, subclasse=True):
        if classe:
            print('==== Classe ===='.center(36, '='))
            print(f"{'Cod':^4} | {'Nome':^10} | {'Dado':^5} | {'Habilidades'}")
            print(f"{dados_classe['cod']:^4}", end= ' | ')
            print(f"{dados_classe['nome']:^10}", end = ' | ')
            print(f"{dados_classe['dado']:^5}", end= ' | ')
            print(f"{str(dados_classe['habilidades']):^9}")
        if subclasse:
            print('==== Subclasses ===='.center(36, '='))
            print(f"{'Nome':^13} | {'Habilidades Especificas'}")
            for a in range(3):
                print(f"{str(dados_classe['nomes_sub'][a]):^13}", end= ' | ')
                print(f"{str(dados_classe['habilidades_sub'][a]):^13}")
        print('=' *60)
    
    @property
    def window(self):
        return self.__window

    @window.setter
    def window(self, window):
        self.__window = window