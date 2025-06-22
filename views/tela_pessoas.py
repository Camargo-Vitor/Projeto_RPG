from views.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaItens(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_components('Item')

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
    '''
    def mostra_tela(self, opcoes=[1, 2, 3, 4, 5, 6, 7, 0]):
        print('===== Pessoas =====')
        print('1. Incluir Jogador')
        print('2. Excluir Jogador')
        print('3. Listar Jogador')
        print('4. Alterar Jogador')
        print('5. Adicionar Ficha')
        print('6. Remover Ficha')
        print('7. Acessar Mestre')
        print('0. Retornar')
        return super().mostra_tela(opcoes)
    '''

    def pegar_dados_pessoa(self):
        layout = [
            [sg.Text('Dados Pessoas', font=('Helvica', 25))],
            [sg.Text('Nome', size=(15, 1)), sg.InputText('', key='nome', enable_events=True)],
            [sg.Text('Telefone', size=(15, 1)), sg.InputText('', key='telefone', enable_events=True)],
            [sg.Text('Cidade', size=(15, 1)), sg.InputText('', key='cidade', enable_events= True)]
            [sg.Text('Bairro', size=(15, 1)), sg.InputText('', key='bairro', enable_events=True)],
            [sg.Text('Numero', size=(15, 1)), sg.InputText('', key='numero', enable_events=True)],
            [sg.Text('Cep', size=(15,1)), sg.InputText('', key='cep', enable_events=True)]
            [sg.Submit('Confirmar', disabled=True), sg.Cancel('Cancelar')]            
        ]

        
        self.__window = sg.Window('Dados Item').Layout(layout)

        while True:
            button, values = self.__window.read()

            if button in (sg.WIN_CLOSED, 'Confirmar'):
                break
            elif button == 'Cancelar':
                self.close()
                return 0

            check_nome = values['nome'].strip() != ''
            check_telefone = values['telefone'] != ''
            check_cidade = values['cidade'].strip() != ''
            check_bairro = values['bairro'].strip() != ''
            check_numero = values['numero'] != ''
            check_cep = values['cep'] != ''
            
            if all([check_nome, check_telefone, check_cidade, check_bairro, check_numero, check_cep]):
                self.__window['Confirmar'].update(disabled=False)
            else:
                self.__window['Conformar'].update(disabled=True)

            self.close()

            
            values['nome'] = values['nome'].title().strip()
            values['telefone'] = int(values['telefone'])
            values['cidade'] = values['cidade'].title().strip()
            values['bairro'] = values['bairro'].title().strip()
            values['numero'] = int(values['numero'])
            values['cep'] = int(values['cep'])
            return values

    def mostra_pessoa(self, dados_pessoa: dict):
        print(f"{dados_pessoa['cod']:^4}", end=' | ')
        print(f"{dados_pessoa['nome']:^16}", end=' | ')
        print(f"{dados_pessoa['telefone']:^13}", end=' | ')
        print(f"{dados_pessoa['cidade']:^16}", end=' | ')
        print(f"{dados_pessoa['bairro']:^12}", end=' | ')
        print(f"{dados_pessoa['numero']:^6}", end=' | ')
        print(f"{dados_pessoa['cep']:^10}", end=' |')

    def mostra_jogador(self, dados_jogador: dict):
        self.mostra_pessoa(dados_jogador)
        print(f"{dados_jogador['personagens']}")

    @property
    def window(self):
        return self.__window

    @window.setter
    def window(self, window):
        if isinstance(window, sg.Window):
            self.__window = window