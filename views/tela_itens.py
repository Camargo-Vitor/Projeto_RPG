from views.tela_abstrata import TelaAbstrata


class TelaItens(TelaAbstrata):

    def mostra_tela(self, opcoes=[1, 2, 3, 4, 0]):
        print('===== Item =====')
        print('1. Criar Item')
        print('2. Excluir Item')
        print('3. Listar Itens')
        print('4. Modificar Item')
        print('0. Retornar')
        return super().mostra_tela(opcoes)

    def pegar_dados_item(self):
        print('===== Dados Item =====')
        nome = self.le_str('Nome: ')
        raridade = self.le_str('Raridade: ')
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
        print(f"{dados_item['cod']:^4}", end=' | ')
        print(f"{dados_item['nome']:^16}", end=' | ')
        print(f"{dados_item['raridade']:^10}", end=' | ')
        print(f"{dados_item['pagina']:^5}", end=' | ')
        print(f"{dados_item['valor']:^9}")
