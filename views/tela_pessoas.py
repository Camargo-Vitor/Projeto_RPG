from views.tela_abstrata import TelaAbstrata


class TelaPessoas(TelaAbstrata):
    def mostra_tela(self):
        print('==== Pessoas ====')
        print('1. Gerir Mestres')
        print('2. Gerir Jogadores')

    