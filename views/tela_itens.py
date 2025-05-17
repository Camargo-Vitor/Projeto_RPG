import os
from views.tela_abstrata import TelaAbstrata


class TelaItens(TelaAbstrata):
    def le_int_ou_float(self, mensagem, conjunto_alvo = None, positivo = False, tipo = 'int'):
        return super().le_int_ou_float(mensagem, conjunto_alvo, positivo, tipo)

    def mostra_tela(self):
        print('===== Item =====')
        print('1. Criar Item')
        print('2. Excluir Item')
        print('3. Listar Itens')
        print('4. Modificar Item')
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

    def pegar_dados_item(self):
        print('===== Dados Item =====')
        nome = input('Nome: ').strip().title()
        raridade = input('Raridade: ').strip().title()
        pagina = self.le_int_ou_float('Página: ', positivo=True)
        valor = self.le_int_ou_float('Valor: ', positivo=True)

        return {
                'nome': nome,
                'raridade': raridade,
                'pagina': pagina,
                'valor': valor
                }        

    def selecionar_obj_por_cod(self, obj, total_codigos):
        return super().selecionar_obj_por_cod(obj, total_codigos)

    def mostra_item(self, dados_item: dict):
        print(f"{dados_item['id']:^4}", end=' | ')
        print(f"{dados_item['nome']:^16}", end=' | ')
        print(f"{dados_item['raridade']:^10}", end=' | ')
        print(f"{dados_item['pagina']:^5}", end=' | ')
        print(f"{dados_item['valor']:^9}")

    def mensagem(self, msg):
        print(msg)
