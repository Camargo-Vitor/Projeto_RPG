class Habilidade():
    def __init__(self, nome: str, nivel: int, pagina: int, origem: str):
        self.__nome = nome.strip().lower()
        self.__nivel = nivel
        self.__pagina = pagina
        self.__origem = origem.strip().lower()

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome.strip().lower()

    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self, nivel: int):
        self.__nivel = nivel

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
    def origem(self, origem: str):
        if origem.strip().lower() in ('especie', 'subespecie', 'classe', 'subclasse'):
            self.__origem = origem.strip().lower()

    def __str__(self):
        return self.nome + ', pag: ' + str(self.pagina)