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

    def le_int_ou_float(self, mensagem: str, conjunto_alvo: list=None, positivo: bool=False, tipo: str='int'):
        while True:
            try:
                if tipo not in ('int', 'float'):
                    raise ValueError("[ERRO] Tipo inválido. Esperado 'int' ou 'float'.")

                entrada = input(mensagem)

                try:
                    num = int(entrada) if tipo == 'int' else float(entrada)
                except ValueError:
                    if tipo == 'int':
                        raise ValueError('[ERRO] O valor digitado deve ser um número inteiro')
                    else:
                        raise ValueError('[ERRO] O valor digitado deve ser um número (utilize "." para decimais)')

                if (conjunto_alvo is not None) and (num not in conjunto_alvo):
                    raise ValueError("[ERRO] O valor digitado não está dentro do conjunto de valores válidos.")
                elif positivo and num < 0:
                    raise ValueError("[ERRO] O valor digitado deve ser positivo")

                return num

            except ValueError as e:
                print(e)
            except Exception as e :
                print(f'[ERRO INESPERADO] Ocorreu um erro inesperado: {str(e)}')

    def le_str(self, mensagem:str, formato='title'):
        entrada = ''
        while True:
            entrada = input(mensagem).strip()
            if not entrada.isnumeric() and not entrada == '':
                break
            print(f'[ERRO] Entrada inválida, não digite números ou espaços vazios.')

        if formato == 'title':
            return entrada.title()
        else:
            return entrada.capitalize()

    def selecionar_obj_por_cod(self, obj: str, total_codigos: list):
        try:
            print(f'===== Busca {obj.title()} =====')
            identificador = self.le_int_ou_float('Digite o Identificador desejado (0 para cancelar): ',
                                        conjunto_alvo = total_codigos
                                        )
            return identificador
        except Exception as e:
            print(f'[ERRO INESPERADO] Erro ao selecionar entidade por código: {e}')

    def mensagem(self, msg):
        print(msg)
