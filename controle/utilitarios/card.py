class Card:
    def __init__(self, id, descricao, valor, cor, subcards=None):
        self.id = id
        self.descricao = descricao
        self.valor = valor
        self.cor = cor
        self.subcards = subcards
