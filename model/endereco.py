class Endereco:
    def __init__(self, cidade: str, bairro: str, numero: int, cep: int):
        self.__cidade = cidade
        self.__bairro = bairro
        self.__numero = numero
        self.__cep = cep

    @property
    def cidade(self):
        return self.__cidade

    @property
    def bairro(self):
        return self.__bairro

    @property
    def numero(self):
        return self.__numero

    @property
    def cep(self):
        return self.__cep

    @cidade.setter
    def cidade(self, cidade: str):
        if isinstance(cidade, str):
            self.__cidade = cidade.strip().title()
        else:
            raise ValueError("[ERRO] Cidade não alterada, valor inválido")

    @bairro.setter
    def bairro(self, bairro: str):
        if isinstance(bairro, str):
            self.__bairro = bairro.strip().title()
        else:
            raise ValueError("[ERRO] Bairro não alterado, valor inválido")

    @numero.setter
    def numero(self, numero: int):
        if isinstance(numero, int):
            self.__numero = numero
        else:
            raise ValueError("[ERRO] Número não alterado, valor inválido")

    @cep.setter
    def cep(self, cep):
        if isinstance(cep, int):
            self.__cep = cep
        else:
            raise ValueError("[ERRO] Cep não alterado, valor inválido")
