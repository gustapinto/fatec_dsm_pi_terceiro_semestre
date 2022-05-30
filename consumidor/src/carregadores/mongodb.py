import logging
from pymongo import MongoClient


class MongoCarregador:
    def __init__(self, banco, conexao):
        self.banco = banco
        self.cliente = MongoClient(conexao)

    def salvar(self, colecao, dados):
        banco_de_dados = self.cliente[self.banco]
        colecao = banco_de_dados[colecao]

        try:
            logging.info(f'Carregando {len(dados)} registros no banco de dados')
            colecao.insert_many(dados)
        except Exception as e:
            logging.error(f'Falha ao carregar {len(dados)} registros no banco de dados, erro {e}')
            return

        logging.info(f'Carregamento concluído com sucesso')
