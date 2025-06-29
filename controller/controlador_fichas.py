from model.ficha import Ficha
from views.tela_fichas import TelaFichas
from typing import TYPE_CHECKING
from DAOs.ficha_dao import FichaDao
from model.exceptions.exception_dict_vazio import *
from model.exceptions.excpetion_ficha import *
if TYPE_CHECKING:
    from controller.controlador_sistema import ControladorSistema


class ControladorFichas:
    def __init__(self, controlador_sistema: "ControladorSistema"):
        self.__controlador_sistema = controlador_sistema
        self.__tela_fichas = TelaFichas()
        self.__ficha_dao = FichaDao()

        # O dicionário de "Fichas" iniciaria normalmente vazio, porém
        # para demonstração, utilzaremos alguns objetos já instanciados. 
        # Estes objetos receberão códigos acima de 999.
        """
        self.__dict_fichas: dict[int, Ficha] = {
            1000: Ficha('Maria', 'Alta e de cabelo azul','nasceu, cresceu, viveu.', 100,
            self.__controlador_sistema.controlador_classes.dict_classes[1001], 
            self.__controlador_sistema.controlador_especies.dict_subespecie[1000],
            ['Percepção', 'Presdigitação', 'Sobrevivência', 'Persuasão', 'Performance'],
            [10, 8, 13, 14, 12, 16]),

            1001: Ficha('Sindur', 'Baixo, com uma longa barba laranja e calvo', 'nasceu, não cresceu, viveu muito', 1341,
            self.__controlador_sistema.controlador_classes.dict_classes[1002],
            self.__controlador_sistema.controlador_especies.dict_subespecie[1001],
            ['Atletismo', 'Lidar com Animais', 'Percepção', 'Intimidação', 'Natureza'],
            [20, 15, 18, 12, 7, 13]),

            1002: Ficha('Kashimir', 'Alto, Velho, com uma cicatriz na bochecha esquerda', 'nasceu, sofreu, creseceu, vendeu a alma, viveu', 6547,
            self.__controlador_sistema.controlador_classes.dict_classes[1003],
            self.__controlador_sistema.controlador_especies.dict_subespecie[1005],
            ['Persuasão', 'Arcanismo', 'Natureza', 'Performace', 'História'],
            [7, 15, 12, 11, 14, 18]),
            1003: Ficha('Sebo', 'Pequeno, Calvo, Magro e Novo', 'Nasceu, Não vive e leu', 100,
            self.__controlador_sistema.controlador_classes.dict_classes[1000],
            self.__controlador_sistema.controlador_especies.dict_subespecie[1002],
            ['Arcanismo', 'Intuição', 'Religião', 'Medicina', 'Furtividade'],
            [7, 14, 11, 18, 15, 13]),
            1004: Ficha('Barmarlee', 'Musculoso, coberto de cicatrizes, velho, barba mal feita', 'nasceu, casou, cresceu, quase foi, sobreviveu', 2341,
            self.__controlador_sistema.controlador_classes.dict_classes[1002],
            self.__controlador_sistema.controlador_especies.dict_subespecie[1003],
            ['Historia', 'Atletismo', 'Intimidação', 'Furtividade', 'Medicina'],
            [17, 13, 16, 12, 12, 8])}
            """
    def selecionar_habilidades_ativas_em_ficha(self, ficha: Ficha):
        try:
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
            if ficha.subclasse:
                for hab in ficha.subclasse.hab_especificas:
                    if hab.nivel <= ficha.nivel:
                        habilidades.append(hab)
            return habilidades
        except Exception as e:
                    self.__tela_fichas.mensagem(f'[ERRO INESPERADO] Erro ao selecionar habilidade: {str(e)}')

    def selecionar_magias_ativas_em_ficha(self, ficha: Ficha):
        try:
            magias = []
            for magia in ficha.lista_magias:
                if magia.nivel <= ficha.nivel:
                    magias.append(magia)
            return magias
        except Exception as e:
            self.__tela_fichas.mensagem(f'[ERRO INESPERADO] Erro ao selecionar magia: {str(e)}')

    def incluir_ficha(self):
        try:
            dados = self.__tela_fichas.pegar_dados_ficha(
                [classe.nome for classe in self.__controlador_sistema.controlador_classes.classe_DAO.get_all()],
                [especie.nome for especie in self.__controlador_sistema.controlador_especies.subespecie_DAO.get_all()]
            )
            for classe in self.__controlador_sistema.controlador_classes.classe_DAO.get_all():
                if classe.nome == dados['classe']:
                    classe_ficha = classe

            for subespecie in self.__controlador_sistema.controlador_especies.subespecie_DAO.get_all():
                if subespecie.nome == dados['subespecie']:
                    subespecie_ficha = subespecie

            nova_ficha = Ficha(
                dados['nome'],
                dados['descricao_fisica'],
                dados['historia'],
                dados['moedas'],
                classe_ficha,
                subespecie_ficha,
                dados['pericias_treinadas'],
                dados['atributos']
            )
            self.__ficha_dao.add(nova_ficha)
            self.__tela_fichas.mensagem('SUCESSO')
        except KeyError as e:
            self.__tela_fichas.mensagem(f"[ERRO] Dado ausente: {str(e)}")
        except Exception as e:
            self.__tela_fichas.mensagem(f'[ERRO INESPERADO] Erro ao incluir ficha: {str(e)}')

    def listar_fichas(self, selecao=True):
        try:
            cod_valido_ficha = list(self.__ficha_dao.get_keys()) + [0]

            dados = []
            if self.__ficha_dao.cache:
                for key, ficha in self.__ficha_dao.cache.items():
                    linha = [
                        key,
                        ficha.nome
                    ]
                    dados.append(linha)

                HEADER = ['Cód', 'Nome Personagem']
                self.__tela_fichas.exibir_tabela(cabecalho=HEADER, dados=dados, nome_objeto='Ficha')

                if selecao:
                    identificador = self.__tela_fichas.selecionar_obj_por_cod(f'fichas', cod_valido_ficha)
                    if identificador == 0:
                        return False
                    else:
                        ficha = self.__ficha_dao.cache[identificador]
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
                                'moedas': 0,
                                'classe': ficha.classe.nome,
                                'subclasse': 'Não há' if ficha.subclasse == None else ficha.subclasse.nome,
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
                                'habilidades': [hab.nome for hab in self.selecionar_habilidades_ativas_em_ficha(ficha)]
                            }
                        )
            else:
                raise DictVazioException()
        except DictVazioException as e:
            self.__tela_fichas.mensagem(e)
        except Exception as e:
            self.__tela_fichas.mensagem(f"[ERRO INESPERADO] Erro ao listar as fichas: {str(e)}")

    def excluir_fichas(self):
        try:
            self.listar_fichas(selecao=False)
            cod_validos = list(self.__ficha_dao.get_keys()) + [0]
            identificador = self.__tela_fichas.selecionar_obj_por_cod('selecione a ficha', cod_validos)
            if identificador == 0:
                return
            else:
                self.__ficha_dao.remove(identificador)
                self.__tela_fichas.mensagem('Ficha removida!')
                return True
        except TypeError as e:
            self.__tela_fichas.mensagem(f'[ERRO] Algum valor de entrada não foi inserido como esperado.')
        except KeyError as e:
            self.__tela_fichas.mensagem(f'[ERRO DE CHAVE] Erro ao excluir ficha, código não encontrado: {str(e)}')
        except Exception as e:
            self.__tela_fichas.mensagem(f'[ERRO INESPERADO] Erro ao excluir ficha: {str(e)}')

    def adicionar_item_ficha(self):
        try:
            self.listar_fichas(selecao=False)
            cod_validos_ficha = list(self.__ficha_dao.get_keys()) + [0]
            identificador_ficha = self.__tela_fichas.selecionar_obj_por_cod('fichas', cod_validos_ficha)
            if identificador_ficha == 0:
                return False
            else:
                item = self.__controlador_sistema.controlador_itens.item_DAO.cache
                self.__controlador_sistema.controlador_itens.listar_itens()
                codigos_validos_item = list(item.keys()) + [0]
                identificador_item = self.__tela_fichas.selecionar_obj_por_cod('item', codigos_validos_item)
                if identificador_item == 0:
                    return False
                else:
                    ficha = self.__ficha_dao.cache[identificador_ficha]
                    ficha.add_item_inventario(item[identificador_item])
                    self.__ficha_dao.update(identificador_ficha, ficha)
                    self.__tela_fichas.mensagem('Item adicionado ao inventário!')
                    return True
        except TypeError as e:
            self.__tela_fichas.mensagem(f'[ERRO] Algum valor de entrada não foi inserido como esperado.')
        except KeyError as e:
            self.__tela_fichas.mensagem(f'[ERRO DE CHAVE] Algum elemento não foi encontrado: {e}')
        except Exception as e:
            self.__tela_fichas.mensagem(f'[ERRO INESPERADO] Erro ao alterar Item: {e}')
            
    def adicionar_magia_ficha(self):
        try:
            self.listar_fichas(selecao=False)
            cod_validos_ficha = list(self.__ficha_dao.get_keys()) + [0]
            identificador_ficha = self.__tela_fichas.selecionar_obj_por_cod('fichas', cod_validos_ficha)
            if identificador_ficha == 0:
                return False
            else:
                magias = self.__controlador_sistema.controlador_magias.magia_DAO.cache
                self.__controlador_sistema.controlador_magias.listar_magias()
                codigos_validos_magia = list(magias.keys()) + [0]
                identificador_magia = self.__tela_fichas.selecionar_obj_por_cod('magia', codigos_validos_magia)
                if identificador_magia == 0:
                    return False
                else:
                    ficha = self.__ficha_dao.cache[identificador_ficha]
                    ficha.add_magia(magias[identificador_magia])
                    self.__ficha_dao.update(identificador_ficha, ficha)
                    self.__tela_fichas.mensagem('Magia adicionada ao inventário!')
                    return True
        except TypeError as e:
            self.__tela_fichas.mensagem(f'[ERRO] Algum valor de entrada não foi inserido como esperado.')
        except KeyError as e:
            self.__tela_fichas.mensagem(f'[ERRO DE CHAVE] Algum elemento não foi encontrado: {e}')
        except Exception as e:
            self.__tela_fichas.mensagem(f'[ERRO INESPERADO] Erro ao alterar Magia: {e}')

    def remover_item_ficha(self):
        try:
            self.listar_fichas(selecao=False)
            cod_validos_ficha = list(self.__ficha_dao.get_keys()) + [0]
            identificador_ficha = self.__tela_fichas.selecionar_obj_por_cod('fichas', cod_validos_ficha)
            if identificador_ficha == 0:
                return False
            else:
                ficha = self.__ficha_dao.cache[identificador_ficha]
                itens = self.__controlador_sistema.controlador_itens.item_DAO.cache
                self.__controlador_sistema.controlador_itens.listar_itens()
                codigos_validos_item = list(itens.keys()) + [0]
                itens_personagem = [item.nome for item in ficha.inventario]
                self.__tela_fichas.mensagem(f'Itens do Personagem: {itens_personagem}')
                identificador_item = self.__tela_fichas.selecionar_obj_por_cod('item', codigos_validos_item)
                if identificador_item == 0:
                    return False
                else: 
                    
                    ficha.rm_item_inventario(itens[identificador_item])
                    self.__ficha_dao.update(identificador_ficha, ficha)
                    self.__tela_fichas.mensagem('Item removido do inventário!')
                    return True
        except TypeError as e:
            self.__tela_fichas.mensagem(f'[ERRO] Algum valor de entrada não foi inserido como esperado.')                
        except KeyError as e:
            self.__tela_fichas.mensagem(f'[ERRO DE CHAVE] Algum elemento não foi encontrado: {e}')
        except Exception as e:
            self.__tela_fichas.mensagem(f'[ERRO INESPERADO] Erro ao alterar Item: {e}')
            
    def remover_magia_ficha(self):
        try:
            self.listar_fichas(selecao=False)
            cod_validos_ficha = list(self.__ficha_dao.get_keys()) + [0]
            identificador_ficha = self.__tela_fichas.selecionar_obj_por_cod('fichas', cod_validos_ficha)
            if identificador_ficha == 0:
                return False
            else:
                ficha = self.__ficha_dao.cache[identificador_ficha]
                magias = self.__controlador_sistema.controlador_magias.magia_DAO.cache
                self.__controlador_sistema.controlador_magias.listar_magias()
                codigos_validos_magia = list(magias.keys()) + [0]
                magias_personagen = [magia.nome for magia in ficha.lista_magias]
                self.__tela_fichas.mensagem(f'Magias do Personagem: {magias_personagen}')
                identificador_magia = self.__tela_fichas.selecionar_obj_por_cod('magia', codigos_validos_magia)
                if identificador_magia == 0:
                    return False
                else:
                    ficha.rm_magia(magias[identificador_magia])
                    self.__ficha_dao.update(identificador_ficha, ficha)
                    self.__tela_fichas.mensagem('Magia removida!')
                    return True
        except TypeError as e:
            self.__tela_fichas.mensagem(f'[ERRO] Algum valor de entrada não foi inserido como esperado.')
        except KeyError as e:
            self.__tela_fichas.mensagem(f'[ERRO DE CHAVE] Algum elemento não foi encontrado: {e}')
        except Exception as e:
            self.__tela_fichas.mensagem(f'[ERRO INESPERADO] Erro ao alterar Magia: {e}')

    def subir_nivel_de_uma_ficha(self):
            self.listar_fichas(selecao=False)
            cod_validos_ficha = list(self.__ficha_dao.get_keys()) + [0]
            identificador_ficha = self.__tela_fichas.selecionar_obj_por_cod('fichas', cod_validos_ficha)
            if identificador_ficha == 0:
                return False
            else:
                ficha = self.__ficha_dao.cache[identificador_ficha]
                if ficha.nivel == 2:
                    infos = {'nomes_sub': [sub.nome for sub in ficha.classe.subclasses],
                            'habilidades_sub': [[hab.nome for hab in sub.hab_especificas] for sub in ficha.classe.subclasses]}
                    self.__controlador_sistema.controlador_classes.tela_classes.mostra_classe_e_subclasse(infos, classe=False)
                    subclasse_ecolhida = self.__tela_fichas.selecionar_obj_por_cod(
                        'Digite a subclasse que deseja se aperfeiçoar (1, 2 ou 3 - de cima para baixo): ', [1, 2, 3])
                    ficha.subclasse = ficha.classe.subclasses[subclasse_ecolhida - 1]
                ficha.subir_nivel()
                self.__ficha_dao.update(identificador_ficha, ficha)
                self.__tela_fichas.mensagem(f'Ficha "{ficha.nome} subiu para o nivel {ficha.nivel}!"')
                return True

    def alterar_vida_ficha(self):
        self.listar_fichas(selecao=False)
        cod_validos_ficha = list(self.__ficha_dao.get_keys()) + [0]
        identificador_ficha = self.__tela_fichas.selecionar_obj_por_cod('fichas', cod_validos_ficha)
        if identificador_ficha == 0:
            return False
        else:
            ficha = self.__ficha_dao.cache[identificador_ficha]
            valor = self.__tela_fichas.ler_vida_alterada()
            vida_antiga = ficha.vida_atual
            ficha.vida_atual += valor
            self.__tela_fichas.mensagem(f'Vida alterada {vida_antiga} -> {ficha.vida_atual}')
            if ficha.vida_atual <= 0:
                self.__tela_fichas.mensagem(f'O personagem "{ficha.nome}" está morrendo!')
            elif vida_antiga <= 0 and ficha.vida_atual > 0:
                self.__tela_fichas.mensagem(f'O personagem "{ficha.nome}" foi estabilizado! <3')
            self.__ficha_dao.update(identificador_ficha, ficha)
            return True

    def relatorio(self):
        if not self.__ficha_dao.cache:
            self.__tela_fichas.mensagem("Nenhuma ficha cadastrada.")
            return False

        fichas = list(self.__ficha_dao.get_all())

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
            if len(self.selecionar_habilidades_ativas_em_ficha(personagem_com_mais_hab)) > \
                len(self.selecionar_habilidades_ativas_em_ficha(ficha)):
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
            'mais_magias': (personagem_mais_magias.nome, len(self.selecionar_magias_ativas_em_ficha(personagem_mais_magias))),
            'maior_vida': (personagem_maior_vida.nome, personagem_maior_vida.vida),
            'maior_dado_vida': (personagem_com_maior_dado_de_vida.nome, personagem_com_maior_dado_de_vida.classe.dado_vida),
            'classe_mais_comum': (classe_mais_comum, qtd_classe_mais_comum),
            'pericia_mais_comum': (pericia_mais_comum, qtd_pericia_mais_comum),
            'maior_atributo': maior_atributo,
            'media_magias': round(media_magias, 2),
            'mais_hab': (personagem_com_mais_hab.nome, len(self.selecionar_habilidades_ativas_em_ficha(ficha)))
        }

        HEADER = ['Métrica', 'Valor', 'Detalhe']
        dados = [
            ["Maior Nível", personagem_com_maior_nivel.nome, personagem_com_maior_nivel.nivel],
            ["Mais Ouro", personagem_mais_ouro.nome, personagem_mais_ouro.moedas],
            ["Mais Itens", personagem_mais_itens.nome, len(personagem_mais_itens.inventario)],
            ["Maior Deslocamento", personagem_maior_deslocamento.nome, personagem_maior_deslocamento.deslocamento],
            ["Mais Magias", personagem_mais_magias.nome, len(self.selecionar_magias_ativas_em_ficha(personagem_mais_magias))],
            ["Maior Vida", personagem_maior_vida.nome, personagem_maior_vida.vida],
            ["Maior Dado de Vida", personagem_com_maior_dado_de_vida.nome, personagem_com_maior_dado_de_vida.classe.dado_vida],
            ["Classe Mais Comum", classe_mais_comum, qtd_classe_mais_comum],
            ["Perícia Mais Comum", pericia_mais_comum, qtd_pericia_mais_comum],
            ["Maior Atributo", '-', maior_atributo],
            ["Média de Magias", "-", round(media_magias, 2)],
            ["Mais Habilidades", personagem_com_mais_hab.nome, len(self.selecionar_habilidades_ativas_em_ficha(ficha))]
        ]

        self.__tela_fichas.exibir_tabela(cabecalho=HEADER, dados=dados, nome_objeto='Relatório de Fichas')
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
    def ficha_dao(self):
        return self.__ficha_dao
