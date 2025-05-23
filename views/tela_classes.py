from views.tela_abstrata import TelaAbstrata


class TelaClasses(TelaAbstrata):
    def mostra_tela(self, opcoes=...):
        print('1. Adicionar Classe')
        print('2. Excluir Classe')
        print('3. Listar Classes')
        print('4. Modificar Classes')
        print('0. Retornar ')
        return super().mostra_tela(opcoes)
    
    def pegar_dados_classes(self):
        print('===== Dados Classes =====')
        nome = input('Digite o nome da classe: ').strip().title()
        dado_vida = input('Digite o dado de vida: ').strip().title()
        habilidade = []
        habilidade_sub = []
        nomes_sub = []
        for a in range(3):
            nome_sub = input('Digite o nome da subclasse: ').strip().title()
            nomes_sub.append(nome_sub)

        return {
            'nome': nome,
            'dado': dado_vida,
            'nome sub': nomes_sub,
            'habilidades': habilidade,
            'habilidades sub': habilidade_sub
        }

    def selecionar_obj_por_cod(self, obj, total_codigos):
        return super().selecionar_obj_por_cod(obj, total_codigos)
    
    def mostra_classes(self, dados_classe: dict):
        pass



