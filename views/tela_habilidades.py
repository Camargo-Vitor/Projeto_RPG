from views.tela_abstrata import TelaAbstrata


class TelaHabilidades(TelaAbstrata):
    def mostra_tela(self, opcoes=[1, 2, 3, 4, 0]):
        print('===== Habilidades =====')
        print('1. Criar Habilidade')
        print('2. Excluir Habilidade')
        print('3. Listar Habilidades')
        print('4. Modificar Habilidade')
        print('0. Retornar')
        return super().mostra_tela(opcoes)

    def pegar_dados_habilidade(self):
        print('===== Dados Habilidades =====')
        nome = self.le_str('Digite o nome da habilidade: ').strip().title()
        nivel = self.le_int_ou_float('Digite o nivel necessário: ', positivo= True)
        pagina = self.le_int_ou_float('Digite a página da habilidade: ', positivo=True)


        while True:
            print('1. Classe')
            print('2. Subclasse')
            print('3. Especie')
            print('4. Subespecie')

            opc = self.le_int_ou_float(
                'Digite o tipo da habilidade: ',
                conjunto_alvo = (1, 2, 3, 4)
            )
            opcoes = {1: 'classe',
                      2: 'subclasse',
                      3: 'especie',
                      4: 'subespecie'}
            
            origem = opcoes[opc]

            return {
            'nome': nome,
            'nivel': nivel,
            'pagina': pagina,
            'origem': origem
        }
    
    def mostra_habilidade(self, dados_habilidade: dict):
        print(f"{dados_habilidade['cod']:^4}", end= ' | ')
        print(f"{dados_habilidade['nome']:^16}", end = ' | ')
        print(f"{dados_habilidade['nivel']:^5}", end= ' | ')
        print(f"{dados_habilidade['pagina']:^6}", end= ' | ')
        print(f"{dados_habilidade['origem']:^10}")

    @property
    def window(self):
        pass

    @window.setter
    def window(self, window):
        pass