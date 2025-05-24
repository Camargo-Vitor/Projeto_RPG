from views.tela_abstrata import TelaAbstrata
from random import randint

class TelaFichas(TelaAbstrata):
    def mostra_tela(self, opcoes=[1, 2, 3, 4, 0]):
        print('===== Fichas =====')
        print('1. Incluir Ficha')
        print
        print('0. Retornar')
        return super().mostra_tela(opcoes)
    
    def pegar_dados_basicos_ficha(self):
        nome = input('Digite o nome do personagem: ').strip().title()
        descricao_fisica = input('Digite uma breve descrição física: ').strip().capitalize()
        historia = input('Digite, brevemente, a história do personagem: ')
        return {
            'nome_personagem': nome,
            'descricao_fisica': descricao_fisica,
            'historia': historia
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
        for i in range(5):
            num_pericia = self.le_int_ou_float(f'Selecione uma pericia ({i+1}/5): ', conjunto_alvo=list(range(1, 19)))
            pericias_treinadas.append(dic_num_pericias[num_pericia])
        return pericias_treinadas

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