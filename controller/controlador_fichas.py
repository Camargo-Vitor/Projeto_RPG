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

    def selecionar_habilidades_aivas_em_ficha(self, ficha: Ficha):
        habilidades = []
        for hab in ficha.especie.hab_especificas:
            if hab.nivel <= ficha.nivel:
                habilidades.append(hab)
        for hab in ficha.especie.habilidades:
            if hab.nivel <= ficha.nivel:
                habilidades.append(hab)
        for hab in ficha.classe.habilidades:
            if hab.nivel <= ficha.nivel:
                habilidades.append(hab)
        for subclasse in ficha.classe.subclasses:
            for hab in subclasse.hab_especificas:
                if hab.nivel <= ficha.nivel:
                    habilidades.append(hab)
        return habilidades

    def selecionar_magias_ativas_em_ficha(self, ficha: Ficha):
        magias = []
        for magia in ficha.lista_magias:
            if magia.nivel <= ficha.nivel:
                magias.append(magia)
        return magias

    def incluir_ficha(self):
        try:
            #dados basicos
            dados__basicos_ficha = self.__tela_fichas.pegar_dados_basicos_ficha()

            #classe
            self.__controlador_sistema.controlador_classes.listar_classes_e_subclasses()
            codigos_validos_class = list(self.__controlador_sistema.controlador_classes.dict_classes.keys()) + [0]
            codigo_classe = self.__tela_fichas.selecionar_obj_por_cod('classe', codigos_validos_class)
            if codigo_classe == 0:
                return False
            else:
                classe = self.__controlador_sistema.controlador_classes.dict_classes[codigo_classe]

            #subespecie
            self.__controlador_sistema.controlador_especies.listar_subespecies()
            codigos_valido_sub_esp = list(self.__controlador_sistema.controlador_especies.dict_subespecie.keys()) + [0]
            codigo_subespecie = self.__tela_fichas.le_int_ou_float('subespecie', codigos_valido_sub_esp)
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
                dados__basicos_ficha['moedas'],
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
            cod_valido_ficha = list(self.__dict_fichas.keys()) + [0]
            self.__tela_fichas.mensagem(f"{'Cod':^4} | {'Nome':^16}")
            for key, ficha in self.__dict_fichas.items():
                self.__tela_fichas.mostra_ficha_basica(
                    {
                        'cod': key,
                        'nome': ficha.nome
                    }
                )
            if selecao:
                identificador = self.__tela_fichas.selecionar_obj_por_cod(f'fichas', cod_valido_ficha)
                if identificador == 0:
                    return False
                else:
                    ficha = self.__dict_fichas[identificador]
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
                            'moedas': ficha.moedas,
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
                            'magias': [magia.nome for magia in self.selecionar_magias_ativas_em_ficha(ficha)],
                            'habilidades': [hab.nome for hab in self.selecionar_habilidades_aivas_em_ficha(ficha)]
                        }
                    )
        except Exception as e:
            self.__tela_fichas.mensagem(f"[ERRO INESPERADO] Erro ao listar os itens em ficha: {str(e)}")

    def excluir_fichas(self):
        try:
            self.listar_fichas()
            cod_validos = list(self.__dict_fichas.keys()) + [0]
            identificador = self.__tela_fichas.selecionar_obj_por_cod('ficha', cod_validos)
            if identificador == 0:
                return
            else:
                del self.__dict_fichas[identificador]
                self.__tela_fichas.mensagem('Ficha removida!')
                return True
        
        except KeyError as e:
            self.__tela_fichas.mensagem(f'[ERRO DE CHAVE] Erro ao excluir ficha, código não encontrado: {str(e)}')
        except Exception as e:
            self.__tela_fichas.mensagem(f'[ERRO INESPERADO] Erro ao excluir ficha: {str(e)}')
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

    def subir_nivel_de_uma_ficha(self):
            self.listar_fichas(selecao=False)
            cod_validos_ficha = list(self.__dict_fichas.keys()) + [0]
            identificador_ficha = self.__tela_fichas.selecionar_obj_por_cod('fichas', cod_validos_ficha)
            if identificador_ficha == 0:
                return False
            else:
                ficha = self.dict_fichas[identificador_ficha]
                ficha.subir_nivel()
                self.__tela_fichas.mensagem(f'Ficha "{ficha.nome} subiu para o nivel {ficha.nivel}!"')
                return True

    def alterar_vida_ficha(self):
        self.listar_fichas(selecao=False)
        cod_validos_ficha = list(self.__dict_fichas.keys()) + [0]
        identificador_ficha = self.__tela_fichas.selecionar_obj_por_cod('fichas', cod_validos_ficha)
        if identificador_ficha == 0:
            return False
        else:
            ficha = self.dict_fichas[identificador_ficha]
            valor = self.__tela_fichas.le_int_ou_float(
                'Digite o valor de vida a ser alterado (Utilize números negativos para subtrair vida): '
            )
            vida_antiga = ficha.vida_atual
            ficha.vida_atual += valor
            self.__tela_fichas.mensagem(f'Vida alterada {vida_antiga} -> {ficha.vida_atual}')
            if ficha.vida_atual <= 0:
                self.__tela_fichas.mensagem(f'O personagem "{ficha.nome}" está morrendo!')
            elif vida_antiga <= 0 and ficha.vida_atual > 0:
                self.__tela_fichas.mensagem(f'O personagem "{ficha.nome}" foi estabilizado! <3')
            return True

    def relatorio(self):
        if not self.__dict_fichas:
            self.__tela_fichas.mensagem("Nenhuma ficha cadastrada.")
            return False

        fichas = list(self.__dict_fichas.values())

        #Valores maiores
        personagem_com_maior_nivel = fichas[0]
        personagem_mais_ouro = fichas[0]
        personagem_mais_itens = fichas[0]
        personagem_maior_deslocamento = fichas[0]
        personagem_mais_magias = fichas[0]
        personagem_com_maior_dado_de_vida = fichas[0]
        personagem_maior_vida = fichas[0]
        personagem_com_mais_hab = fichas[0]

        total_magias = 0
        total_fichas = len(fichas)
        todas_classes = []
        todas_pericias = {}

        for ficha in fichas:
            if ficha.nivel > personagem_com_maior_nivel.nivel:
                personagem_com_maior_nivel = ficha
            if ficha.moedas > personagem_mais_ouro.moedas:
                personagem_mais_ouro = ficha
            if len(ficha.inventario) > len(personagem_mais_itens.inventario):
                personagem_mais_itens = ficha
            if ficha.deslocamento > personagem_maior_deslocamento.deslocamento:
                personagem_maior_deslocamento = ficha
            if  len(self.selecionar_magias_ativas_em_ficha(ficha)) > \
                len(self.selecionar_magias_ativas_em_ficha(personagem_mais_magias)):
                personagem_mais_magias = ficha
            if ficha.vida > personagem_maior_vida.vida:
                personagem_maior_vida = ficha
            if ficha.classe.dado_vida > personagem_com_maior_dado_de_vida.classe.dado_vida:
                personagem_com_maior_dado_de_vida = ficha
            if len(self.selecionar_habilidades_aivas_em_ficha(personagem_com_mais_hab)) > \
                len(self.selecionar_habilidades_aivas_em_ficha(ficha)):
                personagem_com_mais_hab = ficha

            total_magias += len(self.selecionar_magias_ativas_em_ficha(ficha))
            todas_classes.append(ficha.classe.nome)

            for pericia in ficha.pericias_treinadas:
                if pericia in todas_pericias:
                    todas_pericias[pericia] += 1
                else:
                    todas_pericias[pericia] = 1

        # Classe mais comum
        classe_mais_comum = todas_classes[0]
        qtd_classe_mais_comum = todas_classes.count(classe_mais_comum)
        for classe in todas_classes:
            qtd = todas_classes.count(classe)
            if qtd > qtd_classe_mais_comum:
                classe_mais_comum = classe
                qtd_classe_mais_comum = qtd

        # Perícia mais comum
        pericia_mais_comum = ""
        qtd_pericia_mais_comum = 0

        for pericia in todas_pericias:
            if todas_pericias[pericia] > qtd_pericia_mais_comum:
                pericia_mais_comum = pericia
                qtd_pericia_mais_comum = todas_pericias[pericia]

        # Maior atributo bruto
        maior_atributo = 0
        for ficha in fichas:
            for valor in ficha.atributos.values():
                if valor > maior_atributo:
                    maior_atributo = valor

        media_magias = total_magias / total_fichas

        dados_relatorio = {
            'maior_nivel': (personagem_com_maior_nivel.nome, personagem_com_maior_nivel.nivel),
            'mais_ouro': (personagem_mais_ouro.nome, personagem_mais_ouro.moedas),
            'mais_itens': (personagem_mais_itens.nome, len(personagem_mais_itens.inventario)),
            'maior_deslocamento': (personagem_maior_deslocamento.nome, personagem_maior_deslocamento.deslocamento),
            'mais_magias': (personagem_mais_magias.nome, len(personagem_mais_magias.lista_magias)),
            'maior_vida': (personagem_maior_vida.nome, personagem_maior_vida.vida),
            'maior_dado_vida': (personagem_com_maior_dado_de_vida.nome, personagem_com_maior_dado_de_vida.classe.dado_vida),
            'classe_mais_comum': (classe_mais_comum, qtd_classe_mais_comum),
            'pericia_mais_comum': (pericia_mais_comum, qtd_pericia_mais_comum),
            'maior_atributo': maior_atributo,
            'media_magias': round(media_magias, 2),
            'mais_hab': (personagem_com_mais_hab.nome, len(self.selecionar_habilidades_aivas_em_ficha(ficha)))
        }

        self.__tela_fichas.mostra_relatorio(dados_relatorio)
        return dados_relatorio

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.incluir_ficha,
            2: self.excluir_fichas,
            3: self.listar_fichas,
            4: self.alterar_vida_ficha,
            5: self.subir_nivel_de_uma_ficha,
            6: self.adicionar_item_ficha,
            7: self.remover_item_ficha,
            8: self.adicionar_magia_ficha,
            9: self.remover_magia_ficha,
            10: self.relatorio,
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
