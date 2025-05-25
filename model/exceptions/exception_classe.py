class ClasseJahExisteException(Exception):
    def __init__(self, nome: str):
        super().__init__(f"[ERRO] A classe {nome} já existe.")
