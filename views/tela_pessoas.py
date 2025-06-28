from views.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaPessoas(TelaAbstrata):
    def __init__(self, nome_objeto='Pessoas'):
        super().__init__(nome_objeto)

    def mostra_tela(self, nome_objeto = 'Pessoas', layout_extra = None, indice_layout_extra = 0, crud=False):
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
        return super().mostra_tela(nome_objeto, layout, indice_layout_extra, crud=False)
    
    def exibir_tabela(self, cabecalho, dados, nome_objeto = 'Pessoas'):
        return super().exibir_tabela(cabecalho, dados, nome_objeto)
    
    def exibir_mestre(self, dados_mestre):
        try:
            layout = [
                [sg.Text("Dados do Mestre", font=("Arial", 16))],
                [sg.Text(f"Nome: {dados_mestre['nome']}", size=(20, 1))],
                [sg.Text(f"Telefone: {dados_mestre['telefone']}", size=(20, 1))],
                [sg.Text(f"Cidade: {dados_mestre['cidade']} ", size=(20, 1))],
                [sg.Text(f"Bairro: {dados_mestre['bairro']}", size=(20, 1))],
                [sg.Text(f"Número: {dados_mestre['numero']}", size=(20, 1))],
                [sg.Text(f"CEP: {dados_mestre['cep']}", size=(20, 1))],
                [sg.Button("Alterar"), sg.Button("Cancelar")]
            ]

            self.init_components('Dados Mestre', layout, crud=False)
            button, values = self.open()
            if button == 'Cancelar':
                self.close()
                return False
            if button == 'Alterar':
                self.close()
                novos_dados = self.pegar_dados_pessoa()
                return novos_dados
        except Exception as e:
            sg.popup_error(f"[ERRO INESPERADO] Erro ao exibir mestre: {e}")
            return False

    def pegar_dados_pessoa(self):
        layout = [
            [sg.Text('Dados Pessoas', font=('Helvica', 25))],
            [sg.Text('Nome', size=(15, 1)), sg.InputText(key='nome', enable_events=True)],
            [sg.Text('Telefone', size=(15, 1)), sg.InputText('', key='telefone', enable_events=True)],
            [sg.Text('Cidade', size=(15, 1)), sg.InputText('', key='cidade', enable_events= True)],
            [sg.Text('Bairro', size=(15, 1)), sg.InputText('', key='bairro', enable_events=True)],
            [sg.Text('Numero', size=(15, 1)), sg.InputText('', key='numero', enable_events=True)],
            [sg.Text('Cep', size=(15,1)), sg.InputText('', key='cep', enable_events=True)],
            [sg.Submit('Confirmar', disabled=True), sg.Cancel('Cancelar')]            
        ]

        self.init_components('Dados pessoa', layout, crud=False)

        while True:
            button, values = self.open()

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
                self.window['Confirmar'].update(disabled=False)
            else:
                self.window['Confirmar'].update(disabled=True)

        self.close()

        values['nome'] = values['nome'].title().strip()
        values['telefone'] = int(values['telefone'])
        values['cidade'] = values['cidade'].title().strip()
        values['bairro'] = values['bairro'].title().strip()
        values['numero'] = int(values['numero'])
        values['cep'] = int(values['cep'])
        return values
