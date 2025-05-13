class TelaItem():
    def mostra_tela(self):
        print('===== Item =====')
        print('1. Criar Item')
        print('2. Excluir Item')
        print('3. Listar Itens')
        print('4. Modificar Item')
        print('0. Retornar')

        opc = int(input('Opção escolhida: '))
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
        print(
            dados_item['id'], '|',
            dados_item['nome'], '|',
            dados_item['raridade'], '|',
            dados_item['pagina'], '|',
            dados_item['valor']) 

    def mensagem(self, msg):
        print(msg)