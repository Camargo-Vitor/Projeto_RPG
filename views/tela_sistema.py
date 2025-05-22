from views.tela_abstrata import TelaAbstrata


class TelaSistema(TelaAbstrata):

    def mostra_tela(self, opcoes=[1, 2, 3, 4, 5, 6, 7, 0]):
        print('===== Sistema =====')
        print('1. Item')
        print('2. Magia')
        print('3. Habilidade')
        print('4. Espécie')
        print('5. Classe')
        print('6. Ficha')
        print('7. Pessoa')
        print('0. sair')
        return super().mostra_tela(opcoes)
