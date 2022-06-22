from pymongo import MongoClient, DESCENDING


class MongoConnector:
    @property
    def cliente(self):
        return MongoClient('mongodb://consumidor:consumidor@mongo:27017')

    def __obtem_dados(self, campo):
        colecao = self.cliente['animes']['estatisticas']

        return colecao.find({'title': {'$exists': True}}) \
                      .sort([('completed', DESCENDING)]) \
                      .distinct(campo)

    def __limita(self, dados, limite=20):
        return dados[:limite]

    def obtem_dados_grafico(self):
        nomes = self.__limita(self.__obtem_dados('title'))
        totais = self.__limita(self.__obtem_dados('completed'))

        return [(n, t) for n, t in zip(nomes, totais)]

    def obtem_dados_lista(self):
        return self.__limita(self.__obtem_dados('title'), 10)