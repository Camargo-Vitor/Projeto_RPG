class ItemInexistenteException(Exception):
    def __init__(self):
        super().__init__("[ERRO] O Item não existe")

class ItemJahExisteException(Exception):
    def __init__(self, nome: str):
        super().__init__(f'[ERRO] O item "{nome}" já existe')