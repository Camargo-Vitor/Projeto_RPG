class EspecieJahExisteException(Exception):
    def __init__(self):
        super().__init__("[ERRO] A espécie inserida já existe.")

class OrigemInvalidaException(Exception):
    def __init__(self):
        super().__init__("[ERRO] A origem selecionada não é compatível")
