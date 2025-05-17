from views.tela_especies import TelaEspecies
from model.especie import Especie
from model.subespecie import Subespecie
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller.controlador_sistema import ControladorSistema


class ControladorEspecies:
    def __init__(self, controlador_sistema: "ControladorSistema"):
        self.__controlador_sistema = controlador_sistema
        self.__dict_especie: dict[int, Especie] = dict()
        self.__dict_subespecie: dict[int, Subespecie] = dict()
        self.__tela_especies = TelaEspecies()
        self.__cod_esp = 1

    def pega_especie_por_nome(self, nome: str):
        for especie in self.__dict_especie.values():
            if especie.nome == nome:
                return especie
        return None
    
    def pega_subespecie_por_nome(self, nome: str):
        for subespecie in self.__dict_subespecie.values():
            if subespecie.nome == nome:
                return nome
        return None
    
    def incluir_especie(self):
        dados_especie = self.__tela_especies.pegar_dados_especie()
        e = self.pega_especie_por_nome(dados_especie['nome'])
        if e is None:
            especie = Especie(
                dados_especie['nome'],
                dados_especie['deslocamento'],
                dados_especie['altura'],
                dados_especie['habilidade(s)']
                    )
            self.__dict_especie[self.__cod_esp] = especie
            self.__cod_esp +=1
            self.__tela_especies.mensagem('Espécie criada com sucesso!')
        else:
            self.__tela_especies.mensagem('A espécie criada já existe')

    def listar_especies(self):
        self.__tela_especies.mensagem(f'{"Cod":^4} | {"Nome":^16} | {"Deslocamento":^16} | {"Altura(cm)":^12} | {"Habilidade(s)":^9}')
        for key, especie in self.__dict_especie.items():
            self.__tela_especies.mostra_especie(
                {
                    'cod': key,
                    'nome': especie.nome,
                    'deslocamento': especie.deslocamento,
                    'altura': especie.altura,
                    'habilidade(s)': especie.habilidades                 
                }
            )

    def excluir_especie(self):
        self.listar_especies()
        try:
            cod_validos = list(self.__dict_especie.keys()) + [0]
            identificador = self.__tela_especies.selecionar_obj_por_cod('especie', cod_validos)
            if identificador == 0:
                return
            del self.__dict_especie[identificador]
            print('Especie removida!')
            return True
        except:
            return False
        
    def alterar_especie_por_cod(self):
        self.listar_especies()
        try:
            cod_validos = list(self.__dict_especie.keys()) + [0]
            identificador = self.__tela_especies.selecionar_obj_por_cod('especie', cod_validos)
            if identificador == 0:
                return
            especie = self.dict_especie[identificador]
            dados_novos = self.tela_especie.pegar_especie_dados()
            especie.nome = dados_novos['nome']
            especie.deslocamento = dados_novos['deslocamento']
            especie.altura = dados_novos['altura']
            especie.habilidades = dados_novos ['habilidade']
            return True
        except:
            return False
        
    def retornar(self):
        self.controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.incluir_especie,
            2: self.excluir_especie,
            3: self.listar_especies,
            4: self.alterar_especie_por_cod,
            0: self.retornar
        }
        while True:
            opc = self.tela_especie.mostra_tela()
            metodo = opcoes[opc]
            metodo()



    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @property
    def tela_especie(self):
        return self.__tela_especies
    
    @property
    def dict_especie(self):
        return self.__dict_especie
    
    @property
    def dict_subespecie(self):
        return self.__dict_subespecie
