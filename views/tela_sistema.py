import os
class TelaSistema:
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

        opc = int(input('Digite a opção escolhida: '))

        if os.name == 'posix':
            os.system('clear')  
        else:
            os.system('cls')

        return opc
