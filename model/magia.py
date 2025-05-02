class Magia():
    def __init__(self, nome: str, nivel: int, pagina: int):
        self.__nome = nome.strip().lower()
        self.__pagina = pagina
        self.__nivel = nivel


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
            if isinstance(pagina,int):
                 self.__pagina = pagina

    @property
    def nivel(self):
         return self.__nivel
    
    @nivel.setter
    def nivel(self, nivel):
         self.__nivel = nivel

    def __str__(self):
        return self.nome + ', pag: ' + str(self.pagina)