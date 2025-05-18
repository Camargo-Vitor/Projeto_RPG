from model.habilidade import Habilidade
from views.tela_habilidades import TelaHabilidades
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller.controlador_sistema import ControladorSistema


class ControladorHabilidades:

    def __init__(self, controlador_sistema: "ControladorSistema"):
        self.__controlador_sistema = controlador_sistema
        self.__tela_habilidades = TelaHabilidades()
        self.__dict_habilidades: dict[int, Habilidade] = dict()
        self.__cod = 1

    def pega_habilidade_por_nome(self, nome: str):
        for hab in self.__dict_habilidades.values():
            if hab.nome == nome:
                return hab
        return None
    
    def incluir_habilidade(self):
        dados_hab = self.__tela_habilidades.pegar_dados_habilidade()
        hab = self.pega_habilidade_por_nome(dados_hab['nome'])
        if hab == None:
            nova_habilidade = Habilidade(
                dados_hab['nome'],
                dados_hab['nivel'],
                dados_hab['pagina'],
                dados_hab['origem']
            )
            self.__dict_habilidades[self.__cod] = nova_habilidade
            self.__cod += 1
            self.__tela_habilidades.mensagem('Habilidade criada com sucesso!')
        else:
            self.tela_habilidade.mensagem(f'ATENÇÃO: A habilidade "{dados_hab["nome"]}" já existe')
        return False
    
    def listar_habilidades(self):
        self.__tela_habilidades.mensagem(f"{'cod':^4} | {'nome':^16} | {'nível':^5} | {'pagina':^6} | {'origem':^10}")
        for key, habilidade in self.__dict_habilidades.items():
            self.__tela_habilidades.mostra_habilidade(
                {
                'cod': key ,
                'nome': habilidade.nome,
                'nivel': habilidade.nivel,
                'pagina': habilidade.pagina,
                'origem': habilidade.origem
                }
            )
    
    def excluir_habilidade(self):
        self.listar_habilidades()
        try:
            cod_validos = list(self.__dict_habilidades.keys()) + [0]
            identificador = self.__tela_habilidades.selecionar_obj_por_cod('habilidade', cod_validos)
            if identificador == 0:
                return
            else:
                del self.__dict_habilidades[identificador]
                self.__tela_habilidades.mensagem('Habilidade removida!')
                return True
        except:
            return False

    def alterar_habilidade_por_cod(self):
        self.listar_habilidades()
        try:
            cod_validos = list(self.__dict_habilidades.keys()) + [0]
            identificador = self.__tela_habilidades.selecionar_obj_por_cod('habilidades', cod_validos)
            if identificador == 0:
                return
            else:
                habilidade = self.__dict_habilidades[identificador]
                dados_novos = self.__tela_habilidades.pegar_dados_habilidade()
                habilidade.nome = dados_novos['nome']
                habilidade.nivel = dados_novos['nivel']
                habilidade.pagina = dados_novos['pagina']
                habilidade.pagina = dados_novos['origem']
                return True
        except:
            return False

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.incluir_habilidade,
            2: self.excluir_habilidade,
            3: self.listar_habilidades,
            4: self.alterar_habilidade_por_cod,
            0: self.retornar
        }
        while True:
            opc = self.__tela_habilidades.mostra_tela()
            metodo = opcoes[opc]
            metodo()

    @property
    def tela_habilidade(self):
        return self.__tela_habilidades
    
    @property
    def dict_habilidades(self):
        return self.__dict_habilidades