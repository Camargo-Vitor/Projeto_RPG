from abc import ABC, abstractmethod
import os

class TelaAbstrata(ABC):
    @abstractmethod
    def mostra_tela(self, opcoes=[]):
        opc = self.le_int_ou_float(
            'Digite a opção: ',
            conjunto_alvo = opcoes
                    )

        if os.name == 'posix':
            os.system('clear')  
        else:
            os.system('cls')

        return opc

    @abstractmethod
    def le_int_ou_float(self, mensagem: str, conjunto_alvo: list=None, positivo: bool=False, tipo: str='int'):
        while True:
            try:
                if tipo == 'int': 
                    num = int(input(mensagem))
                elif tipo == 'float':
                    num = float(input(mensagem))
                else:
                    raise ValueError
                if (conjunto_alvo is not None) and (num not in conjunto_alvo):
                    raise ValueError
                if positivo and num < 0:
                    raise ValueError
                return num
            except ValueError:
                print('O valor digitado não é um número válido. Tente novamente')

    def selecionar_obj_por_cod(self, obj: str, total_codigos: list):
        print(f'===== Busca {obj.title()} =====')
        identificador = self.le_int_ou_float('Digite o Identificador desejado (0 para cancelar): ',
                                    conjunto_alvo = total_codigos
                                    )
        return identificador

    def mensagem(self, msg):
        print(msg)