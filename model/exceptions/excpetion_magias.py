class MagiaJahExisteException(Exception):
    def __init__(self, nome: str):
        super().__init__(f'[ERRO] A magia "{nome}" já existe.')
