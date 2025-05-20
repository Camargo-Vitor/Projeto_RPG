from views.tela_abstrata import TelaAbstrata


class TelaPessoas(TelaAbstrata):
    def le_int_ou_float(self, mensagem, conjunto_alvo = None, positivo = False, tipo = 'int'):
        return super().le_int_ou_float(mensagem, conjunto_alvo, positivo, tipo)

    def mostra_tela(self, opcoes=[1, 2, 0]):
        print('==== Pessoas ====')
        print('1. Gerir Mestres')
        print('2. Gerir Jogadores')
        print('0. Voltar')
        return super().mostra_tela(opcoes)

    def mostra_tela_mestre(self, opcoes=[1, 2, 3, 4, 0]):
        print('==== Mestre ====')
        print('1. Criar Mestre')
        print('2. Excluir Mestre')
        print('3. Listar Mestres')
        print('4. Alterar Mestre')
        return super().mostra_tela(opcoes)
        
    def mostra_tela_jogador(self, opcoes=[1, 2, 3, 4, 0]):
        print('==== Jogador ====')
        print('1. Criar Jogador')
        print('2. Excluir Jogador')
        print('3. Listar Jogadores')
        print('4. Alterar Jogador')
        return super().mostra_tela(opcoes)
