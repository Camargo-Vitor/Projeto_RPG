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

            #atributos
            atributos = self.__tela_fichas.pegar_dados_atributos()
            
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
            self.__cod += 1
            return True

        except Exception as e:
            self.__tela_fichas.mensagem(f'[ERRO INESPERADO] Erro ao criar Ficha: {e} ({type(e).__name__})')

    def listar_fichas(self, selecao=True):
        try:
            cod_validos = list(self.__dict_fichas.keys()) + [0]
            self.__tela_fichas.mensagem(f"{'Cod':^4} | {'Nome':^16}")
            for key, ficha in self.__dict_fichas.items():
                self.__tela_fichas.mostra_ficha_basica(
                    {
                        'cod': key,
                        'nome': ficha.nome
                    }
                )
            if selecao:
                identificador = self.__tela_fichas.selecionar_obj_por_cod(f'fichas', cod_validos)
                if identificador == 0:
                    return False
                else:
                    '''
                    TERMINAR A INCLUSAO DE HABILIDADES COM BASE NO NIVEL DA FICHA
                    '''
                    ficha = self.__dict_fichas[identificador]
                    habilidades = []
                    habilidades += ficha.classe.habilidades
                    habiliades += ficha
                    habilidades += ficha.especie.habilidades
                    self.__tela_fichas.mostra_ficha_inteira(
                        {
                            'nome': ficha.nome,
                            'nivel': ficha.nivel,
                            'vida': ficha.vida,
                            'vida_atual': ficha.vida_atual,
                            'deslocamento': ficha.deslocamento,
                            'fisico': ficha.fisico,
                            'altura': ficha.altura,
                            'historia': ficha.historia,
                            'classe': ficha.classe.nome,
                            'especie': ficha.especie.nome,
                            'pericias': ficha.pericias_treinadas,
                            'forca': f'{ficha.atributos["forca"]} ({(ficha.atributos["forca"] - 10) // 2})',
                            'destreza': f'{ficha.atributos["destreza"]} ({(ficha.atributos["destreza"] - 10) // 2})',
                            'constituicao': f'{ficha.atributos["constituicao"]} ({(ficha.atributos["constituicao"] - 10) // 2})',
                            'inteligencia': f'{ficha.atributos["inteligencia"]} ({(ficha.atributos["inteligencia"] - 10) // 2})',
                            'sabedoria': f'{ficha.atributos["sabedoria"]} ({(ficha.atributos["sabedoria"] - 10) // 2})',
                            'carisma': f'{ficha.atributos["carisma"]} ({(ficha.atributos["carisma"] - 10) // 2})',
                            'inventario': [item.nome for item in ficha.inventario],
                            'magias': [magia.nome for magia in ficha.lista_magias],
                            'habilidades': habilidades
                        }
                    )
        except Exception as e:
            self.__tela_fichas.mensagem(f"[ERRO INESPERADO] Erro ao listar os itens em ficha: {str(e)}")

    def adicionar_item_ficha(self):
        try:
            self.listar_fichas(selecao=False)
            cod_validos_ficha = list(self.__dict_fichas.keys()) + [0]
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
            self.__tela_fichas.mensagem(f'[ERRO DE CHAVE] Algum elemento não foi encontrado: {e}')
        except Exception as e:
            self.__tela_fichas.mensagem(f'[ERRO INESPERADO] Erro ao alterar Item: {e}')
            
    def adicionar_magia_ficha(self):
        try:
            self.listar_fichas(selecao=False)
            cod_validos_ficha = list(self.__dict_fichas.keys()) + [0]
            identificador_ficha = self.__tela_fichas.selecionar_obj_por_cod('fichas', cod_validos_ficha)
            if identificador_ficha == 0:
                return False
            else:
                magia = self.__controlador_sistema.controlador_magias.dict_magias
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
            self.__tela_fichas.mensagem(f'[ERRO DE CHAVE] Algum elemento não foi encontrado: {e}')
        except Exception as e:
            self.__tela_fichas.mensagem(f'[ERRO INESPERADO] Erro ao alterar Magia: {e}')

    def remover_item_ficha(self):
        try:
            self.listar_fichas(selecao=False)
            cod_validos_ficha = list(self.__dict_fichas.keys()) + [0]
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
            self.__tela_fichas.mensagem(f'[ERRO DE CHAVE] Algum elemento não foi encontrado: {e}')
        except Exception as e:
            self.__tela_fichas.mensagem(f'[ERRO INESPERADO] Erro ao alterar Item: {e}')
            
    def remover_magia_ficha(self):
        try:
            self.listar_fichas(selecao=False)
            cod_validos_ficha = list(self.__dict_fichas.keys()) + [0]
            identificador_ficha = self.__tela_fichas.selecionar_obj_por_cod('fichas', cod_validos_ficha)
            if identificador_ficha == 0:
                return False
            else:
                magias = self.__controlador_sistema.controlador_magias.dict_magias
                self.__controlador_sistema.controlador_magias.listar_magias()
                codigos_validos_magia = list(magias.keys()) + [0]
                identificador_magia = self.__tela_fichas.selecionar_obj_por_cod('magia', codigos_validos_magia)
                if identificador_magia == 0:
                    return False
                else:
                    ficha = self.dict_fichas[identificador_ficha]
                    ficha.rm_magia(magias[identificador_magia])
                    self.__tela_fichas.mensagem('Magia removida!')
                    return True
        except KeyError as e:
            self.__tela_fichas.mensagem(f'[ERRO DE CHAVE] Algum elemento não foi encontrado: {e}')
        except Exception as e:
            self.__tela_fichas.mensagem(f'[ERRO INESPERADO] Erro ao alterar Magia: {e}')


    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.incluir_ficha,
            2: self.listar_fichas,
            3: self.adicionar_item_ficha,
            4: self.remover_item_ficha,
            5: self.adicionar_magia_ficha,
            6: self.remover_magia_ficha,
            0: self.retornar
        }
        while True:
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
