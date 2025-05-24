from views.tela_abstrata import TelaAbstrata


class TelaClasses(TelaAbstrata):
    def mostra_tela(self, opcoes=[1, 2, 3, 4, 0]):
        print('===== Classes =====')
        print('1. Adicionar Classe')
        print('2. Excluir Classe')
        print('3. Listar Classes')
        print('4. Modificar Classes')
        print('0. Retornar ')
        return super().mostra_tela(opcoes)
    
    def pegar_dados_classes(self):
        print('===== Dados Classes =====')
        nome = input('Digite o nome da classe: ').strip().title()
        dado_vida = self.le_int_ou_float('Digite o número do dado de vida: ', positivo = True)
        habilidade = []
        habilidade_sub = []
        nomes_sub = []
        for a in range(3):
            #Por padrão todas as classes possuem 3 subclasses
            nome_sub = input(f'Digite o nome da {a+1} ª subclasse: ').strip().title()
            nomes_sub.append(nome_sub)

        return {
            'nome': nome,
            'dado': dado_vida,
            'nomes sub': nomes_sub,
            'habilidades': habilidade,
            'habilidades sub': habilidade_sub
        }

    def selecionar_obj_por_cod(self, obj, total_codigos):
        return super().selecionar_obj_por_cod(obj, total_codigos)
    
    def mostra_classe(self, dados_classe: dict):
        print(f"{dados_classe['cod']:^4}", end= ' | ')
        print(f"{dados_classe['nome']:^10}", end = ' | ')
        print(f"{dados_classe['dado']:^5}", end= ' | ')
        print(f"{str(dados_classe['habilidades']):^ 9}")

    def mostra_subclasse(self, dados_subclasse: dict):
        for a in range(3):
            print(f"{str(dados_subclasse['nomes sub'][a]):^13}", end= ' | ')
            print(f"{str(dados_subclasse['habilidades sub'][a]):^13}")



