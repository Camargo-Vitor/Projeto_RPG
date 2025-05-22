from views.tela_especies import TelaEspecies
from model.especie import Especie
from model.subespecie import Subespecie
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller.controlador_sistema import ControladorSistema


class ControladorEspecies:
    def __init__(self, controlador_sistema: "ControladorSistema"):
        self.__controlador_sistema = controlador_sistema
        self.__dict_especie: dict[int, Especie] = dict()
        self.__dict_subespecie: dict[int, Subespecie] = dict()
        self.__tela_especies = TelaEspecies()
        self.__cod_esp = 1
        self.__cod_sub_esp = 1

    def pega_especie_por_nome(self, nome: str):
        for especie in self.__dict_especie.values():
            if especie.nome == nome:
                return especie
        return None
    
    def pega_subespecie_por_nome(self, nome: str):
        for subespecie in self.__dict_subespecie.values():
            if subespecie.nome == nome:
                return nome
        return None
    
    def incluir_especie(self):
        dados_especie = self.__tela_especies.pegar_dados_especie()
        e = self.pega_especie_por_nome(dados_especie['nome'])
        if e is None:
            especie = Especie(
                dados_especie['nome'],
                dados_especie['deslocamento'],
                dados_especie['altura'],
                    )
            self.__dict_especie[self.__cod_esp] = especie
            self.__cod_esp +=1
            self.__tela_especies.mensagem('Espécie criada com sucesso!')
        else:
            self.__tela_especies.mensagem('A espécie criada já existe.')

    def incluir_subespecie(self):
        self.listar_especies()
        cod_validos = list(self.__dict_especie.keys()) + [0]
        identificador = self.__tela_especies.selecionar_obj_por_cod('especie', cod_validos)
        if identificador == 0:
            return False
        especie = self.__dict_especie[identificador]
        dados_subespecie = self.__tela_especies.pegar_dados_subespecie(especie.nome)
        s = self.pega_subespecie_por_nome(dados_subespecie['nome'])
        if s is None:
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
        else:
            self.__tela_especies.mensagem('A subespecie criada ja existe!')

    def listar_especies(self):
        self.__tela_especies.mensagem(f'{"Cod":^4} | {"Nome":^16} | {"Deslocamento":^16} | {"Altura média(cm)":^18} | {"Habilidade(s)":^9}')
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

    def listar_subespecies(self):
        self.__tela_especies.mensagem(f'{"Cod":^4} | {"Nome":^16} | {"Deslocamento":^16} | {"Altura média":^18} | {"Habilidade(s)":^9} | {"Habilidades(s) específicas":^25}')
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

    def excluir_especie(self):
        self.listar_especies()
        try:
            cod_validos = list(self.__dict_especie.keys()) + [0]
            identificador = self.__tela_especies.selecionar_obj_por_cod('especie', cod_validos)
            if identificador == 0:
                return
            else:
                for key, subespecie in self.__dict_subespecie.items():
                    if super(Subespecie, subespecie).nome == self.__dict_especie[identificador].nome:
                        del self.dict_subespecie[key]
                del self.__dict_especie[identificador]
                self.__tela_especies.mensagem('Especie removida!')
            return True
        except:
            return False
        
    def excluir_subsespecie(self):
        self.listar_subespecies()
        try:
            cod_validos = list(self.__dict_subespecie.keys()) + [0]
            identificador = self.__tela_especies.selecionar_obj_por_cod('subespecie', cod_validos)
            if identificador == 0:
                return
            else:
                del self.__dict_subespecie[identificador]
                self.__tela_especies.mensagem('Subespecie removida!')
            return True
        except:
            return False
        
    def alterar_especie_por_cod(self):
        self.listar_especies()
        try:
            cod_validos = list(self.__dict_especie.keys()) + [0]
            identificador = self.__tela_especies.selecionar_obj_por_cod('especie', cod_validos)
            if identificador == 0:
                return
            especie = self.__dict_especie[identificador]
            dados_novos = self.__tela_especies.pegar_dados_especie()
            especie.nome = dados_novos['nome']
            especie.deslocamento = dados_novos['deslocamento']
            especie.altura = dados_novos['altura']
            especie.habilidades = dados_novos ['habilidades']
            return True
        except:
            return False

    def alterar_subespecie_por_cod(self):
        self.listar_subespecies()
        try:
            cod_validos = list(self.__dict_subespecie.keys()) + [0]
            identificador = self.__tela_especies.selecionar_obj_por_cod('subespecie', cod_validos)
            if identificador == 0:
                return
            subespecie = self.__dict_subespecie[identificador]
            dados_novos = self.__tela_especies.pegar_dados_subespecie(super(Subespecie, subespecie).nome)
            self.dict_subespecie[identificador].nome_sub = dados_novos['nome']
            self.__tela_especies.mensagem('Alterado com sucesso!')
            return True
        except:
            return False
       
    def add_habilidade_especie(self):
        self.listar_especies()
        try:
            cod_validos_esp = list(self.__dict_especie.keys()) + [0]
            identificador_esp = self.__tela_especies.selecionar_obj_por_cod('especie', cod_validos_esp)
            if identificador_esp == 0:
                return
            else:
                habilidade = self.__controlador_sistema.controlador_habilidades.dict_habilidades
                self.__controlador_sistema.controlador_habilidades.listar_habilidades()
                cod_validos_hab = list(habilidade.keys()) + [0]
                identificador_hab = self.__tela_especies.selecionar_obj_por_cod('habilidade', cod_validos_hab)
                if habilidade[identificador_hab].origem == 'especie':
                    if identificador_hab == 0:
                        return
                    else:
                        especie = self.__dict_especie[identificador_esp]
                        especie.add_habilidade(habilidade[identificador_hab])
                        self.__tela_especies.mensagem('Hablidade adicionada!')
                        return True
                else:
                    self.__tela_especies.mensagem('Origem invalida')
                    return
        except:
            return False
        

    def add_habilidade_subespecie(self):
        self.listar_subespecies()
        try:
            cod_validos_sub = list(self.__dict_subespecie.keys()) + [0]
            identificador_sub = self.__tela_especies.selecionar_obj_por_cod('subespecie', cod_validos_sub)
            if identificador_sub == 0:
                return
            else:
                habilidades = self.__controlador_sistema.controlador_habilidades.dict_habilidades
                cod_validos_hab = list(habilidades.keys()) + [0]
                self.__controlador_sistema.controlador_habilidades.listar_habilidades()
                identificador_hab = self.__tela_especies.selecionar_obj_por_cod('habilidade', cod_validos_hab)
                if identificador_hab == 0:
                    return
                elif habilidades[identificador_hab].origem == 'subespecie':
                    subespecie = self.__dict_subespecie[identificador_sub]
                    subespecie.add_hab_sub(habilidades[identificador_hab])
                    self.__tela_especies.mensagem('Hablidade adicionada!')
                    return True
                else:
                    self.__tela_especies.mensagem('Origem invalida')
                    return
        except:
            return False
        
    def remove_habilidade_especie(self):
        self.listar_especies()
        try:
            cod_valido_esp = list(self.__dict_especie.keys()) + [0]
            identificador_esp = self.__tela_especies.selecionar_obj_por_cod('especie', cod_valido_esp)
            especie = self.__dict_especie[identificador_esp]
            if identificador_esp == 0:
                return
            else:
                habilidade = self.__controlador_sistema.controlador_habilidades.dict_habilidades
                cod_valido_hab = list(habilidade.keys()) + [0]
                self.__controlador_sistema.controlador_habilidades.listar_habilidades()
                identificador_hab = self.__tela_especies.selecionar_obj_por_cod('habilidade', cod_valido_hab)
                if identificador_hab == 0:
                    return
                else:
                    especie.rm_hab(habilidade[identificador_hab])
                    self.__tela_especies.mensagem('Habilidade Removida!')
                    return True
        except:
            return False
    
    def remove_habilidade_subespecie(self):
        self.listar_subespecies()
        try:
            cod_validos_sub = list(self.__dict_subespecie.keys()) + [0]
            identificador_sub = self.__tela_especies.selecionar_obj_por_cod('subespecie', cod_validos_sub)
            if identificador_sub == 0:
                return
            else:
                habilidade = self.__controlador_sistema.controlador_habilidades.dict_habilidades
                subespecie = self.__dict_subespecie[identificador_sub]
                cod_validos_hab = list(habilidade.keys())
                self.__controlador_sistema.__controlador_habilidades.listar_habilidades()
                identificador_hab = self.__tela_especies.selecionar_obj_por_cod('habilidade', cod_validos_hab)
                if identificador_hab == 0:
                    return
                else:
                    subespecie.rm_hab_sub(habilidade[identificador_hab])
                    self.__tela_especies.mensagem('Habilidade Removida!')
                    return True
        except:
            return False

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
            2: self.excluir_subsespecie,
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
