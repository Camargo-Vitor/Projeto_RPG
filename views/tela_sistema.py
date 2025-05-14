import os
from views.tela_abstrata import TelaAbstrata
class TelaSistema(TelaAbstrata):
    def le_int(self, mensagem, conjunto_alvo = None, positivo = False):
        return super().le_int(mensagem, conjunto_alvo, positivo)

    def mostra_tela(self):
        print('===== Sistema =====')
        print('1. Item')
        print('2. Magia')
        print('3. Habilidade')
        print('4. Espécie')
        print('5. Classe')
        print('6. Ficha')
        print('7. Pessoa')
        print('0. sair')

        opc = self.le_int(
                          'Digite a opção: ',
                          conjunto_alvo = (0, 1, 2, 3, 4, 5, 6, 7)
                          )

        if os.name == 'posix':
            os.system('clear')  
        else:
            os.system('cls')

        return opc
