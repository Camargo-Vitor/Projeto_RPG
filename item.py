class Item():
    def __init__(self, nome: str, valor: int, raridade: str, pagina: int):
        self.__nome = nome
        self.__valor = valor
        self.__raridade = raridade
        self.__pagina = pagina


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
    

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        if isinstance(valor, int):    
            self.__valor = valor


    @property
    def raridade(self):
        return self.__raridade

    @raridade.setter
    def raridade(self, raridade):
        if isinstance(raridade, str):
            self.__raridade = raridade

    @property
    def pagina(self):
        return self.__pagina        

    @nome.setter
    def pagina(self, pagina):
        if isinstance(pagina, int):
            self.__pagina = pagina

    
   


    
      