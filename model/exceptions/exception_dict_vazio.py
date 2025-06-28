class DictVazioException(Exception):
    def __init__(self):
        super().__init__(f"[ERRO] Não há nenhum objeto na lista.")
