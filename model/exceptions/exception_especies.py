class EspecieJahExisteException(Exception):
    def __init__(self, nome: str):
        super().__init__(f"[ERRO] A espécie {nome} já existe.")


