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
        self.__dict__classes : dict[int, Classe] = {
            1000: Classe('Classe_teste', 6, ['Sub_teste1', 'Sub_teste2', 'Sub_teste3'])
        }
        
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
                dados_classe['nomes_sub']
            )
            self.__dict__classes[self.__cod] = classe
            self.__cod += 1
            self.__tela_classes.mensagem('Classe criada com sucesso!')
        else:
            self.__tela_classes.mensagem('A classe criada ja existe!')
    
    def listar_classes_e_subclasses(self, classes=True, subclasses=True):
        try:
            for key, classe in self.__dict__classes.items():
                self.__tela_classes.mostra_classe_e_subclasse(
                    {
                        'cod': key,
                        'nome': classe.nome,
                        'dado': classe.dado_vida,
                        'habilidades': [hab.nome for hab in classe.habilidades],
                        'nomes_sub': [sub.nome for sub in classe.subclasses],
                        'habilidades_sub': [[hab.nome for hab in sub.hab_especificas] for sub in classe.subclasses]
                    }, 
                    classe=classes, subclasse=subclasses
                )

        except Exception as e:
            self.__tela_classes.mensagem(f'ERRO INESPERADO Erro ao listar classe: {e}')

    def excluir_classe(self):
        try:
            self.listar_classes_e_subclasses(subclasses=False)
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

    def alterar_dados_base_classe(self):
        try:
            self.listar_classes_e_subclasses(subclasses=False)
            codigos_validos = list(self.__dict__classes.keys()) + [0]
            identificador = self.__tela_classes.le_int_ou_float(
                'Digite o código da classe: (0 para cancelar) ',
                conjunto_alvo=codigos_validos
            )
            if identificador == 0:
                return False
            else:
                classe = self.__dict__classes[identificador]
                novos_dados = self.__tela_classes.pegar_dados_classes(basico=True)
                classe.nome = novos_dados['nome']
                classe.dado_vida = novos_dados['dado']
        except Exception as e:
            self.__tela_classes.mensagem(f'[ERRO INESPERADO] Erro ao modificar dados base de classe: {e}') 

    def adiciona_hab_classe(self):
        try:
            self.listar_classes_e_subclasses(subclasses=False)
            codigos_validos = list(self.__dict__classes.keys()) + [0]
            identificador = self.__tela_classes.le_int_ou_float(
                'Digite o código da classe: (0 para cancelar) ',
                conjunto_alvo=codigos_validos
            )
            if identificador == 0:
                return False
            else:
                classe = self.__dict__classes[identificador]
                self.__controlador_sistema.controlador_habilidades.listar_habilidades(origem='classe')
                codigos_validos = list(self.__controlador_sistema.controlador_habilidades.dict_habilidades.keys()) + [0]
                identificador = self.__tela_classes.le_int_ou_float(
                    'Digite o código da Habilidade: (0 para cancelar) ',
                    conjunto_alvo=codigos_validos
                )
                if identificador == 0:
                    return False
                else:
                    habilidade = self.__controlador_sistema.controlador_habilidades.dict_habilidades[identificador]
                    classe.add_hab(habilidade)
                    self.__tela_classes.mensagem('Habilidade adicionada com sucesso!')
                    return True
        except ValueError as e:
            self.__tela_classes.mensagem(e)
        except Exception as e:
            self.__tela_classes.mensagem(f'[ERRO INESPERADO] Erro ao adicionar habilidade em classe: {e}')

    def adiciona_hab_subclasse(self):
        try:
            self.listar_classes_e_subclasses(subclasses=False)
            codigos_validos = list(self.__dict__classes.keys()) + [0]
            identificador = self.__tela_classes.le_int_ou_float(
                'Digite o código da classe: (0 para cancelar) ',
                conjunto_alvo=codigos_validos
            )
            if identificador == 0:
                return False
            else:
                classe = self.__dict__classes[identificador]
                infos = {'nomes_sub': [sub.nome for sub in classe.subclasses],
                         'habilidades_sub': [[hab.nome for hab in sub.hab_especificas] for sub in classe.subclasses]}
                self.tela_classes.mostra_classe_e_subclasse(infos, classe=False)
                identificador = self.__tela_classes.le_int_ou_float(
                    'Digite qual a subclasse (1, 2 ou 3 - de cima para baixo): ',
                    conjunto_alvo=[1, 2, 3]
                )
                if identificador == 0:
                    return False
                else:
                    subclasse = classe.subclasses[identificador-1]    
                    self.__controlador_sistema.controlador_habilidades.listar_habilidades(origem='subclasse')
                    codigos_validos = list(self.__controlador_sistema.controlador_habilidades.dict_habilidades.keys()) + [0]
                    identificador = self.__tela_classes.le_int_ou_float(
                        'Digite o código da Habilidade: (0 para cancelar) ',
                        conjunto_alvo=codigos_validos
                    )
                    if identificador == 0:
                        return False
                    else:
                        habilidade = self.__controlador_sistema.controlador_habilidades.dict_habilidades[identificador]
                        subclasse.add_hab(habilidade)
                        self.__tela_classes.mensagem('Habilidade adicionada com sucesso!')
                        return True
        except ValueError as e:
            self.__tela_classes.mensagem(e)
        except Exception as e:
            self.__tela_classes.mensagem(f'[ERRO INESPERADO] Erro ao adicionar habilidade em subclasse: {e}')

    def remover_hab_classe(self):
        try:
            self.listar_classes_e_subclasses(subclasses=False)
            codigos_validos = list(self.__dict__classes.keys()) + [0]
            identificador = self.__tela_classes.le_int_ou_float(
                'Digite o código da classe: (0 para cancelar) ',
                conjunto_alvo=codigos_validos
            )
            if identificador == 0:
                return False
            else:
                todas_habilidades = self.__controlador_sistema.controlador_habilidades.dict_habilidades
                classe = self.__dict__classes[identificador]
                self.__controlador_sistema.controlador_habilidades.listar_habilidades('classe')
                codigos_validos = list(todas_habilidades.keys()) + [0]
                identificador = self.__tela_classes.le_int_ou_float(
                    'Digite o identificador da habilidade que deseja excluir (0 para cancelar): ',
                    conjunto_alvo=codigos_validos
                )
                if identificador == 0:
                    return False
                elif todas_habilidades[identificador] not in classe.habilidades:
                    raise KeyError("[ERRO DE CHAVE] A habilidade selecionada é inválida.")
                else:
                    classe.rm_hab(todas_habilidades[identificador])
                    self.__tela_classes.mensagem('Habilidade removida com sucesso!')
                    return True

        except KeyError as e: 
            self.__tela_classes.mensagem(e)
        except Exception as e:
            self.__tela_classes.mensagem(f'[ERRO INESPERADO] Erro ao excluir habilidade em classe: {e}')

    def remover_hab_subclasse(self):
        try:
            self.listar_classes_e_subclasses(subclasses=False)
            codigos_validos = list(self.__dict__classes.keys()) + [0]
            identificador = self.__tela_classes.le_int_ou_float(
                'Digite o código da classe: (0 para cancelar) ',
                conjunto_alvo=codigos_validos
            )
            if identificador == 0:
                return False
            else:
                classe = self.__dict__classes[identificador]
                infos = {'nomes_sub': [sub.nome for sub in classe.subclasses],
                         'habilidades_sub': [[hab.nome for hab in sub.hab_especificas] for sub in classe.subclasses]}
                self.tela_classes.mostra_classe_e_subclasse(infos, classe=False)
                identificador = self.__tela_classes.le_int_ou_float(
                    'Digite qual subclasse (1, 2 ou 3 - de cima para baixo): ',
                    conjunto_alvo=[1, 2, 3]
                )
                if identificador == 0:
                    return False
                else:
                    subclasse = classe.subclasses[identificador-1]
    
                    self.__controlador_sistema.controlador_habilidades.listar_habilidades(origem='subclasse')
                    codigos_validos = list(self.__controlador_sistema.controlador_habilidades.dict_habilidades.keys()) + [0]
                    identificador = self.__tela_classes.le_int_ou_float(
                        'Digite o código da Habilidade: (0 para cancelar) ',
                        conjunto_alvo=codigos_validos
                    )
                    if identificador == 0:
                        return False
                    else:
                        habilidade = self.__controlador_sistema.controlador_habilidades.dict_habilidades[identificador]
                        subclasse.rm_hab(habilidade)
                        self.__tela_classes.mensagem('Habilidade removida com sucesso!')
                        return True

        except ValueError as e:
            self.__tela_classes.mensagem(e)
        except Exception as e:
            self.__tela_classes.mensagem(f'[ERRO INESPERADO] Erro ao adicionar habilidade em subclasse: {e}')
      
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.incluir_classe,
            2: self.excluir_classe,
            3: self.listar_classes_e_subclasses,
            4: self.alterar_dados_base_classe,
            5: self.adiciona_hab_classe,
            6: self.remover_hab_classe,
            7: self.adiciona_hab_subclasse,
            8: self.remover_hab_subclasse,
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
