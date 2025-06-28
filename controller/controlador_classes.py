from model.classe import Classe
from model.exceptions.exception_classe import *
from model.exceptions.excpetion_habilidades import *
from views.tela_classes import TelaClasses
from DAOs.classe_dao import ClasseDao
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controlador_sistema import ControladorSistema


class ControladorClasses:
    def __init__(self, controlador_sistema: "ControladorSistema"):
        self.__controlador_sistema = controlador_sistema
        self.__tela_classes = TelaClasses()
        self.__classe_DAO = ClasseDao()

    def pega_classe_por_nome(self, nome: str):
        for classe in self.__classe_DAO.get_all():
            if classe.nome== nome:
                return classe
        return None
    
    def incluir_classe(self):
        try:
            dados_classe = self.__tela_classes.pegar_dados_classes()
            if dados_classe == 0:
                return False
            c = self.pega_classe_por_nome(dados_classe['nome'])
            if c:
                raise ClasseJahExisteException(dados_classe['nome'])
            else:
                classe = Classe(
                    dados_classe['nome'],
                    dados_classe['dado'],
                    dados_classe['nomes_sub']
                )
                self.__classe_DAO.add(classe)
                self.__tela_classes.mensagem('Classe criada com sucesso!')
                return True
        except ClasseJahExisteException as e:
            self.__tela_classes.mensagem(e)
        except KeyError as e:
            self.__tela_classes.mensagem(f'"[ERRO] Dado ausente: {str(e)}"')
        except Exception as e:
            self.__tela_classes.mensagem(f'[ERRO INESPERADO] Erro ao incluir classe: {str(e)}')

    
    def listar_classes(self):
        try:
            dados = []
            for cod, classe in self.__classe_DAO.cache.items():
                linha = [
                    cod,
                    classe.nome,
                    classe.dado_vida,
                    ', '.join(hab.nome for hab in classe.habilidades)
                ]
                dados.append(linha)

            HEADER = ["Cod", "Nome", "Dado Vida", "Habilidades"]
            self.__tela_classes.exibir_tabela(cabecalho=HEADER, dados=dados, nome_objeto='Classe')

        except Exception as e:
            self.__tela_classes.mensagem(f'[ERRO INESPERADO] Erro ao listar classes: {str(e)}')

    def listar_classes_e_sub_classe(self):
            dados = []
            for cod, classe in self.__classe_DAO.cache.items():
                linha = [
                    cod,
                    classe.nome,
                    classe.subclasses[0].nome, 
                    classe.subclasses[1].nome,
                    classe.subclasses[2].nome,
                    [hab.nome for hab in classe.subclasses[0].hab_especificas],
                    [hab.nome for hab in classe.subclasses[1].hab_especificas],
                    [hab.nome for hab in classe.subclasses[2].hab_especificas]
                ]
                dados.append(linha)

            HEADER = ["cod", "Nome", "1ª Subclasse", "2ª Subclassse", "3ª Subclasse", 'hab 1ª', 'hab 2ª', 'hab 3ª']
            self.__tela_classes.exibir_tabela(cabecalho=HEADER, dados=dados, nome_objeto='Subclasse')
                

    def excluir_classe(self):
        try:
            self.listar_classes()
            cod_validos = list(self.__classe_DAO.get_keys()) + [0]
            identificador = self.__tela_classes.selecionar_obj_por_cod('classe', cod_validos)
            if identificador == 0:
                return False
            else:
                self.__classe_DAO.remove(identificador)
                self.__tela_classes.mensagem('Classe removida!')
                return True
        except KeyError as e:
            self.__tela_classes.mensagem(f'[ERRO DE CHAVE] Erro ao excluir espécie, código não encontrado: {str(e)}')
        except Exception as e:
            self.__tela_classes.mensagem(f'[ERRO INESPERADO] Erro ao excluir classe: {e}') 

    def alterar_dados_base_classe(self):
        try:
            self.listar_classes()
            codigos_validos = list(self.__classe_DAO.get_keys()) + [0]
            identificador = self.__tela_classes.selecionar_obj_por_cod('classe', codigos_validos)
            if identificador == 0:
                return False
            else:
                classe = self.__classe_DAO.cache[identificador]
                dados_novos = self.__tela_classes.pegar_dados_classes()
                e = self.pega_classe_por_nome(dados_novos['nome'])
                if e is None:
                    classe.nome = dados_novos['nome']
                    classe.dado_vida = dados_novos['dado']
                    self.__classe_DAO.update(identificador, classe)
                    self.__tela_classes.mensagem(f'Classe de código {identificador} alterada com sucesso!')
                else:
                    raise ClasseJahExisteException(dados_novos['nome'])
        except ClasseJahExisteException as e:
            self.__tela_classes.mensagem(e)
        except KeyError as e:
            self.__tela_classes.mensagem(f'[ERRO DE CHAVE] Dado ausente: {str(e)}')
        except Exception as e:
            self.__tela_classes.mensagem(f'[ERRO INESPERADO] Erro ao modificar dados base de classe: {str(e)}') 

    def adiciona_hab_classe(self):
        try:
            self.listar_classes()
            codigos_validos_class = list(self.__classe_DAO.get_keys()) + [0]
            identificador_class = self.__tela_classes.selecionar_obj_por_cod('classes', codigos_validos_class)
            if identificador_class == 0:
                return False
            else:
                habilidades = self.__controlador_sistema.controlador_habilidades.habilidade_DAO.cache
                self.__controlador_sistema.controlador_habilidades.listar_habilidades(origem='classe')
                codigos_validos_hab = list(self.__controlador_sistema.controlador_habilidades.habilidade_DAO.get_keys()) + [0]
                identificador_hab = self.__tela_classes.selecionar_obj_por_cod('habilidade', codigos_validos_hab)
                if identificador_hab == 0:
                    return False
                elif habilidades[identificador_hab].origem == 'classe':
                    classe = self.__classe_DAO.cache[identificador_class]
                    if habilidades[identificador_hab].nome in [hab.nome for hab in classe.habilidades]:
                        raise HabilidadeJahExiste(habilidades[identificador_hab].nome)
                    classe.add_hab(habilidades[identificador_hab])
                    self.__classe_DAO.update(identificador_hab, classe)
                    self.__tela_classes.mensagem('Habilidade adicionada!')
                    return True
                else:
                    raise OrigemInvalidaException()
        except HabilidadeJahExiste as e:
            self.__tela_classes.mensagem(e)
        except OrigemInvalidaException as e:
            self.__tela_classes.mensagem(e)
        except KeyError as e:
            self.__tela_classes.mensagem(f'[ERRO DE CHAVE] Algum elemento não foi encontrado: {str(e)}')
        except Exception as e:
            self.__tela_classes.mensagem(f'[ERRO INESPERADO] Erro ao adicionar habilidade em classe: {str(e)}')

    def adiciona_hab_subclasse(self):
        try:
            self.listar_classes_e_sub_classe()
            codigos_validos_class = list(self.__classe_DAO.get_keys()) + [0]
            identificador_class= self.__tela_classes.selecionar_obj_por_cod('Classe', codigos_validos_class)
            if identificador_class == 0:
                return False
            else:
                classe = self.__classe_DAO.cache[identificador_class]
                habilidades = self.__controlador_sistema.controlador_habilidades.habilidade_DAO.cache
                identificador_sub = self.__tela_classes.ler_subclasse()
                if identificador_sub == 0:
                    return False
                else:
                    subclasse = classe.subclasses[identificador_sub - 1]    
                    self.__controlador_sistema.controlador_habilidades.listar_habilidades(origem='subclasse')
                    codigos_validos_sub = list(self.__controlador_sistema.controlador_habilidades.habilidade_DAO.get_keys()) + [0]
                    identificador_hab = self.__tela_classes.selecionar_obj_por_cod('subclasse', codigos_validos_sub)
                if identificador_hab == 0:
                    return False
                elif habilidades[identificador_hab].origem == 'subclasse':
                    if habilidades[identificador_hab].nome in [hab.nome for hab in subclasse.hab_especificas]:
                        raise HabilidadeJahExiste(habilidades[identificador_hab].nome)
                    subclasse.add_hab(habilidades[identificador_hab])
                    self.__classe_DAO.update(identificador_class, classe)
                    self.__tela_classes.mensagem('Habilidade adicionada!')
                    return True
                else:
                    raise OrigemInvalidaException()
        except HabilidadeJahExiste as e:
            self.__tela_classes.mensagem(e)
        except OrigemInvalidaException as e:
            self.__tela_classes.mensagem(e)
        except KeyError as e:
            self.__tela_classes.mensagem(f'[ERRO DE CHAVE] Algum elemento não foi encontrado: {e}')
        except Exception as e:
            self.__tela_classes.mensagem(f'[ERRO INESPERADO] Erro ao adicionar habilidade em subclasse: {e}')

    def remover_hab_classe(self):
        try:
            self.listar_classes()
            codigos_validos = list(self.__classe_DAO.get_keys()) + [0]
            identificador_class = self.__tela_classes.selecionar_obj_por_cod('classe', codigos_validos)
            if identificador_class == 0:
                return False
            else:
                habilidades = self.__controlador_sistema.controlador_habilidades.habilidade_DAO.cache
                classe = self.__classe_DAO.cache[identificador_class]
                self.__controlador_sistema.controlador_habilidades.listar_habilidades('classe')
                codigos_validos_hab = list(habilidades.keys()) + [0]
                identificador_hab = self.__tela_classes.selecionar_obj_por_cod('habilidades', codigos_validos_hab)
                if identificador_hab == 0:
                    return False
                elif habilidades[identificador_hab] not in classe.habilidades:
                    raise KeyError("[ERRO DE CHAVE] A habilidade selecionada é inválida.")
                else:
                    classe.rm_hab(habilidades[identificador_hab])
                    self.__classe_DAO.update(identificador_hab, classe)
                    self.__tela_classes.mensagem('Habilidade removida com sucesso!')
                    return True

        except KeyError as e: 
            self.__tela_classes.mensagem(f'ERRO DE CHAVE] Elemento não excluido, código não encontado: {e}')
        except Exception as e:
            self.__tela_classes.mensagem(f'[ERRO INESPERADO] Erro ao excluir habilidade em classe: {e}')

    def remover_hab_subclasse(self):
        try:
            self.listar_classes()
            codigos_validos_class = list(self.__classe_DAO.get_keys()) + [0]
            identificador_class = self.__tela_classes.selecionar_obj_por_cod('classe', codigos_validos_class)
            if identificador_class == 0:
                return False
            else:
                classe = self.__classe_DAO.cache[identificador_class]
                infos = {'nomes_sub': [sub.nome for sub in classe.subclasses],
                         'habilidades_sub': [[hab.nome for hab in sub.hab_especificas] for sub in classe.subclasses]}
                self.__tela_classes.mostra_classe_e_subclasse(infos, classe=False)
                identificador_sub = self.__tela_classes.le_int_ou_float(
                    'Digite qual subclasse (1, 2 ou 3 - de cima para baixo): ',
                    conjunto_alvo=[1, 2, 3]
                )
                if identificador_sub == 0:
                    return False
                else:
                    subclasse = classe.subclasses[identificador_sub-1]
    
                    self.__controlador_sistema.controlador_habilidades.listar_habilidades(origem='subclasse')
                    codigos_validos_hab = list(self.__controlador_sistema.controlador_habilidades.habilidade_DAO.get_keys()) + [0]
                    identificador_hab = self.__tela_classes.selecionar_obj_por_cod('habilidade', codigos_validos_hab)
                    if identificador_hab == 0:
                        return False
                    else:
                        habilidade = self.__controlador_sistema.controlador_habilidades.habilidade_DAO.cache[identificador_hab]
                        subclasse.rm_hab(habilidade[identificador_hab])
                        self.__classe_DAO.update(identificador_class, classe)
                        self.__tela_classes.mensagem('Habilidade removida com sucesso!')
                        return True

        except KeyError as e:
            self.__tela_classes.mensagem(f'[ERRO DE CHAVE] Elemento não excluido, código não encontrado: {e}')
        except Exception as e:
            self.__tela_classes.mensagem(f'[ERRO INESPERADO] Erro ao adicionar habilidade em subclasse: {e}')
      
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.incluir_classe,
            2: self.excluir_classe,
            3: self.listar_classes,
            4: self.alterar_dados_base_classe,
            5: self.adiciona_hab_classe,
            6: self.remover_hab_classe,
            7: self.adiciona_hab_subclasse,
            8: self.remover_hab_subclasse,
            9: self.listar_classes_e_sub_classe,
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
    def classe_DAO(self):
        return self.__classe_DAO
