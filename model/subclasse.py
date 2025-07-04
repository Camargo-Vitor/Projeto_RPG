from model.habilidade import Habilidade


class Subclasse():
    def __init__(self,
                 nome_sub: str):
        self.__nome = nome_sub
        self.__hab_espeficicas: list[Habilidade] = []

    @property
    def nome(self):
        return self.__nome

    @property
    def hab_especificas(self):
        return self.__hab_espeficicas

    @nome.setter
    def nome(self, nome: str, nome_sub: str):
        if isinstance(nome_sub, str):
            self.__nome = nome + ' ' + nome_sub
        else:
            raise ValueError("[ERRO] Nome não alterado, valor inválido \
                              (verifique coleta de nome + sub_nome)")

    def add_hab(self, habilidade: Habilidade):
        if isinstance(habilidade, Habilidade) and habilidade.origem == 'subclasse':
            self.__hab_espeficicas.append(habilidade)
        else:
            raise ValueError("[ERRO] Habilidade não adicionada, valor inválido")

    def rm_hab(self, habilidade: Habilidade):
        for habilidade_lista in self.__hab_espeficicas:
            if habilidade_lista.nome == habilidade.nome:
                self.__hab_espeficicas.remove(habilidade_lista)
                return True
        raise KeyError("[ERRO] Habilidade não encontrada")
