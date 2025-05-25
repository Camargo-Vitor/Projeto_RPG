from views.tela_abstrata import TelaAbstrata
from random import randint

class TelaFichas(TelaAbstrata):
    def mostra_tela(self, opcoes=[1, 2, 3, 4, 0]):
        print('===== Fichas =====')
        print('1. Incluir Ficha')
        print('2. Listar Ficha')
        
        print('0. Retornar')
        return super().mostra_tela(opcoes)
    
    def pegar_dados_basicos_ficha(self):
        nome = self.le_str('Digite o nome do personagem: ')
        descricao_fisica = self.le_str('Digite uma breve descrição física: ', 'capitalize')
        historia = self.le_str('Digite, brevemente, a história do personagem: ', 'capitalize')
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
    
    def mostra_ficha(self, dados_ficha: dict):
        print(f"{dados_ficha['cod']:^4}", end= ' | ')
        print(f"{dados_ficha['nome']:^16}")
        
    def mostra_ficha_inteira(self, dados_ficha: dict):
        self.mostra_ficha()
        print(f"{dados_ficha['nivel']:^4}")
        print(f"{dados_ficha['vida']}")
        print(f"{dados_ficha['vida_atual']}")
        print(f"{dados_ficha['deslocamento']}")
        print(f"{dados_ficha['fisíco']}")
        print(f"{dados_ficha['altura']}")
        print(f"{dados_ficha['historia']}")
        print(f"{dados_ficha['classe']}")
        print(f"{dados_ficha['especie']}")
        print('><' * 8 + 'Utilitários' + '><' * 8)
        print(f"{dados_ficha['inventario']}")
        print(f"{dados_ficha['magias']}")
        print(f"{dados_ficha['habilidades']}")


        '''
        return '><' * 8 + 'Ficha de Personagem' + '><' * 8 + \
        f'\nNome: {self.nome}\
        \nVida: {self.vida}\
        \nNível: {self.nivel}\
        \nDeslocamento: {self.especie.deslocamento}\
        \nFisico: {self.fisico}\
        \nAltura: {self.altura}cm\
        \nHistória: {self.historia}\
        \nClasse: {self.classe.nome}\
        \nEspecie: {self.especie.nome}\n' + \
        '><' * 8 + 'Atributos' + '><' * 8 + f'\
        \nForça: {self.__atributos["forca"]} ({(self.__atributos["forca"] - 10) // 2})\
        \nDestreza: {self.__atributos["destreza"]} ({(self.__atributos["destreza"] - 10) // 2})\
        \nConstituição: {self.__atributos["constituicao"]} ({(self.__atributos["constituicao"] - 10) // 2})\
        \nInteligencia: {self.__atributos["inteligencia"]} ({(self.__atributos["inteligencia"] - 10) // 2})\
        \nSabedoria: {self.__atributos["sabedoria"]} ({(self.__atributos["sabedoria"] - 10) // 2})\
        \nCarisma: {self.__atributos["carisma"]} ({(self.__atributos["carisma"] - 10) // 2})\n' + \
        '><' * 8 + 'Utilitários' + '><' * 8 + f'\
        \nInventário: {"vazio" if self.inventario == [] else [str(x) for x in self.inventario]}\
        \nMagias: {"Nenhuma magia" if self.lista_magias == [] else [str(x) for x in self.lista_magias]}\
        \nHabilidades: {"Nenhuma habilidade" if self.habilidades == [] else [str(x) for x in self.habilidades]}'
        '''