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
        for especie in self.dict_especie.values():
            if especie.nome == nome:
                return especie
        return None
    
    def pega_subespecie_por_nome(self, nome: str):
        for subespecie in self.dict_subespecie.values():
            if subespecie.nome == nome:
                return nome
        return None
    
    def incluir_especie(self):
        dados_especie = self.tela_especies.pegar_dados_especie()
        e = self.pega_especie_por_nome(dados_especie['nome'])
        if e is None:
            especie = Especie(
                dados_especie['nome'],
                dados_especie['deslocamento'],
                dados_especie['altura'],
                    )
            self.dict_especie[self.__cod_esp] = especie
            self.__cod_esp +=1
            self.tela_especies.mensagem('Espécie criada com sucesso!')
        else:
            self.tela_especies.mensagem('A espécie criada já existe.')

    def incluir_subespecie(self):
        self.listar_especies()
        cod_validos = list(self.dict_especie.keys()) + [0]
        identificador = self.tela_especies.selecionar_obj_por_cod('especie', cod_validos)
        especie = self.dict_especie[identificador]
        dados_subespecie = self.tela_especies.pegar_dados_subespecie(especie.nome)
        s = self.pega_subespecie_por_nome(dados_subespecie['nome'])
        if s is None:
            subespecie = Subespecie(
                especie.nome, 
                dados_subespecie['nome'],
                especie.deslocamento,
                especie.altura,
            )
            self.dict_subespecie[self.__cod_sub_esp] = subespecie
            self.__cod_sub_esp += 1
            self.tela_especies.mensagem('Subespecie criada com sucesso!')
        else:
            self.tela_especies.mensagem('A subespecie criada ja existe!')

    def listar_especies(self):
        self.tela_especies.mensagem(f'{"Cod":^4} | {"Nome":^16} | {"Deslocamento":^16} | {"Altura média(cm)":^18} | {"Habilidade(s)":^9}')
        for key, especie in self.dict_especie.items():
            self.tela_especies.mostra_especie(
                {
                    'cod': key,
                    'nome': especie.nome,
                    'deslocamento': especie.deslocamento,
                    'altura': especie.altura,
                    'habilidades': especie.habilidades                 
                }
            )
    #Arrumar isso aqui junto
    def listar_subespecies(self):
        self.__tela_especies.mensagem(f'{"Cod":^4} | {"Nome":^16} | {"Deslocamento":^16} | {"Altura média":^18} | {"Habilidade(s)":^9} | {"Habilidades(s) específicas":^25}')
        for key, subespecie in self.dict_subespecie.items():
            self.tela_especies.mostra_subespecie(
                {
                    'habilidades' : subespecie.habilidades
                }
            )
        
    def excluir_especie(self):
        self.listar_especies()
        try:
            cod_validos = list(self.dict_especie.keys()) + [0]
            identificador = self.tela_especies.selecionar_obj_por_cod('especie', cod_validos)
            if identificador == 0:
                return
            else:
                del self.dict_especie[identificador]
                self.tela_especies.mensagem('Especie removida!')
            return True
        except:
            return False
        
    def excluir_subsespecie(self):
        self.listar_subespecies()
        try:
            cod_validos = list(self.dict_subespecie.keys()) + [0]
            identificador = self.tela_especies.selecionar_obj_por_cod('subespecie', cod_validos)
            if identificador == 0:
                return
            else:
                del self.dict_subespecie[identificador]
                self.tela_especies.mensagem('Subespecie removida!')
            return True
        except:
            return False
        
    def alterar_especie_por_cod(self):
        self.listar_especies()
        try:
            cod_validos = list(self.dict_especie.keys()) + [0]
            identificador = self.__tela_especies.selecionar_obj_por_cod('especie', cod_validos)
            if identificador == 0:
                return
            especie = self.dict_especie[identificador]
            dados_novos = self.tela_especies.pegar_dados_especie()
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
            cod_validos = list(self.dict_especie.keys()) + [0]
            identificador = self.tela_especies.selecionar_obj_por_cod('subespecie', cod_validos)
            if identificador == 0:
                return
            subespecie = self.dict_subespecie[identificador]
            dados_novos = self.tela_especies.pegar_dados_subespecie()
            subespecie.habilidades = dados_novos['habilidades']
            return True
        except:
            return False
       
    def add_habilidade_especie(self):
        self.listar_especies()
        try:
            cod_validos_esp = list(self.dict_especie.keys()) + [0]
            identificador_esp = self.tela_especies.selecionar_obj_por_cod('especie', cod_validos_esp)
            if identificador_esp == 0:
                return
            else:
                habilidade = self.controlador_sistema.controlador_habilidades.dict_habilidades
                self.controlador_sistema.controlador_habilidades.listar_habilidades()
                cod_validos_hab = list(habilidade.keys()) + [0]
                identificador_hab = self.tela_especies.selecionar_obj_por_cod('habilidade', cod_validos_hab)
                if habilidade[identificador_hab].origem == 'especie':
                    if identificador_hab == 0:
                        return
                    else:
                        especie = self.dict_especie[identificador_esp]
#Printar/Excluir nome e código(nesse e nos 3 abaixo)
                        especie.habilidades.append(habilidade[identificador_hab].nome)
                        self.tela_especies.mensagem('Hablidade adicionada!')
                        return True
                else:
                    self.tela_especies.mensagem('Origem invalida')
                    return
        except:
            return False
        

    def add_habilidade_subespecie(self):
        self.listar_subespecies()
        try:
            cod_validos_sub = list(self.dict_subespecie.keys()) + [0]
            identificador_sub = self.tela_especies.selecionar_obj_por_cod('subespecie', cod_validos_sub)
            if identificador_sub == 0:
                return
            else:
                habilidade = self.controlador_sistema.controlador_habilidades.dict_habilidades
                cod_validos_hab = list(habilidade.keys()) + [0]
                identificador_hab = self.tela_especies.selecionar_obj_por_cod('habilidade', cod_validos_hab)
                self.controlador_sistema.controlador_habilidades.listar_habilidades()
                if habilidade[identificador_hab].origem == 'subespecie':
                    if identificador_hab == 0:
                        return
                    else:
                        subespecie = self.dict_especie[identificador_sub]
                        subespecie.habilidades.append(habilidade[identificador_hab].nome)
                        self.tela_especies.mensagem('Hablidade adicionada!')
                        return True
                else:
                    self.tela_especies.mensagem('Origem invalida')
                    return
        except:
            return False
        
    def remove_habilidade_especie(self):
        self.listar_especies()
        try:
            cod_valido_esp = list(self.dict_especie.keys()) + [0]
            identificador_esp = self.tela_especies.selecionar_obj_por_cod('especie', cod_valido_esp)
            especie = self.dict_especie[identificador_esp]
            if identificador_esp == 0:
                return
            else:
                habilidade = self.controlador_sistema.controlador_habilidades.dict_habilidades
                cod_valido_hab = list(habilidade.keys()) + [0]
                self.tela_especies.mensagem(f'Lista de habilidades: {especie.habilidades}')
                identificador_hab = self.tela_especies.selecionar_obj_por_cod('habilidade', cod_valido_hab)
                if identificador_hab == 0:
                    return
                else:
                    especie.habilidades.remove(habilidade[identificador_hab].nome)
                    self.tela_especies.mensagem('Habilidade Removida!')
                    return True
        except:
            return False
    
    def remove_habilidade_subespecie(self):
        self.listar_subespecies()
        try:
            cod_validos_sub = list(self.dict_subespecie.keys()) + [0]
            identificador_sub = self.tela_especies.selecionar_obj_por_cod('subespecie', cod_validos_sub)
            if identificador_sub == 0:
                return
            else:
                habilidade = self.controlador_sistema.controlador_habilidades.dict_habilidades
                cod_validos_hab = list(habilidade.keys())
                self.tela_especies.mensagem(f'Lista de habilidades: {subespecie.habilidades}')
                identificador_hab = self.tela_especies.selecionar_obj_por_cod('habilidade', cod_validos_hab)
                if identificador_hab == 0:
                    return
                else:
                    subespecie = self.dict_subespecie[identificador_sub]
                    subespecie.habilidades.remove(habilidade[identificador_hab].nome)
                    self.tela_especies.mensagem('Habilidade Removida!')
                    return True
        except:
            return False

    def retornar(self):
        self.controlador_sistema.abre_tela()
    
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
            opc = self.tela_especies.mostra_tela_especie()
            metodo = opcoes[opc]
            metodo()

    def abre_tela_subespecie(self):
        opcoes= {
            1: self.incluir_subespecie,
            2: self.excluir_subsespecie,
            3: self.listar_subespecies,
            4: self.alterar_subespecie_por_cod,
            5: self.add_habilidade_subespecie,
            6:self.remove_habilidade_subespecie,
            0: self.abre_tela
        }
        while True:
            opc = self.tela_especies.mostra_tela_subespecie()
            metodo = opcoes[opc]
            metodo()

    def abre_tela(self):
        opcoes = {
            1: self.abre_tela_especie,
            2: self.abre_tela_subespecie,
            0: self.retornar
        }
        while True:
            opc = self.tela_especies.mostra_tela()
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
