from pymongo import MongoClient


class MongoCarregador:
    def __init__(self, banco, conexao):
        self.banco = banco
        self.cliente = MongoClient(conexao)

    def salvar(self, colecao, dados):
        banco_de_dados = self.cliente[self.banco]
        colecao = banco_de_dados[colecao]

        try:
            colecao.insert_many(dados)
        except TypeError:
            pass
