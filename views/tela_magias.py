from views.tela_abstrata import TelaAbstrata


class TelaMagias(TelaAbstrata):

    def mostra_tela(self, opcoes=[1, 2, 3, 4, 0]):
        print('===== Magias =====')
        print('1. Criar Magia')
        print('2. Excluir Magia')
        print('3. Listar Magias')
        print('4. Modificar Magia')
        print('0. Retornar')
        return super().mostra_tela(opcoes)

    def pegar_dados_magia(self):
        print('==== Dados Magia ====')
        nome = self.le_str('Digite o nome: ')
        nivel = self.le_int_ou_float('Digite o nivel de desbloqueio: ', positivo=True)
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
