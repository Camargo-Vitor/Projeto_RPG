from views.tela_abstrata import TelaAbstrata


class TelaClasses(TelaAbstrata):
    def mostra_tela(self, opcoes=...):
        print('1. Adicionar Classe')
        print('2. Excluir Classe')
        print('3. Listar Classes')
        print('4. Modificar Classes')
        print('0. Retornar')
        return super().mostra_tela(opcoes)