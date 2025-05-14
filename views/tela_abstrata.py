from abc import ABC, abstractmethod
class TelaAbstrata(ABC):
    @abstractmethod
    def le_int(self, mensagem: str, conjunto_alvo: list=None, positivo: bool=False):
        while True:
            try: 
                num = int(input(mensagem))
                if (conjunto_alvo is not None) and (num not in conjunto_alvo):
                    raise ValueError
                if positivo and num < 0:
                    raise ValueError
                return num
            except ValueError:
                print('O valor digitado não é um inteiro válido. Tente novamente')
