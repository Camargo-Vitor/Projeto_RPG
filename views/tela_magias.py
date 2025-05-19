from views.tela_abstrata import TelaAbstrata
import os


class TelaMagias(TelaAbstrata):
    def le_int_ou_float(self, mensagem, conjunto_alvo = None, positivo = False, tipo = 'int'):
        return super().le_int_ou_float(mensagem, conjunto_alvo, positivo, tipo)

    def mostra_tela(self):
        print('==== Magias ====')
        print('1. Criar Magia')
        print('2. Excluir Magia')
        print('3. Listar Magias')
        print('4. Modificar Magia')
        print('0. Retornar')

        opc = self.le_int_ou_float(
                    'Digite a opção: ',
                    conjunto_alvo = (0, 1, 2, 3, 4)
                    )

        if os.name == 'posix':
            os.system('clear')  
        else:
            os.system('cls')

        return opc

    def pegar_dados_magia(self):
        print('==== Dados Magia ====')
        nome = input('Digite o nome: ').strip().title()
        nivel = self.le_int_ou_float('Digite o nivel de desbloqueio (1-3): ', conjunto_alvo=[1, 2, 3])
        pagina = self.le_int_ou_float('Digite a página referência: ', positivo=True)
        return {
                'nome': nome,
                'nivel': nivel,
                'pagina': pagina
                }

    def selecionar_obj_por_cod(self, obj, total_codigos):
        return super().selecionar_obj_por_cod(obj, total_codigos)   

    def mostra_magia(self, dados_magia: dict):
        print(f"{dados_magia['cod']:^4}", end=' | ')
        print(f"{dados_magia['nome']:^16}", end=' | ')
        print(f"{dados_magia['nivel']:^5}", end=' | ')
        print(f"{dados_magia['pagina']:^5}")

    def mensagem(self, msg):
        print(msg)