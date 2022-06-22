import logging
from src.extratores.jikan import JikanExtrator


class JikanIngestor:
    def __init__(self, carregador):
        self.carregador = carregador
        self.extrator = JikanExtrator()

    def ingerir_animes_populares(self):
        animes = self.extrator.obtem_animes_populares(50)
        self.carregador.salvar('populares', animes)

        return [(anime['id'], anime['nome']) for anime in animes]

    def ingerir_estatisticas(self, dados):
        estatisticas = []
        for id, name in dados:
            estatistica = self.extrator.obtem_estatisticas_anime(id, name)
            if not estatistica:
                continue
            estatisticas.append(estatistica)

        self.carregador.salvar('estatisticas', estatisticas)
