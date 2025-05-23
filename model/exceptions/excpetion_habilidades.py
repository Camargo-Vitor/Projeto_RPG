class HabilidadeJahExiste(Exception):
    def __init__(self, nome: str):
        super().__init__(f'[ERRO] A habilidade "{nome}"já existe.')
