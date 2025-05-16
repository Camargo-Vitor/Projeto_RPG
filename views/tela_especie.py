from views.tela_abstrata import TelaAbstrata


class TelaEspecie(TelaAbstrata):
    def le_int(self, mensagem, conjunto_alvo = None, positivo = False):
        return super().le_int(mensagem, conjunto_alvo, positivo)

    def mostra_tela(self):
        print('===== Especie =====')
        print('1. Criar Especie')
        print('2. Excluir Especie')
        print('3. Listar Especie')
        print('4. Modificar Especie')
        print('0. Retornar')