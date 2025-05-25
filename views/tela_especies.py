from views.tela_abstrata import TelaAbstrata


class TelaEspecies(TelaAbstrata):
    
    def mostra_tela(self, opcoes = [1, 2, 0]):
        print('===== Especie/Subespecie =====')
        print('1. Gerir Especie')
        print('2. Gerir Subespecie')
        print('0. Retornar')
        return super().mostra_tela(opcoes)
    
    def mostra_tela_especie(self, opcoes = [1, 2, 3, 4, 5, 6, 0]):
        print('===== Especie =====')
        print('1. Criar Especie')
        print('2. Excluir Especie')
        print('3. Listar Especies')
        print('4. Modificar Especie')
        print('5. Adicionar Habilidade')
        print('6. Remover Habilidade')
        print('0. Retornar')
        return super().mostra_tela(opcoes)
    
    def mostra_tela_subespecie(self, opcoes = [1, 2, 3, 4, 5, 6, 0]):
        print('===== Subespecie =====')
        print('1. Criar Subespecie')
        print('2. Excluir Subespecie')
        print('3. Listar Subespecie')
        print('4. Modidicar Subespecie')    
        print('5. Adicionar Habilidade')
        print('6. Remover Habilidade')
        print('0. Retornar')
        return super().mostra_tela(opcoes)
    
    def pegar_dados_especie(self):
        print('===== Dados Especie =====')
        nome = input('Nome: ')
        deslocamento = self.le_int_ou_float('Deslocamento : ', tipo= 'float')
        altura = self.le_int_ou_float('Altura(cm): ', positivo= True)
        habilidades = []
        return {
            'nome': nome, 
            'deslocamento': deslocamento,
            'altura': altura,
            'habilidades': habilidades
            }
    
    def pegar_dados_subespecie(self, especie: str):
        print('===== Dados Subespecie =====')
        nome = input(f'Nome: {especie} ').strip()
        return {'nome': nome}
        
    def selecionar_obj_por_cod(self, obj, total_codigos):
        return super().selecionar_obj_por_cod(obj, total_codigos)
    
    def mostra_especie(self, dados_especie: dict):
        print(f"{dados_especie['cod']:^4}", end=' | ')
        print(f"{dados_especie['nome']:^16}", end=' | ')
        print(f"{dados_especie['deslocamento']:^16}", end=' | ')
        print(f"{dados_especie['altura']:^18}")
        print(f'===== Habilidades ====='.center(64, '='))
        print(f"{str(dados_especie['habilidades'])}")

    def mostra_subespecie(self, dados_subespecie: dict):
        self.mostra_especie(dados_subespecie)
        print(f'===== Habilidades específicas ====='.center(64, '='))
        print(f"{str(dados_subespecie['habilidades_esp'])}")
