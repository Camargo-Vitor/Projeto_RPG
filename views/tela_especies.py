import os
from views.tela_abstrata import TelaAbstrata


class TelaEspecies(TelaAbstrata):
    def le_int(self, mensagem, conjunto_alvo = None, positivo = False):
        return super().le_int(mensagem, conjunto_alvo, positivo)

    def mostra_tela(self):
        print('===== Especie =====')
        print('1. Criar Especie')
        print('2. Excluir Especie')
        print('3. Listar Especies')
        print('4. Modificar Especie')
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
    
    def pegar_especie_dados(self):
        print('===== dados especie =====')
        nome = input('Nome:')
        deslocamento = input('Deslocamento: ')
        altura = self.le_int('Altura: ', positivo= True)
        habilidades = []
        print('===== insira "0" quando não desejar inserir mais habilidades =====')
        while True:
            habilidade = input('Habilidade: ')
            if not habilidade == '0':
                habilidades.append(habilidade)
            else:
                break
        return{
            'nome': nome, 
            'deslocamento': deslocamento,
            'altura': altura,
            'habilidade(s)': habilidades  
            }
        
    def selecionar_obj_por_cod(self, obj, total_codigos):
        return super().selecionar_obj_por_cod(obj, total_codigos)
    
    def mostra_especie(self, dados_especie: dict):
        print(f"{dados_especie['cod']:^4}", end=' | ')
        print(f"{dados_especie['nome']:^16}", end=' | ')
        print(f"{dados_especie['deslocamento']:^10}", end=' | ')
        print(f"{dados_especie['altura']:^5}", end=' | ')
        print(f"{dados_especie['habilidade(s)']:^9}")

    def mensagem(self, msg):
        print(msg)
            