from views.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaPessoas(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_components('Pessoa')

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def mostra_tela(self, opcoes = [], nome_objeto = 'Pessoas', layout_extra = None, indice_layout_extra = 0, crud=False):
        layout = [
            [sg.Text(f'Gerenciador de Pessoa', font = ('Arial', 25))],
            [sg.Text('Escolha uma opção', font=('Arial', 15))],
            [sg.Radio(f'Incluir Jogador', 'RD1', enable_events=True, key = '1')],
            [sg.Radio(f'Excluir Jogador ', 'RD1', enable_events=True, key = '2')],
            [sg.Radio(f'Listar Jogador', 'RD1', enable_events=True, key = '3')],
            [sg.Radio(f'Alterar Jogador', 'RD1', enable_events=True, key = '4')],
            [sg.Radio(f'Adicionar Ficha', 'RD1', enable_events=True, key = '5')],
            [sg.Radio(f'Excluir Ficha', 'RD1', enable_events=True, key = '6')],
            [sg.Radio(f'Acessar Mestre', 'RD1', enable_events=True, key = '7')],
            [sg.Radio('Retornar', "RD1", enable_events=True, key = '0')],
            [sg.Button('Confirmar', disabled=True), sg.Cancel('Cancelar')]
        ]
        return super().mostra_tela(opcoes, nome_objeto, layout, indice_layout_extra, crud=False)
    
    def exibir_tabela(self, cabecalho, dados, nome_objeto = 'Pessoas'):
        return super().exibir_tabela(cabecalho, dados, nome_objeto)
    

    def exibir_mestre(self, mestre):
        try:
            layout = [
                [sg.Text("Dados do Mestre", font=("Arial", 16))],
                [sg.Text("Nome:", size=(10, 1)), sg.InputText(mestre.nome, key="nome")],
                [sg.Text("Telefone:", size=(10, 1)), sg.InputText(mestre.telefone, key="telefone")],
                [sg.Text("Cidade:", size=(10, 1)), sg.InputText(mestre.endereco.cidade, key="cidade")],
                [sg.Text("Bairro:", size=(10, 1)), sg.InputText(mestre.endereco.bairro, key="bairro")],
                [sg.Text("Número:", size=(10, 1)), sg.InputText(mestre.endereco.numero, key="numero")],
                [sg.Text("CEP:", size=(10, 1)), sg.InputText(mestre.endereco.cep, key="cep")],
                [sg.Button("Salvar"), sg.Button("Cancelar")]
            ]

            window = sg.Window("Alterar Mestre", layout)
            while True:
                event, values = window.read()
                if event in (sg.WINDOW_CLOSED, "Cancelar"):
                    window.close()
                    return False
                elif event == "Salvar":
                    window.close()
                    return {
                        "nome": values["nome"],
                        "telefone": values["telefone"],
                        "cidade": values["cidade"],
                        "bairro": values["bairro"],
                        "numero": values["numero"],
                        "cep": values["cep"]
                    }
        except Exception as e:
            sg.popup_error(f"[ERRO INESPERADO] Erro ao exibir mestre: {e}")
            return False
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
            [sg.Text('Cidade', size=(15, 1)), sg.InputText('', key='cidade', enable_events= True)],
            [sg.Text('Bairro', size=(15, 1)), sg.InputText('', key='bairro', enable_events=True)],
            [sg.Text('Numero', size=(15, 1)), sg.InputText('', key='numero', enable_events=True)],
            [sg.Text('Cep', size=(15,1)), sg.InputText('', key='cep', enable_events=True)],
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
                self.__window['Confirmar'].update(disabled=True)

        self.close()

            
        values['nome'] = values['nome'].title().strip()
        values['telefone'] = int(values['telefone'])
        values['cidade'] = values['cidade'].title().strip()
        values['bairro'] = values['bairro'].title().strip()
        values['numero'] = int(values['numero'])
        values['cep'] = int(values['cep'])
        return values

    @property
    def window(self):
        return self.__window

    @window.setter
    def window(self, window):
        if isinstance(window, sg.Window):
            self.__window = window