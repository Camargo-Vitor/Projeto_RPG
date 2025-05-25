class EspecieJahExisteException(Exception):
    def __init__(self, nome: str):
        super().__init__(f"[ERRO] A espécie {nome} já existe.")

class OrigemInvalidaException(Exception):
    def __init__(self):
        super().__init__("[ERRO] A origem selecionada não é compatível")
    