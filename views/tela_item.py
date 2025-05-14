import os
from views.tela_abstrata import TelaAbstrata
class TelaItem(TelaAbstrata):
    def le_int(self, mensagem, conjunto_alvo = None, positivo = False):
        return super().le_int(mensagem, conjunto_alvo, positivo)

    def mostra_tela(self):
        print('===== Item =====')
        print('1. Criar Item')
        print('2. Excluir Item')
        print('3. Listar Itens')
        print('4. Modificar Item')
        print('0. Retornar')

        opc = self.le_int(
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
        pagina = self.le_int('Página: ', positivo=True)
        valor = self.le_int('Valor: ', positivo=True)

        return {
                'nome': nome,
                'raridade': raridade,
                'pagina': pagina,
                'valor': valor
                }        

    def selecionar_item_por_id(self, total_ids: list):
        print('===== Busca Item =====')
        identificador = self.le_int('Digite o Identificador do Item desejado (0 para cancelar): ',
                                    conjunto_alvo = total_ids
                                    )
        return identificador

    def mostra_item(self, dados_item: dict):
        print(f"{dados_item['id']:^4}", end=' | ')
        print(f"{dados_item['nome']:^16}", end=' | ')
        print(f"{dados_item['raridade']:^10}", end=' | ')
        print(f"{dados_item['pagina']:^5}", end=' | ')
        print(f"{dados_item['valor']:^9}")

    def mensagem(self, msg):
        print(msg)
