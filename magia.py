class Magia():
    def __init__(self, nome: str, pagina: int):
        self.__nome = nome
        self.__pagina = pagina

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
            if isinstance(pagina,int):
                 self.__pagina = pagina
