from views.tela_abstrata import TelaAbstrata
from random import randint

class TelaFichas(TelaAbstrata):
    def mostra_tela(self, opcoes=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]):
        print('===== Fichas =====')
        print('1. Incluir Ficha')
        print('2. Excluir Ficha')
        print('3. Listar Ficha')
        print('4. Alterar vida de uma ficha')
        print('5. Subir nivel de uma ficha')
        print('6. Adicionar item em ficha')
        print('7. Remover item ficha')
        print('8. Adicionar maiga em ficha')
        print('9. Remover magia em ficha')
        print('10. Relatório de fichas')
        print('0. Retornar')
        return super().mostra_tela(opcoes)

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
    
    def mostra_ficha_basica(self, dados_ficha: dict):
        print(f"{dados_ficha['cod']:^4}", end= ' | ')
        print(f"{dados_ficha['nome']:^16}")
        
    def mostra_ficha_inteira(self, dados_ficha: dict):
        print(f"Nome: {dados_ficha['nome']}")
        print(f"Nivel: {dados_ficha['nivel']:^4}")
        print(f"Vida: {dados_ficha['vida_atual']}/{dados_ficha['vida']}")
        print(f"Moedas: {dados_ficha['moedas']}")
        print(f"Descrição física: {dados_ficha['fisico']}")
        print(f"História: {dados_ficha['historia']}")
        print(f"Altura: {dados_ficha['altura']}")
        print(f"Deslocamento: {dados_ficha['deslocamento']}")
        print(f"Pericias Treinadas: {dados_ficha['pericias']}")
        print(f"Classe: {dados_ficha['classe']}")
        print(f"Especie: {dados_ficha['especie']}")
        print('><' * 8 + 'Atributos' + '><' * 8)
        print(f"Forca: {dados_ficha['forca']}")
        print(f"Destreza: {dados_ficha['destreza']}")
        print(f"Constituição: {dados_ficha['constituicao']}")
        print(f"Inteligência: {dados_ficha['inteligencia']}")
        print(f"Sabedoria: {dados_ficha['sabedoria']}")
        print(f"Carisma: {dados_ficha['carisma']}")
        print('><' * 8 + 'Utilitários' + '><' * 8)
        print(f"Inventário: {dados_ficha['inventario']}")
        print(f"Magias: {dados_ficha['magias']}")
        print(f"Habilidades: {dados_ficha['habilidades']}")

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
