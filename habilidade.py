class Habilidade():
    def __init__(self, nome: str, pagina: int, origem: str):
        self.__nome = nome.strip().lower()
        self.__pagina = pagina
        self.__origem = origem


    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome.strip().lower()


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
        if isinstance(origem, str).strip.lower:
            self.__origem = origem

    def __str__(self):
        return f'><' * 8 + 'Habilidade nova criada' + '><' * 8 + \
        f'\nNome da Habilidade: {self.__nome}\
        \nOrigem: {self.__origem}\
        \nPágina: {self.__pagina}'