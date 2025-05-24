from model.classe import Classe
from model.subclasse import Subclasse
from views.tela_classes import TelaClasses
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controlador_sistema import ControladorSistema


class ControladorClasses:
    def __init__(self, controlador_sistema: "ControladorSistema"):
        self.__controlador_sistema = controlador_sistema
        self.__tela_classes = TelaClasses()
        self.__dict__classes : dict[int, Classe] = dict()
        self.__cod = 1

    def pega_classe_por_nome(self, nome: str):
        for classe in self.__dict__classes.values():
            if classe.nome== nome:
                return classe
        return None
    
    def incluir_classe(self):
        dados_classe = self.__tela_classes.pegar_dados_classes()
        c = self.pega_classe_por_nome(dados_classe['nome'])
        if c is None:
                classe = Classe(
                    dados_classe['nome'],
                    dados_classe['dado'],
                    dados_classe['nome sub']
                )
                self.__dict__classes[self.__cod] = classe
                self.__cod += 1
                self.__tela_classes.mensagem('Classe criada com sucesso!')
                print(classe)
                print(classe.__subclasses)
        else:
            self.__tela_classes.mensagem('A classe criada ja existe!')
    
    def listar_classes(self):
        try:
            self.__tela_classes.mensagem(f"{'Cod':^4} | {'Nome':^10} | {'Dado':^5}")
            for key, classe in self.__dict__classes.items():
                self.__tela_classes.mostra_classe(
                    {
                        'cod': key,
                        'nome': classe.nome,
                        'dado': classe.dado_vida,
                        'habilidades': [hab.nome for hab in classe.habilidades],
 
                    }
                )
           # self.__tela_classes.mensagem(f"{'Nome sub':^13} | {'Habilidades':^9}")
           # for sub_classe in self.__dict__classes.items():
                #self.__tela_classes.mostra_subclasse(
                        #{
                        #    'nomes sub': sub_classe,
                        #    'habilidades_sub':  sub_classe
                        #    }
               # )
        except Exception as e:
            self.tela_classes.mensagem(f'ERRO INESPERADO Erro ao listar classe: {e}')

    def excluir_classe(self):
        try:
            self.listar_classes()
            cod_validos = list(self.__dict__classes.keys()) + [0]
            identificador = self.__tela_classes.selecionar_obj_por_cod('classe', cod_validos)
            if identificador == 0:
                return False
            else:
                del self.__dict__classes[identificador]
                self.__tela_classes.mensagem('Classe removida!')
                return True
        except Exception as e:
            self.__tela_classes.mensagem(f'[ERRO INESPERADO] Erro ao excluir classe: {e}') 
            
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.incluir_classe,
            2: self.listar_classes,
            3: self.excluir_classe,
            0: self.retornar
        }

        while True:
            opc = self.__tela_classes.mostra_tela()
            metodo = opcoes[opc]
            metodo()

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
    
    @property
    def tela_classes(self):
        return self.__tela_classes
    
    @property
    def dict_classes(self):
        return self.__dict__classes
            
        