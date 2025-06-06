from views.tela_abstrata import TelaAbstrata


class TelaPessoas(TelaAbstrata):
    def mostra_tela(self, opcoes=[1, 2, 3, 4, 5, 6, 7, 0]):
        print('===== Pessoas =====')
        print('1. Incluir Jogador')
        print('2. Excluir Jogador')
        print('3. Listar Jogador')
        print('4. Alterar Jogador')
        print('5. Adicionar Ficha')
        print('6. Remover Ficha')
        print('7. Acessar Mestre')
        print('0. Retornar')
        return super().mostra_tela(opcoes)

    def pegar_dados_pessoa(self):
        print('==== Dados Pessoa ====')
        nome = self.le_str('Digite o nome: ')
        while True:
            telefone = self.le_int_ou_float(
                'Digite o número de telefone (com DDD, tudo junto): ', positivo=True)
            if len(str(telefone)) == 11:
                break
            else:
                print('Formato inválido')
        cidade = self.le_str('Digite a cidade: ')
        bairro = self.le_str('Digite o bairro: ')
        numero = self.le_int_ou_float('Digite o número do endereço: ', positivo=True)
        cep = self.le_int_ou_float('Digite o cep (somente numeros): ', positivo=True)
        return {
            'nome': nome,
            'telefone': telefone,
            'cidade': cidade,
            'bairro': bairro,
            'numero': numero,
            'cep': cep
        }

    def mostra_pessoa(self, dados_pessoa: dict):
        print(f"{dados_pessoa['cod']:^4}", end=' | ')
        print(f"{dados_pessoa['nome']:^16}", end=' | ')
        print(f"{dados_pessoa['telefone']:^13}", end=' | ')
        print(f"{dados_pessoa['cidade']:^16}", end=' | ')
        print(f"{dados_pessoa['bairro']:^12}", end=' | ')
        print(f"{dados_pessoa['numero']:^6}", end=' | ')
        print(f"{dados_pessoa['cep']:^10}", end=' |')

    def mostra_jogador(self, dados_jogador: dict):
        self.mostra_pessoa(dados_jogador)
        print(f"{dados_jogador['personagens']}")
