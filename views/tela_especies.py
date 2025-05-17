import os
from views.tela_abstrata import TelaAbstrata


class TelaEspecies(TelaAbstrata):
    def le_int_ou_float(self, mensagem, conjunto_alvo = None, positivo = False, tipo = 'int'):
        return super().le_int_ou_float(mensagem, conjunto_alvo, positivo, tipo)

    def mostra_tela(self):
        print('===== Especie =====')
        print('1. Criar Especie')
        print('2. Excluir Especie')
        print('3. Listar Especies')
        print('4. Modificar Especie')
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
    
    def pegar_dados_especie(self):
        print('===== dados especie =====')
        nome = input('Nome: ')
        deslocamento = self.le_int_ou_float('Deslocamento : ', tipo= 'float')
        altura = self.le_int_ou_float('Altura(cm): ', positivo= True)
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
        print(f"{dados_especie['deslocamento']:^16}", end=' | ')
        print(f"{dados_especie['altura']:^12}", end=' | ')
        print(f"{str(dados_especie['habilidade(s)']):^9}")

    def mensagem(self, msg):
        print(msg)
            