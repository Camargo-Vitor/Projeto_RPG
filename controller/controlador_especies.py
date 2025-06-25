from views.tela_especies import TelaEspecies
from model.especie import Especie
from model.subespecie import Subespecie
from model.exceptions.exception_especies import *
from model.exceptions.excpetion_habilidades import *
from DAOs.especie_dao import EspecieDao
from DAOs.subespecie import SubepecieDao
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller.controlador_sistema import ControladorSistema


class ControladorEspecies:
    def __init__(self, controlador_sistema: "ControladorSistema"):
        self.__controlador_sistema = controlador_sistema
        self.__tela_especies = TelaEspecies()
        self.__especie_DAO = EspecieDao()
        self.__subespecie_DAO = SubepecieDao()

    def pega_especie_por_nome(self, nome: str):
        try:
            for especie in self.__especie_DAO.get_all():
                if especie.nome == nome:
                    return especie
            return None
        except Exception as e:
            self.__tela_especies.mensagem(f'[ERRO INESPERADO] Erro ao selecionar especie: {str(e)}')

    def pega_subespecie_por_sub_nome(self, nome_sub: str):
        try:
            for subespecie in self.__subespecie_DAO.get_all():
                if subespecie.nome_sub == nome_sub:
                    return subespecie
            return None
        except Exception as e:
            self.__tela_especies.mensagem(f'[ERRO INESPERADO] Erro ao selecionar subespecie: {str(e)}')

    def incluir_especie(self):
        try:
            dados_especie = self.__tela_especies.pegar_dados_especie()
            if dados_especie == 0:
                return False
            e = self.pega_especie_por_nome(dados_especie['nome'])
            if e:
                raise EspecieJahExisteException(dados_especie['nome'])
            else:
                especie = Especie(
                    dados_especie['nome'],
                    dados_especie['deslocamento'],
                    dados_especie['altura'],
                        )
                self.__especie_DAO.add(especie)
                self.__tela_especies.mensagem('Espécie criada com sucesso!')
                return True
        except EspecieJahExisteException as e:
            self.__tela_especies.mensagem(e)
        except KeyError as e:
            self.__tela_especies.mensagem(f"[ERRO] Dado ausente: {str(e)}")
        except Exception as e:
            self.__tela_especies.mensagem(f'[ERRO INESPERADO] Erro ao incluir espécie: {str(e)}')

    def incluir_subespecie(self):
            try:
                self.listar_especies()
                cod_validos = list(self.__subespecie_DAO.get_keys()) + [0]
                identificador = self.__tela_especies.selecionar_obj_por_cod('especie', cod_validos)
                if identificador == 0:
                    return False
                else:
                    especie = self.__especie_DAO.cache[identificador]
                    dados_subespecie = self.__tela_especies.pegar_dados_subespecie(especie.nome)
                    if dados_subespecie == 0:
                        return False
                    s = self.pega_subespecie_por_sub_nome(dados_subespecie['nome'])

                    if s:
                        raise EspecieJahExisteException(dados_subespecie['nome'])
                    else:
                        subespecie = Subespecie(
                            especie.nome, 
                            dados_subespecie['nome'],
                            especie.deslocamento,
                            especie.altura,
                            especie.habilidades
                        )
                        self.__subespecie_DAO.add(subespecie)
                        self.__tela_especies.mensagem('Subespecie criada com sucesso!')
                        return True

            except EspecieJahExisteException as e:
                self.__tela_especies.mensagem(e)
            except KeyError as e:
                self.__tela_especies.mensagem(f"[ERRO] Dado ausente: {str(e)}")
            except Exception as e:
                self.__tela_especies.mensagem(f'[ERRO INESPERADO] Erro ao incluir subespecie: {str(e)}')

    def listar_especies(self):
        try:
            dados = []

            for key, especie in self.__especie_DAO.cache.items():
                linha = [
                    key,
                    especie.nome,
                    especie.deslocamento,
                    especie.altura,
                    ', '.join(hab.nome for hab in especie.habilidades)
                ]
                dados.append(linha)
            HEADER = ['Código', 'Nome', 'Deslocamento', 'Altura', 'Habilidades']
            self.__tela_especies.exibir_tabela(cabecalho=HEADER, dados=dados, nome_objeto='Especie')
        except Exception as e:
            self.__tela_especies.mensagem(f'[ERRO INESPERADO] Erro ao listar as espécies: {str(e)}')

    def listar_subespecies(self):
        try:
            dados = []

            for key, subespecie in self.__subespecie_DAO.cache.items():
                habilidades = []
                for hab in subespecie.habilidades:
                    habilidades.append(hab.nome)

                habilidades_esp = []
                for hab in subespecie.hab_especificas:
                    habilidades_esp.append(hab.nome)

                linha = [
                    key,
                    subespecie.nome,
                    subespecie.deslocamento,
                    subespecie.altura,
                    ', '.join(habilidades),
                    ', '.join(habilidades_esp)
                ]
                dados.append(linha)

            HEADER = ['Código', 'Nome', 'Deslocamento', 'Altura', 'Habilidades', 'Habilidades Específicas']
            self.__tela_especies.exibir_tabela(cabecalho=HEADER, dados=dados)
        except Exception as e:
            self.__tela_especies.mensagem(f'[ERRO INESPERADO] Erro ao listar as subespécies: {str(e)}')

    def excluir_especie(self):
        try:
            self.listar_especies()
            cod_validos = list(self.__especie_DAO.get_keys()) + [0]
            identificador = self.__tela_especies.selecionar_obj_por_cod('especie', cod_validos)
            if identificador == 0:
                return False
            else:
                subespecies_relacionadas = []
                for key, subespecie in self.__subespecie_DAO.cache.items():
                    if super(Subespecie, subespecie).nome == self.__especie_DAO.cache[identificador].nome:
                        subespecies_relacionadas.append(key)
                for i in subespecies_relacionadas:
                    self.__subespecie_DAO.remove(i)
                    self.__subespecie_DAO.remove(identificador)
                self.__tela_especies.mensagem('Especie removida!')
                return True
            
        except KeyError as e:
            self.__tela_especies.mensagem(f'[ERRO DE CHAVE] Erro ao excluir espécie, código não encontrado: {str(e)}')
        except Exception as e:
            self.__tela_especies.mensagem(f'[ERRO INESPERADO] Erro ao excluir espécie: {str(e)}')

    def excluir_subespecie(self):
        try:
            self.listar_subespecies()
            cod_validos = list(self.__subespecie_DAO.get_keys()) + [0]
            identificador = self.__tela_especies.selecionar_obj_por_cod('subespécie', cod_validos)
            if identificador == 0:
                return False
            else:
                self.__subespecie_DAO.remove(identificador)
                self.__tela_especies.mensagem('Subespecie removida!')
                return True
        except KeyError as e:
            self.__tela_especies.mensagem(f'[ERRO DE CHAVE] Erro ao excluir subespecie, código não encontrado: {str(e)}')
        except Exception as e:
            self.__tela_especies.mensagem(f'[ERRO INESPERADO] Erro ao excluir subespécie: {str(e)}')
        
    def alterar_especie_por_cod(self):
        try:
            self.listar_especies()
            cod_validos = list(self.__especie_DAO.get_keys()) + [0]
            identificador = self.__tela_especies.selecionar_obj_por_cod('especie', cod_validos)
            if identificador == 0:
                return False
            else:
                    especie = self.__especie_DAO.cache[identificador]
                    dados_novos = self.__tela_especies.pegar_dados_especie()
                    e = self.pega_especie_por_nome(dados_novos['nome'])
                    if e is None:
                        especie.nome = dados_novos['nome']
                        especie.deslocamento = dados_novos['deslocamento']
                        especie.altura = dados_novos['altura']
                        self.__tela_especies.mensagem(f'Especie de código {identificador} alterada com sucesso!')
                        return True
                    else:
                        raise EspecieJahExisteException(dados_novos['nome'])
        except EspecieJahExisteException as e:
            self.__tela_especies.mensagem(e)
        except KeyError as e:
            self.__tela_especies.mensagem(f'[ERRO DE CHAVE] Erro ao buscar espécie, código não encontrado: {str(e)}')
        except Exception as e:
            self.__tela_especies.mensagem(f'[ERRO INESPERADO] Erro ao alterar espécie por código: {str(e)}')

    def alterar_subespecie_por_cod(self):
        try:
            self.listar_subespecies()
            cod_validos = list(self.__subespecie_DAO.get_keys()) + [0]
            identificador = self.__tela_especies.selecionar_obj_por_cod('subespecie', cod_validos)
            if identificador == 0:
                return False
            subespecie = self.__subespecie_DAO.cache[identificador]
            dados_novos = self.__tela_especies.pegar_dados_subespecie(super(Subespecie, subespecie).nome)
            e = self.pega_subespecie_por_sub_nome(dados_novos['nome'])
            if e is None:
                self.__subespecie_DAO.cache[identificador].nome_sub = dados_novos['nome']
                self.__tela_especies.mensagem(f'Subespécie de código {identificador} alterada com sucesso!')
                return True
            else:
                raise EspecieJahExisteException(dados_novos['nome'])
        except EspecieJahExisteException as e:
                self.__tela_especies.mensagem(e)
        except KeyError as e:
            self.__tela_especies.mensagem(f'[ERRO DE CHAVE] Erro ao buscar subespécie, código não encontrado: {str(e)}')
        except Exception as e:
            self.__tela_especies.mensagem(f'[ERRO INESPERADO] Erro ao alterar subespécie por código: {e}')
        
    def add_habilidade_especie(self):
        try:
            self.listar_especies()
            cod_validos_esp = list(self.__especie_DAO.get_keys()) + [0]
            identificador_esp = self.__tela_especies.selecionar_obj_por_cod('especie', cod_validos_esp)
            if identificador_esp == 0:
                return False
            else:
                habilidades = self.__controlador_sistema.controlador_habilidades.habilidade_DAO.cache
                self.__controlador_sistema.controlador_habilidades.listar_habilidades('especie')
                cod_validos_hab = list(habilidades.keys()) + [0]
                identificador_hab = self.__tela_especies.selecionar_obj_por_cod('habilidade', cod_validos_hab)
                if identificador_hab == 0:
                    return
                elif habilidades[identificador_hab].origem == 'especie':
                    especie = self.__especie_DAO.cache[identificador_esp]
                    if habilidades[identificador_hab].nome in [hab.nome for hab in especie.habilidades]:
                        raise HabilidadeJahExiste(habilidades[identificador_hab].nome)
                    especie.add_habilidade(habilidades[identificador_hab])
                    self.__tela_especies.mensagem('Hablidade adicionada!')
                    return True
                else:
                    raise OrigemInvalidaException()
        except HabilidadeJahExiste as e:
            self.__tela_especies.mensagem(e)
        except OrigemInvalidaException as e:
            self.__tela_especies.mensagem(e)
        except KeyError as e:
            self.__tela_especies.mensagem(f'[ERRO DE CHAVE] Erro ao buscar habilidade, código não encontrado: {str(e)}')
        except Exception as e:
            self.__tela_especies.mensagem(f'[ERRO INESPERADO] Erro ao adicionar habilidade em espécie: {e}')

    def add_habilidade_subespecie(self):
        try:
            self.listar_subespecies()
            cod_validos_sub = list(self.__especie_DAO.get_keys()) + [0]
            identificador_sub = self.__tela_especies.selecionar_obj_por_cod('subespecie', cod_validos_sub)
            if identificador_sub == 0:
                return False
            habilidades = self.__controlador_sistema.controlador_habilidades.__habilidade_DAO.cache
            cod_validos_hab = list(habilidades.keys()) + [0]
            self.__controlador_sistema.controlador_habilidades.listar_habilidades('subespecie')
            identificador_hab = self.__tela_especies.selecionar_obj_por_cod('habilidade', cod_validos_hab)
            if identificador_hab == 0:
                return False
            elif habilidades[identificador_hab].origem == 'subespecie':
                subespecie = self.__subespecie_DAO.cache[identificador_sub]
                if habilidades[identificador_hab].nome in [hab.nome for hab in subespecie.habilidades]:
                    raise HabilidadeJahExiste(habilidades[identificador_hab].nome)
                subespecie.add_hab_sub(habilidades[identificador_hab])
                self.__tela_especies.mensagem('Hablidade adicionada!')
                return True
            else:
                raise OrigemInvalidaException()

        except HabilidadeJahExiste as e:
            self.__tela_especies.mensagem(e)
        except OrigemInvalidaException as e:
            self.__tela_especies.mensagem(e)
        except KeyError as e:
            self.__tela_especies.mensagem(f'[ERRO DE CHAVE] Erro ao buscar habilidade, código não encontrado: {str(e)}')
        except Exception as e:
            self.__tela_especies.mensagem(f'[ERRO INESPERADO] Erro ao adicionar habilidade em espécie: {e}')
        
    def remove_habilidade_especie(self):
        try:
            self.listar_especies()
            cod_valido_esp = list(self.__especie_DAO.get_keys()) + [0]
            identificador_esp = self.__tela_especies.selecionar_obj_por_cod('especie', cod_valido_esp)
            especie = self.__especie_DAO.cache[identificador_esp]
            if identificador_esp == 0:
                return False
            else:
                habilidade = self.__controlador_sistema.controlador_habilidades.habilidade_DAO.cache
                cod_valido_hab = list(habilidade.keys()) + [0]
                self.__controlador_sistema.controlador_habilidades.listar_habilidades('especie')
                identificador_hab = self.__tela_especies.selecionar_obj_por_cod('habilidade', cod_valido_hab)
                if identificador_hab == 0:
                    return False
                else:
                    especie.rm_hab(habilidade[identificador_hab])
                    self.__tela_especies.mensagem('Habilidade Removida!')
                    return True

        except KeyError as e:
            self.__tela_especies.mensagem(f'[ERRO DE CHAVE] Elemento não excluido, código não encontado.: {e}')
        except Exception as e:
            self.__tela_especies.mensagem(f'[ERRO INESPERADO] Erro remover habilidade de espécie: {e}')
    
    def remove_habilidade_subespecie(self):
        try:
            self.listar_subespecies()
            cod_validos_sub = list(self.__subespecie_DAO.get_keys()) + [0]
            identificador_sub = self.__tela_especies.selecionar_obj_por_cod('subespecie', cod_validos_sub)
            if identificador_sub == 0:
                return False
            else:
                habilidade = self.__controlador_sistema.controlador_habilidades.habilidade_DAO.cache
                subespecie = self.__subespecie_DAO.cache[identificador_sub]
                cod_validos_hab = list(habilidade.keys())
                self.__controlador_sistema.controlador_habilidades.listar_habilidades('subespecie')
                identificador_hab = self.__tela_especies.selecionar_obj_por_cod('habilidade', cod_validos_hab)
                if identificador_hab == 0:
                    return False
                else:
                    subespecie.rm_hab_sub(habilidade[identificador_hab])
                    self.__tela_especies.mensagem('Habilidade Removida!')
                    return True

        except KeyError as e:
            self.__tela_especies.mensagem(f'[ERRO DE CHAVE] Elemento não excluido, código não encontrado: {e}')
        except Exception as e:
            self.__tela_especies.mensagem(f'[ERRO INESPERADO] Erro ao adicionar habilidade em espécie: {e}')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.incluir_especie,
            2: self.excluir_especie,
            3: self.listar_especies,
            4: self.alterar_especie_por_cod,
            5: self.add_habilidade_especie,
            6: self.remove_habilidade_especie,
            7: self.incluir_subespecie,
            8: self.excluir_subespecie,
            9: self.listar_subespecies,
            10: self.alterar_subespecie_por_cod,
            11: self.add_habilidade_subespecie,
            12: self.remove_habilidade_subespecie,
            0: self.retornar
        }
        while True:
            opc = self.__tela_especies.mostra_tela()
            metodo = opcoes[opc]
            metodo()

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @property
    def especie_DAO(self):
        return self.__especie_DAO
    
    @property
    def subespecie(self):
        return self.__subespecie_DAO
