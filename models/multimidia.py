class Multimidia:
    tipo: str
    src: str

    def __init__(self, tipo, src):
        self.tipo = tipo
        self.src = src

    def reprJSON(self):
        return dict(tipo=self.tipo, src=self.src)
