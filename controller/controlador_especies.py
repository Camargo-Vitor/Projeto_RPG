from views.tela_especies import TelaEspecies
from model.especie import Especie
from model.subespecie import Subespecie
from model.exceptions.exception_especies import *
from model.exceptions.excpetion_habilidades import *
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller.controlador_sistema import ControladorSistema


class ControladorEspecies:
    def __init__(self, controlador_sistema: "ControladorSistema"):
        self.__controlador_sistema = controlador_sistema
        self.__dict_especie: dict[int, Especie] = {
            1000: Especie('Ser humano', 9, 170)
        }
        self.__dict_subespecie: dict[int, Subespecie] = {
            1000: Subespecie('Ser humano', 'De Xaragua', 9, 170, self.__dict_especie[1000].habilidades)
        }
        self.__tela_especies = TelaEspecies()
        self.__cod_esp = 1
        self.__cod_sub_esp = 1

    def pega_especie_por_nome(self, nome: str):
        try:
            for especie in self.__dict_especie.values():
                if especie.nome == nome:
                    return especie
            return None
        except Exception as e:
            self.__tela_especies.mensagem(f'[ERRO INESPERADO] Erro ao selecionar especie: {str(e)}')

    def pega_subespecie_por_sub_nome(self, nome_sub: str):
        try:
            for subespecie in self.__dict_subespecie.values():
                if subespecie.nome_sub == nome_sub:
                    return subespecie
            return None
        except Exception as e:
            self.__tela_especies.mensagem(f'[ERRO INESPERADO] Erro ao selecionar subespecie: {str(e)}')

    def incluir_especie(self):
        try:
            dados_especie = self.__tela_especies.pegar_dados_especie()
            e = self.pega_especie_por_nome(dados_especie['nome'])
            if e:
                raise EspecieJahExisteException(dados_especie['nome'])
            else:
                especie = Especie(
                    dados_especie['nome'],
                    dados_especie['deslocamento'],
                    dados_especie['altura'],
                        )
                self.__dict_especie[self.__cod_esp] = especie
                self.__cod_esp +=1
                self.__tela_especies.mensagem('Espécie criada com sucesso!')
                return True
        except EspecieJahExisteException as e:
            self.tela_especies.mensagem(e)
        except KeyError as e:
            self.__tela_especies.mensagem(f"[ERRO] Dado ausente: {str(e)}")
        except Exception as e:
            self.__tela_especies.mensagem(f'[ERRO INESPERADO] Erro ao incluir espécie: {str(e)}')

    def incluir_subespecie(self):
            try:
                self.listar_especies()
                cod_validos = list(self.__dict_especie.keys()) + [0]
                identificador = self.__tela_especies.selecionar_obj_por_cod('especie', cod_validos)
                if identificador == 0:
                    return False
                else:
                    especie = self.__dict_especie[identificador]
                    dados_subespecie = self.__tela_especies.pegar_dados_subespecie(especie.nome)
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
                        self.__dict_subespecie[self.__cod_sub_esp] = subespecie
                        self.__cod_sub_esp += 1
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
            for key, especie in self.__dict_especie.items():
                self.__tela_especies.mostra_especie(
                    {
                        'cod': key,
                        'nome': especie.nome,
                        'deslocamento': especie.deslocamento,
                        'altura': especie.altura,
                        'habilidades': [hab.nome for hab in especie.habilidades]             
                    }
                )

        except Exception as e:
            self.__tela_especies.mensagem(f'[ERRO INESPERADO] Erro ao listar as especies: {str(e)}')

    def listar_subespecies(self):
        try:
            for key, subespecie in self.__dict_subespecie.items():
                self.__tela_especies.mostra_subespecie(
                    {
                        'cod': key,
                        'nome': subespecie.nome,
                        'deslocamento': subespecie.deslocamento,
                        'altura': subespecie.altura,
                        'habilidades' : [hab.nome for hab in subespecie.habilidades],
                        'habilidades_esp' : [hab.nome for hab in subespecie.hab_especificas]
                    }
                )

        except Exception as e:
            self.__tela_especies.mensagem(f'[ERRO INESPERADO] Erro ao listar as subespécies: {str(e)}')

    def excluir_especie(self):
        try:
            self.listar_especies()
            cod_validos = list(self.__dict_especie.keys()) + [0]
            identificador = self.__tela_especies.selecionar_obj_por_cod('especie', cod_validos)
            if identificador == 0:
                return False
            else:
                for key, subespecie in self.__dict_subespecie.items():
                    if super(Subespecie, subespecie).nome == self.__dict_especie[identificador].nome:
                        del self.__dict_subespecie[key]
                del self.__dict_especie[identificador]
                self.__tela_especies.mensagem('Especie removida!')
                return True
            
        except KeyError as e:
            self.__tela_especies.mensagem(f'[ERRO DE CHAVE] Erro ao excluir espécie, código não encontrado: {str(e)}')
        except Exception as e:
            self.__tela_especies.mensagem(f'[ERRO INESPERADO] Erro ao excluir espécie: {str(e)}')

    def excluir_subespecie(self):
        try:
            self.listar_subespecies()
            cod_validos = list(self.__dict_subespecie.keys()) + [0]
            identificador = self.__tela_especies.selecionar_obj_por_cod('subespécie', cod_validos)
            if identificador == 0:
                return False
            else:
                del self.__dict_subespecie[identificador]
                self.__tela_especies.mensagem('Subespecie removida!')
                return True
        except KeyError as e:
            self.tela_especies.mensagem(f'[ERRO DE CHAVE] Erro ao excluir subespecie, código não encontrado: {str(e)}')
        except Exception as e:
            self.__tela_especies.mensagem(f'[ERRO INESPERADO] Erro ao excluir subespécie: {str(e)}')
        
    def alterar_especie_por_cod(self):
        try:
            self.listar_especies()
            cod_validos = list(self.__dict_especie.keys()) + [0]
            identificador = self.__tela_especies.selecionar_obj_por_cod('especie', cod_validos)
            if identificador == 0:
                return False
            else:
                    especie = self.__dict_especie[identificador]
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
            self.__tela_especies.mensagem(f'[ERRO DE CHAVE] Dado ausente: {str(e)}')
        except Exception as e:
            self.__tela_especies.mensagem(f'[ERRO INESPERADO] Erro ao alterar espécie por código: {str(e)}')

    def alterar_subespecie_por_cod(self):
        try:
            self.listar_subespecies()
            cod_validos = list(self.__dict_subespecie.keys()) + [0]
            identificador = self.__tela_especies.selecionar_obj_por_cod('subespecie', cod_validos)
            if identificador == 0:
                return False
            else:
                subespecie = self.__dict_subespecie[identificador]
                dados_novos = self.__tela_especies.pegar_dados_subespecie(super(Subespecie, subespecie).nome)
                e = self.pega_subespecie_por_sub_nome(dados_novos['nome_sub'])
                if e is None:
                    self.__dict_subespecie[identificador].nome_sub = dados_novos['nome']
                    self.__tela_especies.mensagem(f'Subespécie de código {identificador} alterada com sucesso!')
                    return True
                else:
                    raise EspecieJahExisteException(dados_novos['nome'])
        except EspecieJahExisteException as e:
            self.__tela_classes.mensagem(e)
        except KeyError as e:
            self.__tela_especies.mensagem(f'[ERRO DE CHAVE] Algum elemento não foi encontrado: {e}')
        except Exception as e:
            self.__tela_especies.mensagem(f'[ERRO INESPERADO] Erro ao alterar subespécie por código: {e}')
       
    def add_habilidade_especie(self):
        try:
            self.listar_especies()
            cod_validos_esp = list(self.__dict_especie.keys()) + [0]
            identificador_esp = self.__tela_especies.selecionar_obj_por_cod('especie', cod_validos_esp)
            if identificador_esp == 0:
                return False
            else:
                habilidades = self.__controlador_sistema.controlador_habilidades.dict_habilidades
                self.__controlador_sistema.controlador_habilidades.listar_habilidades('especie')
                cod_validos_hab = list(habilidades.keys()) + [0]
                identificador_hab = self.__tela_especies.selecionar_obj_por_cod('habilidade', cod_validos_hab)
                if identificador_hab == 0:
                    return
                elif habilidades[identificador_hab].origem == 'especie':
                    especie = self.__dict_especie[identificador_esp]
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
            self.__tela_especies.mensagem(f'[ERRO DE CHAVE] Algum elemento não foi encontrado: {e}')
        except Exception as e:
            self.__tela_especies.mensagem(f'[ERRO INESPERADO] Erro ao adicionar habilidade em espécie: {e}')

    def add_habilidade_subespecie(self):
        try:
            self.listar_subespecies()
            cod_validos_sub = list(self.__dict_subespecie.keys()) + [0]
            identificador_sub = self.__tela_especies.selecionar_obj_por_cod('subespecie', cod_validos_sub)
            if identificador_sub == 0:
                return False
            else:
                habilidades = self.__controlador_sistema.controlador_habilidades.dict_habilidades
                cod_validos_hab = list(habilidades.keys()) + [0]
                self.__controlador_sistema.controlador_habilidades.listar_habilidades('subespecie')
                identificador_hab = self.__tela_especies.selecionar_obj_por_cod('habilidade', cod_validos_hab)
                if identificador_hab == 0:
                    return False
                elif habilidades[identificador_hab].origem == 'subespecie':
                    subespecie = self.__dict_subespecie[identificador_sub]
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
            self.__tela_especies.mensagem(f'[ERRO DE CHAVE] Algum elemento não foi encontrado: {e}')
        except Exception as e:
            self.__tela_especies.mensagem(f'[ERRO INESPERADO] Erro ao adicionar habilidade em espécie: {e}')
        
    def remove_habilidade_especie(self):
        try:
            self.listar_especies()
            cod_valido_esp = list(self.__dict_especie.keys()) + [0]
            identificador_esp = self.__tela_especies.selecionar_obj_por_cod('especie', cod_valido_esp)
            especie = self.__dict_especie[identificador_esp]
            if identificador_esp == 0:
                return False
            else:
                habilidade = self.__controlador_sistema.controlador_habilidades.dict_habilidades
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
            self.__tela_especies.mensagem(f'[ERRO INESPERADO] Erro ao adicionar habilidade em espécie: {e}')
    
    def remove_habilidade_subespecie(self):
        try:
            self.listar_subespecies()
            cod_validos_sub = list(self.__dict_subespecie.keys()) + [0]
            identificador_sub = self.__tela_especies.selecionar_obj_por_cod('subespecie', cod_validos_sub)
            if identificador_sub == 0:
                return False
            else:
                habilidade = self.__controlador_sistema.controlador_habilidades.dict_habilidades
                subespecie = self.__dict_subespecie[identificador_sub]
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
    
    def retornar_tela_especie(self):
        self.abre_tela()
        
    def abre_tela_especie(self):
        opcoes = {
            1: self.incluir_especie,
            2: self.excluir_especie,
            3: self.listar_especies,
            4: self.alterar_especie_por_cod,
            5: self.add_habilidade_especie,
            6: self.remove_habilidade_especie,
            0: self.abre_tela
        }
        while True:
            opc = self.__tela_especies.mostra_tela_especie()
            metodo = opcoes[opc]
            metodo()

    def abre_tela_subespecie(self):
        opcoes= {
            1: self.incluir_subespecie,
            2: self.excluir_subespecie,
            3: self.listar_subespecies,
            4: self.alterar_subespecie_por_cod,
            5: self.add_habilidade_subespecie,
            6: self.remove_habilidade_subespecie,
            0: self.abre_tela
        }
        while True:
            opc = self.__tela_especies.mostra_tela_subespecie()
            metodo = opcoes[opc]
            metodo()

    def abre_tela(self):
        opcoes = {
            1: self.abre_tela_especie,
            2: self.abre_tela_subespecie,
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
    def tela_especies(self):
        return self.__tela_especies
    
    @property
    def dict_especie(self):
        return self.__dict_especie
    
    @property
    def dict_subespecie(self):
        return self.__dict_subespecie
