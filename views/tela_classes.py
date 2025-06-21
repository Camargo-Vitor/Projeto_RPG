from views.tela_abstrata import TelaAbstrata


class TelaClasses(TelaAbstrata):
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
    
    def pegar_dados_classes(self, basico=False):
        print('===== Dados Classe =====')
        nome = self.le_str('Digite o nome da classe: ')
        dado_vida = self.le_int_ou_float('Digite o número do dado de vida: ', positivo = True)
        if basico:
            return {
                'nome': nome,
                'dado': dado_vida
            }
        else:
            nomes_sub = []
            for a in range(3):
                #Por padrão todas as classes possuem 3 subclasses
                nome_sub = self.le_str(f'Digite o nome da {a+1} ª subclasse: ')
                nomes_sub.append(nome_sub)

            return {
                'nome': nome,
                'dado': dado_vida,
                'nomes_sub': nomes_sub,
            }

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
        pass

    @window.setter
    def window(self, window):
        pass