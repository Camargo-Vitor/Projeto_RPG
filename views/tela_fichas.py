from views.tela_abstrata import TelaAbstrata
from random import randint
import PySimpleGUI as sg


class TelaFichas(TelaAbstrata):
    def __init__(self):
        self.__window: sg.Window = None
        self.init_components('Ficha')

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    '''
    def mostra_tela(self, opcoes=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]):
        print('===== Fichas =====')
        print('1. Incluir Ficha')
        print('2. Excluir Ficha')
        print('3. Listar Ficha')
        print('4. Alterar vida de uma ficha')
        print('5. Subir nivel de uma ficha')
        print('6. Adicionar item em ficha')
        print('7. Remover item ficha')
        print('8. Adicionar magia em ficha')
        print('9. Remover magia em ficha')
        print('10. Relatório de fichas')
        print('0. Retornar')
        return super().mostra_tela(opcoes)
    '''
    def mostra_tela(self, opcoes = [], nome_objeto = 'Ficha', layout_extra = None, indice_layout_extra = 0, crud=False):
        layout = [
            [sg.Text(f'Gerenciador de Fichas', font = ('Arial', 25))],
            [sg.Text('Escolha uma opção', font=('Arial', 15))],
            [sg.Radio(f'Incluir Ficha', 'RD1', enable_events=True, key = '1')],
            [sg.Radio(f'Excluir Ficha', 'RD1', enable_events=True, key = '2')],
            [sg.Radio(f'Listar Fichas', 'RD1', enable_events=True, key = '3')],
            [sg.Radio(f'Alterar vida de uma Ficha', 'RD1', enable_events=True, key = '4')],
            [sg.Radio(f'Subir nivel de uma Ficha', 'RD1', enable_events=True, key = '5')],
            [sg.Radio(f'Adicionar Item em Ficha', 'RD1', enable_events=True, key = '6')],
            [sg.Radio(f'Remover Item em Ficha', 'RD1', enable_events=True, key = '7')],
            [sg.Radio(f'Adicionar Magia em Ficha', 'RD1', enable_events=True, key = '8')],
            [sg.Radio(f'Remover Magia em Ficha', 'RD1', enable_events=True, key = '9')],
            [sg.Radio(f'Relatorio Fichas', 'RD1', enable_events=True, key = '10')],
            [sg.Radio('Retornar', "RD1", enable_events=True, key = '0')],
            [sg.Button('Confirmar', disabled=True), sg.Cancel('Cancelar')]
        ]
        return super().mostra_tela(opcoes, nome_objeto, layout, indice_layout_extra, crud)

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

        window = sg.Window('Nova Ficha', layout)

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                window.close()
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

            window['Confirmar'].update(disabled=not check_inputs)

            if event == 'Confirmar':
                pericias_treinadas = [dic_num_pericias[k] for k in dic_num_pericias if values[k]]
                atributos_distribuidos = [int(values[f'atributo_{a}']) for a in ATRIBUTOS]
                if sorted(atributos_distribuidos) != sorted(valores_sorteados):
                    sg.popup_error('Cada valor sorteado deve ser usado exatamente uma vez!')
                    continue

                window.close()
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

    def pegar_dados_basicos_ficha(self):
        print(' Dados Básicos Ficha '.center(60, '='))
        nome = self.le_str('Digite o nome do personagem: ')
        descricao_fisica = self.le_str('Digite uma breve descrição física: ', 'capitalize')
        historia = self.le_str('Digite, brevemente, a história do personagem: ', 'capitalize')
        moedas = self.le_int_ou_float('Digite quantas moedas o personagem tem: ',positivo=True)
        print('='*60)
        return {
            'nome_personagem': nome,
            'descricao_fisica': descricao_fisica,
            'historia': historia,
            'moedas': moedas
        }
    
    def pegar_dados_pericias(self):
        print('==== Pericias ====')
        print('[Força]')
        print('1. Atletismo')
        print('[Destreza]')
        print('2. Prestidigitação')
        print('3. Acrobacia')
        print('4. Furtividade')
        print('[Inteligência]')
        print('5. Arcanismo')
        print('6. História')
        print('7. Investigação')
        print('8. Natureza')
        print('9. Religião')
        print('[Sabedoria]')
        print('10. Percepção')
        print('11. Lidar com Animais')
        print('12. Intuição')
        print('13. Sobrevivência')
        print('14. Medicina')
        print('[Carisma]')
        print('15. Persuasão')
        print('16. Intimidação')
        print('17. Performance')
        print('18. Enganação')
        dic_num_pericias = {
            1: 'atletismo',
            2: 'prestidigitacao',
            3: 'acrobacia',
            4: 'furtividade',
            5: 'arcanismo',
            6: 'historia',
            7: 'investigacao',
            8: 'natureza',
            9: 'religiao',
            10: 'percepcao',
            11: 'lidar com animais',
            12: 'intuicao',
            13: 'sobrevivencia',
            14: 'medicina',
            15: 'persuasao',
            16: 'intimidacao',
            17: 'performance',
            18: 'enganacao'
        }
        pericias_treinadas = []
        valores_validos = list(range(1, 19))
        for i in range(5):
            num_pericia = self.le_int_ou_float(f'Selecione uma pericia ({i+1}/5): ', conjunto_alvo=valores_validos)
            pericias_treinadas.append(dic_num_pericias[num_pericia])
            valores_validos.remove(num_pericia)
        return pericias_treinadas

    def ler_vida_alterada(self):
        layout = [
            [sg.Text("Alterar Vida", font=("Arial", 24))],
            [sg.Radio('Dano', 'RD1', enable_events=True, key='dano'),
             sg.Radio('Cura', 'RD1', enable_events=True, key='cura')],
            [sg.Text('Vida: '), sg.InputText(size=(15, 1), enable_events=True, key='vida')],
            [sg.Submit('Confirmar', disabled=True), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Alterar vida').Layout(layout)

        while True:
            button, values = self.open()

            if button in (sg.WIN_CLOSED, 'Confirmar'):
                self.close()
                if values['dano']:
                    return -int(values['vida'])
                elif values['cura']:
                    return +int(values['vida'])
            elif button == 'Cancelar':
                self.close()
                return 0

            if values['vida'].isnumeric() and (values['dano'] or values['cura']):
                self.__window['Confirmar'].update(disabled=False)
            else:
                self.__window['Confirmar'].update(disabled=True)

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
            event, _ = window.read()
            if event in (sg.WINDOW_CLOSED, 'Fechar'):
                break
        window.close()

    def mostra_relatorio(self, dados):
        print("\n" + "=" * 30)
        print("RELATÓRIO DE PERSONAGENS")
        print("=" * 30)
        print(f">> Maior nível: {dados['maior_nivel'][0]} (nível {dados['maior_nivel'][1]})")
        print(f">> Mais rico: {dados['mais_ouro'][0]} ({dados['mais_ouro'][1]} moedas)")
        print(f">> Mais itens: {dados['mais_itens'][0]} ({dados['mais_itens'][1]} itens)")
        print(f">> Maior deslocamento: {dados['maior_deslocamento'][0]} ({dados['maior_deslocamento'][1]}m)")
        print(f">> Mais magias: {dados['mais_magias'][0]} ({dados['mais_magias'][1]} magias)")
        print(f">> Mais vida: {dados['maior_vida'][0]} ({dados['maior_vida'][1]} HP)")
        print(f">> Maior dado de vida: {dados['maior_dado_vida'][0]} ({dados['maior_dado_vida'][1]})")
        print(f">> Classe mais comum: {dados['classe_mais_comum'][0]} ({dados['classe_mais_comum'][1]} personagens)")
        print(f">> Perícia mais comum: {dados['pericia_mais_comum'][0]} ({dados['pericia_mais_comum'][1]} vezes)")
        print(f">> Personagem com mais habilidades: {dados['mais_hab'][0]} ({dados['mais_hab'][1]})")
        print(f">> Maior atributo registrado: {dados['maior_atributo']}")
        print(f">> Média de magias por personagem: {dados['media_magias']}")
        print("=" * 30 + "\n")

    @property
    def window(self):
        return self.__window

    @window.setter
    def window(self, window):
        if isinstance(window, sg.Window):
            self.__window = window
