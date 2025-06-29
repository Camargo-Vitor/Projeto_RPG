class FichaJahExisteException(Exception):
    def __init__(self, nome: str):
        super().__init__(f"[ERRO] A ficha {nome} já existe.")