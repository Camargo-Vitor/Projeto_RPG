class JogadorJahExisteException(Exception):
    def __init__(self, nome: str):
        super().__init__(f"[ERRO] O jogador {nome} já existe.")
