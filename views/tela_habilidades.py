from views.tela_abstrata import TelaAbstrata
import os

class TelaHabilidades(TelaAbstrata):
    def le_int(self, mensagem, conjunto_alvo = None, positivo = False):
        return super().le_int(mensagem, conjunto_alvo, positivo)

    def mostra_tela(self):
        print('==== Habilidades ====')
        print('1. Criar Habilidade')
        print('2. Excluir Habilidade')
        print('3. Listar Habilidades')
        print('4. Modificar Habilidade')
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

    def pegar_dados_habilidade(self):
        nome = input('Digite o nome da habilidade: ').strip().title()
        nivel = self.le_int('Digite o nivel necessário: ', conjunto_alvo=[1, 2, 3])
        pagina = self.le_int('Digite a página da habilidade: ', positivo=True)

        while True:
            origem = input('Digite o tipo da habilidade (Classe, subclasse, especie ou subespecie): ').strip().capitalize()
            if origem.lower() in ('classe', 'subclasse', 'especie', 'subespecie'):
                break
            print('Opção inválida.')

        return {
            'nome': nome,
            'nivel': nivel,
            'pagina': pagina,
            'origem': origem
        }
