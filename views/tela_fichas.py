from views.tela_abstrata import TelaAbstrata
from random import randint
import PySimpleGUI as sg


class TelaFichas(TelaAbstrata):
    def __init__(self, nome_objeto='Ficha'):
        super().__init__(nome_objeto)

    def mostra_tela(self, nome_objeto = 'Ficha', layout_extra = None, indice_layout_extra = 0, crud=False):
        layout = [
            [sg.Text(f'Gerenciador de Fichas', font = ('Arial', 25))],
            [sg.Text('Escolha uma opção', font=('Arial', 15))],
            [sg.Radio(f'Incluir Ficha', 'RD1', enable_events=True, key = '1')],
            [sg.Radio(f'Excluir Ficha', 'RD1', enable_events=True, key = '2')],
            [sg.Radio(f'Listar Fichas', 'RD1', enable_events=True, key = '3')],
            [sg.Radio(f'Alterar vida de uma Ficha', 'RD1', enable_events=True, key = '4')],
            [sg.Radio(f'Alterar moedas de uma Ficha', 'RD1', enable_events=True, key = '40')],
            [sg.Radio(f'Subir nivel de uma Ficha', 'RD1', enable_events=True, key = '5')],
            [sg.Radio(f'Adicionar Item em Ficha', 'RD1', enable_events=True, key = '6')],
            [sg.Radio(f'Remover Item em Ficha', 'RD1', enable_events=True, key = '7')],
            [sg.Radio(f'Adicionar Magia em Ficha', 'RD1', enable_events=True, key = '8')],
            [sg.Radio(f'Remover Magia em Ficha', 'RD1', enable_events=True, key = '9')],
            [sg.Radio(f'Relatorio Fichas', 'RD1', enable_events=True, key = '10')],
            [sg.Radio('Retornar', "RD1", enable_events=True, key = '0')],
            [sg.Button('Confirmar', disabled=True), sg.Cancel('Cancelar')]
        ]
        return super().mostra_tela(nome_objeto, layout, indice_layout_extra, crud)

    def pegar_dados_ficha(self, classes: list[str], subespecies: list[str]):
        dic_num_pericias = {
            1: 'atletismo', 2: 'prestidigitacao', 3: 'acrobacia', 4: 'furtividade',
            5: 'arcanismo', 6: 'historia', 7: 'investigacao', 8: 'natureza', 9: 'religiao',
            10: 'percepcao', 11: 'lidar com animais', 12: 'intuicao', 13: 'sobrevivencia',
            14: 'medicina', 15: 'persuasao', 16: 'intimidacao', 17: 'performance', 18: 'enganacao'
        }

        lista_pericias = [(k, v.title()) for k, v in dic_num_pericias.items()]

        valores_sorteados = [sum(sorted([randint(1, 6) for _ in range(4)])[1:]) for _ in range(6)]
        ATRIBUTOS = ['forca', 'destreza', 'constituicao', 'inteligencia', 'sabedoria', 'carisma']

        layout = [
            [sg.Text('Criar Ficha', font=('Helvetica', 20))],
            [sg.Text('Nome:'), sg.Input(key='nome', enable_events=True)],
            [sg.Text('Descrição Física:'), sg.Multiline(size=(35, 3), key='descricao_fisica', enable_events=True)],
            [sg.Text('História:'), sg.Multiline(size=(35, 3), key='historia', enable_events=True)],
            [sg.Text('Moedas:'), sg.Input(key='moedas', enable_events=True)],
            [sg.Text('Classe:'), sg.Combo(classes, key='classe', readonly=True, enable_events=True)],
            [sg.Text('Subespécie:'), sg.Combo(subespecies, key='subespecie', readonly=True, enable_events=True)],

            [sg.Text('Selecione 5 perícias:')],
            [sg.Checkbox(nome, key=num, enable_events=True) for num, nome in lista_pericias[:6]],
            [sg.Checkbox(nome, key=num, enable_events=True) for num, nome in lista_pericias[6:12]],
            [sg.Checkbox(nome, key=num, enable_events=True) for num, nome in lista_pericias[12:]],

            [sg.Text(f'Valores sorteados: {valores_sorteados}')],
        ]

        for atributo in ATRIBUTOS:
            layout.append([
                sg.Text(f'{atributo.title()}:'),
                sg.Combo(values=valores_sorteados.copy(), key=f'atributo_{atributo}', readonly=True, enable_events=True)
            ])

        layout.append([sg.Button('Confirmar', key='Confirmar', disabled=True), sg.Cancel('Cancelar')])

        self.init_components('Nova ficha', layout, crud=False)

        while True:
            button, values = self.open()
            if button in (sg.WIN_CLOSED, 'Cancelar'):
                self.close()
                return 0

            check_inputs = all([
                values['nome'].strip(),
                values['descricao_fisica'].strip(),
                values['historia'].strip(),
                values['classe'],
                values['subespecie'],
                values['moedas'].isdigit(),
                sum([values[k] for k in dic_num_pericias]) == 5,
                all([values[f'atributo_{a}'] != '' for a in ATRIBUTOS])
            ])

            self.window['Confirmar'].update(disabled=not check_inputs)

            if button == 'Confirmar':
                pericias_treinadas = [dic_num_pericias[k] for k in dic_num_pericias if values[k]]
                atributos_distribuidos = [int(values[f'atributo_{a}']) for a in ATRIBUTOS]
                if sorted(atributos_distribuidos) != sorted(valores_sorteados):
                    sg.popup_error('Cada valor sorteado deve ser usado exatamente uma vez!')
                    continue

                self.window.close()
                return {
                    'nome': values['nome'].strip().title(),
                    'descricao_fisica': values['descricao_fisica'].strip(),
                    'historia': values['historia'].strip(),
                    'classe': values['classe'],
                    'subespecie': values['subespecie'],
                    'moedas': int(values['moedas']),
                    'pericias_treinadas': pericias_treinadas,
                    'atributos': atributos_distribuidos
                }

    def ler_dado_alterado(self, dado='vida'):
        layout = [
            [sg.Text(f"Alterar {dado}", font=("Arial", 24))],
            [sg.Radio('Subtrair', 'RD1', enable_events=True, key='subtrair'),
             sg.Radio('Somar', 'RD1', enable_events=True, key='somar')],
            [sg.Text('Dado: '), sg.InputText(size=(15, 1), enable_events=True, key='valor')],
            [sg.Submit('Confirmar', disabled=True), sg.Cancel('Cancelar')]
        ]

        self.init_components('Altera dado', layout, crud=False)

        while True:
            button, values = self.open()

            if button in (sg.WIN_CLOSED, 'Confirmar'):
                self.close()
                if values['subtrair']:
                    return -int(values['valor'])
                elif values['somar']:
                    return +int(values['valor'])
            elif button == 'Cancelar':
                self.close()
                return 0

            if values['valor'].isnumeric() and (values['subtrair'] or values['somar']):
                self.window['Confirmar'].update(disabled=False)
            else:
                self.window['Confirmar'].update(disabled=True)

    def pegar_dados_atributos(self):
        print('==== Atributos ====')
        valores_sorteados = []
        for x in range(6):
            valores_sorteados.append(sum((sorted([int(randint(1, 6)) for x in range(4)]))[1:]))
        sequencia_atributos = [
            'forca',
            'destreza',
            'constituicao',
            'inteligencia',
            'sabedoria',
            'carisma'
        ]

        sequencia_escolhida = []
        while valores_sorteados != []:
            print(f'Valores sorteados: {valores_sorteados}')
            num_escolhido = self.le_int_ou_float(f'Selecione o valor de {sequencia_atributos[0]}: ', conjunto_alvo=valores_sorteados)
            del sequencia_atributos[0]
            sequencia_escolhida.append(num_escolhido)
            valores_sorteados.remove(num_escolhido)

        return sequencia_escolhida
        
    def mostra_ficha_inteira(self, dados_ficha: dict):
        atributos = [
            ['Força', dados_ficha['forca']],
            ['Destreza', dados_ficha['destreza']],
            ['Constituição', dados_ficha['constituicao']],
            ['Inteligência', dados_ficha['inteligencia']],
            ['Sabedoria', dados_ficha['sabedoria']],
            ['Carisma', dados_ficha['carisma']]
        ]

        layout = [
            [sg.Text('FICHA DE PERSONAGEM', font=('Helvetica', 20), justification='center', expand_x=True)],
            [sg.Text(f"Nome: {dados_ficha['nome']}", size=(40,1)), sg.Text(f"Nível: {dados_ficha['nivel']}")],
            [sg.Text(f"Classe: {dados_ficha['classe']}"), sg.Text(f"Subclasse: {dados_ficha['subclasse']}")],
            [sg.Text(f"Espécie: {dados_ficha['especie']}"), sg.Text(f"Deslocamento: {dados_ficha['deslocamento']} metros"), sg.Text(f"Altura: {dados_ficha['altura']} cm")],
            [sg.Text(f"Vida: {dados_ficha['vida_atual']}/{dados_ficha['vida']}"), sg.Text(f"Moedas: {dados_ficha['moedas']}")],
            
            [sg.Frame('Atributos', [[sg.Column([[sg.Text(attr, size=(12,1)), sg.Text(valor)] for attr, valor in atributos])]])],

            [sg.Text('Perícias treinadas:'), sg.Multiline('\n'.join(dados_ficha['pericias']), size=(45, 3), disabled=True)],
            [sg.Text('Inventário:'), sg.Multiline('\n'.join(dados_ficha['inventario']), size=(45, 3), disabled=True)],
            [sg.Text('Magias:'), sg.Multiline('\n'.join(dados_ficha['magias']), size=(45, 3), disabled=True)],
            [sg.Text('Habilidades:'), sg.Multiline('\n'.join(dados_ficha['habilidades']), size=(45, 3), disabled=True)],

            [sg.Text('Descrição Física:'), sg.Multiline(dados_ficha['fisico'], size=(45, 3), disabled=True)],
            [sg.Text('História:'), sg.Multiline(dados_ficha['historia'], size=(45, 5), disabled=True)],

            [sg.Button('Fechar')]
        ]

        window = sg.Window('Visualização da Ficha', layout, modal=True)

        while True:
            button, _ = window.read()
            if button in (sg.WINDOW_CLOSED, 'Fechar'):
                break
        window.close()
