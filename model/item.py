class Item():
    def __init__(
                 self,
                 nome: str,
                 valor: int,
                 raridade: str,
                 pagina: int):
        self.__nome = nome
        self.__valor = valor
        self.__raridade = raridade
        self.__pagina = pagina

    @property
    def nome(self):
        return self.__nome

    @property
    def valor(self):
        return self.__valor

    @property
    def raridade(self):
        return self.__raridade

    @property
    def pagina(self):
        return self.__pagina        

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise ValueError()

    @valor.setter
    def valor(self, valor):
        if isinstance(valor, int):    
            self.__valor = valor
        else:
            raise ValueError()

    @raridade.setter
    def raridade(self, raridade):
        if isinstance(raridade, str):
            self.__raridade = raridade
        else:
            raise ValueError()

    @pagina.setter
    def pagina(self, pagina: int):
        if isinstance(pagina, int): 
            self.__pagina = pagina
        else:
            raise ValueError()
