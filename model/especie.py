from model.habilidade import Habilidade


class Especie():
    def __init__(self,
                 nome: str,
                 deslocamento: float,
                 altura: int,
                 habilidades: list[Habilidade] = []):
        self.__nome = nome
        self.__deslocamento = deslocamento
        self.__altura = altura
        self.__habilidades = habilidades

    @property
    def nome(self):     
        return self.__nome

    @property
    def altura(self):
        return self.__altura

    @property
    def deslocamento(self):
        return self.__deslocamento 

    @property
    def habilidades(self):
        return self.__habilidades

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise ValueError("[ERRO] Nome não alterado, valor inválido")

    @altura.setter
    def altura(self, altura):
        if isinstance(altura, int):
            self.__altura = altura
        else:    
            raise ValueError("[ERRO] Altura não alterado, valor inválido")

    @deslocamento.setter
    def deslocamento(self, deslocamento):
        if isinstance(deslocamento, float):
            self.__deslocamento = deslocamento
        else:
            raise ValueError("[ERRO] Deslocamento não alterado, valor inválido")

    def add_habilidade(self, habilidade: Habilidade):
        if isinstance(habilidade, Habilidade) and habilidade.origem == 'especie':
            self.habilidades.append(habilidade)
        else:
            raise ValueError("[ERRO] Habilidade não adicionada, valor inválido \
                              (verificar origem da habilidade)")

    def rm_hab(self, habilidade: Habilidade):
        if habilidade in self.habilidades:
            self.habilidades.remove(habilidade)
        else:
            raise KeyError("[ERRO] Habilidade não encontrada")
