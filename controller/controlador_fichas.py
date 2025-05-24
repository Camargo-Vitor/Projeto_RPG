from model.ficha import Ficha
from views.tela_fichas import TelaFichas
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller.controlador_sistema import ControladorSistema


class ControladorFichas:
    def __init__(self, controlador_sistema: "ControladorSistema"):
        self.__controlador_sistema = controlador_sistema
        self.__tela_fichas = TelaFichas()
        self.__cod = 1
        self.__dict_fichas: dict[int, Ficha] = dict()

    def incluir_ficha(self):
        try:

            #atributos
            atributos = self.__tela_fichas.pegar_dados_atributos()
            #dados basicos
            dados__basicos_ficha = self.__tela_fichas.pegar_dados_basicos_ficha()

            #classe
            self.__controlador_sistema.controlador_classes.listar_classes_e_subclasses()
            codigos_validos = list(self.__controlador_sistema.controlador_classes.dict_classes.keys()) + [0]
            codigo_classe = self.__tela_fichas.le_int_ou_float(
                'Digite o código da classe (0 para cancelar): ',
                conjunto_alvo = codigos_validos
                )
            if codigo_classe == 0:
                return False
            else:
                classe = self.__controlador_sistema.controlador_classes.dict_classes[codigo_classe]

            #subespecie
            self.__controlador_sistema.controlador_especies.listar_subespecies()
            codigos_validos = list(self.__controlador_sistema.controlador_especies.dict_subespecie.keys()) + [0]
            codigo_subespecie = self.__tela_fichas.le_int_ou_float(
                'Digite o código da subespecie (0 para cancelar): ',
                conjunto_alvo = codigos_validos
                )
            if codigo_subespecie == 0:
                return False
            else:
                subespecie = self.__controlador_sistema.controlador_especies.dict_subespecie[codigo_subespecie]
            
            #pericias
            pericias_treinadas = self.__tela_fichas.pegar_dados_pericias()

            nova_ficha = Ficha(
                dados__basicos_ficha['nome_personagem'],
                dados__basicos_ficha['descricao_fisica'],
                dados__basicos_ficha['historia'],
                classe,
                subespecie,
                pericias_treinadas,
                atributos)
            
            self.__dict_fichas[self.__cod] = nova_ficha
            print(nova_ficha)
            return True

        except Exception as e:
            self.__tela_fichas.mensagem(f'[ERRO INESPERADO] Erro ao criar Ficha: {e} ({type(e).__name__})')

    def listar_ficha(self):
        try:
            cod_validos = list(self.dict_fichas.keys()) + [0]
            self.__tela_fichas.mensagem(f"{'Cod':^4} | {'Nome':^16}")
            for key, ficha_cod in self.__dict_fichas.items():
                self.__tela_fichas.mostra_ficha(
                    {
                        'cod': key,
                        'nome': ficha_cod.nome
                    }
                )
                identificador = self.tela_fichas.selecionar_obj_por_cod(f'fichas', cod_validos)
                if identificador == 0:
                    return False
                else:
                    ficha = self.dict_fichas[identificador]
                    self.__tela_fichas.mostra_ficha_inteira(
                        {
                            ficha.nivel,
                            ficha.vida,
                            ficha.vida_atual,
                            ficha.deslocamento,
                            ficha.fisico,
                            ficha.altura,
                            ficha.historia,
                            ficha.classe,
                            ficha.especie,
                            ficha.inventario,
                            ficha.lista_magias
                        }
                    )
        except Exception as e:
            self.tela_fichas.mensagem(f"[ERRO INESPERADO] Erro ao listar os itens: {str(e)}")


    def adicionar_item_ficha(self):
        try:
            self.listar_ficha()
            cod_validos_ficha = list(self.__dict_fichas.keys() + [0])
            identificador_ficha = self.__tela_fichas.selecionar_obj_por_cod('fichas', cod_validos_ficha)
            if identificador_ficha == 0:
                return False
            else:
                item = self.__controlador_sistema.controlador_itens.dict_item
                self.__controlador_sistema.controlador_itens.listar_itens()
                codigos_validos_item = list(item.keys()) + [0]
                identificador_item = self.__tela_fichas.selecionar_obj_por_cod('item', codigos_validos_item)
                if identificador_item == 0:
                    return False
                else:
                    ficha = self.dict_fichas[identificador_ficha]
                    ficha.add_item_inventario(item[identificador_item])
                    self.__tela_fichas.mensagem('Item adicionada ao inventário!')
                    return True
        except KeyError as e:
            self.__tela_fichas.mensagem(f'ERRO DE CHAVE] Algum elemento não foi encontrado: {e}')
        except Exception as e:
            self.__tela_fichas.mensagem(f'[ERRO INESPERADO] Erro ao alterar Item: {e}')
            
    def adicionar_magia_ficha(self):
        try:
            self.listar_ficha()
            cod_validos_ficha = list(self.__dict_fichas.keys() + [0])
            identificador_ficha = self.__tela_fichas.selecionar_obj_por_cod('fichas', cod_validos_ficha)
            if identificador_ficha == 0:
                return False
            else:
                magia = self.__controlador_sistema.controlador_magias.__dict_magias
                self.__controlador_sistema.controlador_magias.listar_magias()
                codigos_validos_magia = list(magia.keys()) + [0]
                identificador_magia = self.__tela_fichas.selecionar_obj_por_cod('magia', codigos_validos_magia)
                if identificador_magia == 0:
                    return False
                else:
                    ficha = self.dict_fichas[identificador_ficha]
                    ficha.add_magia(magia[identificador_magia])
                    self.__tela_fichas.mensagem('Magia adicionada ao inventário!')
                    return True
        except KeyError as e:
            self.__tela_fichas.mensagem(f'ERRO DE CHAVE] Algum elemento não foi encontrado: {e}')
        except Exception as e:
            self.__tela_fichas.mensagem(f'[ERRO INESPERADO] Erro ao alterar Magia: {e}')

    def remover_item_ficha(self):
        try:
            self.listar_ficha()
            cod_validos_ficha = list(self.__dict_fichas.keys() + [0])
            identificador_ficha = self.__tela_fichas.selecionar_obj_por_cod('fichas', cod_validos_ficha)
            if identificador_ficha == 0:
                return False
            else:
                item = self.__controlador_sistema.controlador_itens.dict_item
                self.__controlador_sistema.controlador_itens.listar_itens()
                codigos_validos_item = list(item.keys()) + [0]
                identificador_item = self.__tela_fichas.selecionar_obj_por_cod('item', codigos_validos_item)
                if identificador_item == 0:
                    return False
                else: 
                    ficha = self.dict_fichas[identificador_ficha]
                    ficha.rm_item_inventario(item[identificador_item])
                    self.__tela_fichas.mensagem('Item removido do inventário!')
                    return True
                
                
        except KeyError as e:
            self.__tela_fichas.mensagem(f'ERRO DE CHAVE] Algum elemento não foi encontrado: {e}')
        except Exception as e:
            self.__tela_fichas.mensagem(f'[ERRO INESPERADO] Erro ao alterar Item: {e}')
            
    def remover_magia_ficha(self):
        try:
            self.listar_ficha()
            cod_validos_ficha = list(self.__dict_fichas.keys() + [0])
            identificador_ficha = self.__tela_fichas.selecionar_obj_por_cod('fichas', cod_validos_ficha)
            if identificador_ficha == 0:
                return False
            else:
                magia = self.__controlador_sistema.controlador_magias.__dict_magias
                self.__controlador_sistema.controlador_magias.listar_magias()
                codigos_validos_magia = list(magia.keys()) + [0]
                identificador_magia = self.__tela_fichas.selecionar_obj_por_cod('magia', codigos_validos_magia)
                if identificador_magia == 0:
                    return False
                else:
                    ficha = self.dict_fichas[identificador_ficha]
                    ficha.rm_magia(magia[identificador_magia])
                    self.__tela_fichas.mensagem('Magia removida!')
                    return True
        except KeyError as e:
            self.__tela_fichas.mensagem(f'ERRO DE CHAVE] Algum elemento não foi encontrado: {e}')
        except Exception as e:
            self.__tela_fichas.mensagem(f'[ERRO INESPERADO] Erro ao alterar Magia: {e}')


    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.incluir_ficha,
            2: self.listar_ficha,
            3: self.adicionar_item_ficha,
            4: self.remover_item_ficha,
            5: self.adicionar_magia_ficha,
            6: self.remover_magia_ficha,
            0: self.retornar
        }
        opc = self.__tela_fichas.mostra_tela()
        metodo = opcoes[opc]
        metodo()

    @property
    def tela_fichas(self):
        return self.__tela_fichas

    @property
    def cod(self):
        return self.__cod

    @property
    def dict_fichas(self):
        return self.__dict_fichas
