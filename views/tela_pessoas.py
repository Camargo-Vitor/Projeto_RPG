from views.tela_abstrata import TelaAbstrata
import os 


class TelaPessoas(TelaAbstrata):
    def le_int_ou_float(self, mensagem, conjunto_alvo = None, positivo = False, tipo = 'int'):
        return super().le_int_ou_float(mensagem, conjunto_alvo, positivo, tipo)

    def mostra_tela(self):
        print('==== Pessoas ====')
        print('1. Gerir Mestres')
        print('2. Gerir Jogadores')
        print('0. Voltar')
        
        opc = self.le_int_ou_float(
                    'Digite a opção: ',
                    conjunto_alvo = (0, 1, 2)
                    )

        if os.name == 'posix':
            os.system('clear')  
        else:
            os.system('cls')

        return opc

    def mostra_tela_mestre(self):
        print('==== Mestre ====')

        opc = self.le_int_ou_float(
                    'Digite a opção: ',
                    conjunto_alvo = (0, 1, 2)
                    )

        if os.name == 'posix':
            os.system('clear')  
        else:
            os.system('cls')

        return opc
        
    def mostra_tela_jogador(self):
        print('==== Jogador ====')
        
        opc = self.le_int_ou_float(
                    'Digite a opção: ',
                    conjunto_alvo = (0, 1, 2)
                    )

        if os.name == 'posix':
            os.system('clear')  
        else:
            os.system('cls')

        return opc
