import os
class TelaItem():
    def mostra_tela(self):
        print('===== Item =====')
        print('1. Criar Item')
        print('2. Excluir Item')
        print('3. Listar Itens')
        print('4. Modificar Item')
        print('0. Retornar')

        opc = int(input('Opção escolhida: '))

        if os.name == 'posix':
            os.system('clea')  
        else:
            os.system('cls')

        return opc

    def pegar_dados_item(self):
        print('===== Dados Item =====')
        nome = input('Nome: ')
        rariradade = input('Raridade: ')
        pagina = input('Página: ')
        valor = input('Valor: ')

        return {
                'nome': nome,
                'raridade': rariradade,
                'pagina': pagina,
                'valor': valor}        

    def selecionar_item_por_id(self):
        print('===== Busca Item =====')
        identificador = input('Digite o Identificador do Item desejado: ')
        return identificador

    def mostra_item(self, dados_item: dict):
        print(f"{dados_item['id']:^4}", end=' | ')
        print(f"{dados_item['nome']:^16}", end=' | ')
        print(f"{dados_item['raridade']:^10}", end=' | ')
        print(f"{dados_item['pagina']:^5}", end=' | ')
        print(f"{dados_item['valor']:^9}")

    def mensagem(self, msg):
        print(msg)
