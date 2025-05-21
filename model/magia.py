class Magia():
    def __init__(self,
                 nome: str,
                 nivel: int,
                 pagina: int):
        self.__nome = nome
        self.__pagina = pagina
        self.__nivel = nivel

    @property
    def nome(self):
        return self.__nome

    @property
    def pagina(self):
        return self.__pagina

    @property
    def nivel(self):
         return self.__nivel

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise ValueError("[ERRO] Nome não alterado, valor inválido")
    
    @pagina.setter
    def pagina(self, pagina: int):
        if isinstance(pagina,int):
            self.__pagina = pagina
        else:
            raise ValueError("[ERRO] Página não alterada, valor inválido")

    @nivel.setter
    def nivel(self, nivel: int):
        if isinstance(nivel, int):
            self.__nivel = nivel
        else:
            raise ValueError("[ERRO] Nível não alterado, valor inválido")
