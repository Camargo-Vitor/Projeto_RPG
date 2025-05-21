class Habilidade():
    def __init__(self,
                 nome: str,
                 nivel: int,
                 pagina: int,
                 origem: str):
        self.__nome = nome
        self.__nivel = nivel
        self.__pagina = pagina
        self.__origem = origem

    @property
    def nome(self):
        return self.__nome

    @property
    def nivel(self):
        return self.__nivel

    @property
    def pagina(self):
        return self.__pagina

    @property
    def origem(self):
        return self.__origem

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise ValueError("[ERRO] Nome não alterado, valor inválido")

    @nivel.setter
    def nivel(self, nivel: int):
        if isinstance(nivel, int):
            self.__nivel = nivel
        else:
            raise ValueError("[ERRO] Nível não alterado, valor inválido")

    @pagina.setter
    def pagina(self, pagina):
        if isinstance(pagina, int):
            self.__pagina = pagina
        else:
            raise ValueError("[ERRO] Página não alterada, valor inválido")

    @origem.setter
    def origem(self, origem: str):
        if origem.strip().lower() in ('especie', 'subespecie', 'classe', 'subclasse'):
            self.__origem = origem
        else:
            raise ValueError("[ERRO] Origem não alterada, valor inválido")
