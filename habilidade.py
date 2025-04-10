class Habilidade():
    def __init__(self, nome: str, pagina: int, origem: str):
        self.__nome = nome
        self.__pagina = pagina
        self.__origem = origem


    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome


    @property
    def pagina(self):
        return self.__pagina
    
    @pagina.setter
    def pagina(self, pagina):
        if isinstance(pagina, int):
            self.__pagina = pagina
    

    @property
    def origem(self):
        return self.__origem
    
    @origem.setter
    def origem(self, origem):
        if isinstance(origem, str):
            self.__origem = origem

    #essa aqui que vai fazer o add habilidades com lista de tupla