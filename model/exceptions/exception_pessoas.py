class JogadorJahExisteException(Exception):
    def __init__(self, nome: str):
        super().__init__(f"[ERRO] O jogador de {nome} já existe.")
class FichaJahExisteException(Exception):
    def __init__(self, nome: str):
        super().__init__(f"[ERRO] A ficha de {nome} já existe.")