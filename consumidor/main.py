from sys import argv

from time import sleep

from src.log import configura_logger
from src.carregadores.mongodb import MongoCarregador
from src.ingestores.jikan import JikanIngestor


def main():
    configura_logger()

    try:
        conexao = argv[1]
    except IndexError:
        print('Usar python main.py <connection_string>')
        return

    carregador = MongoCarregador('animes', conexao)
    ingestor = JikanIngestor(carregador)

    while True:
        ids = ingestor.ingerir_animes_populares()
        ingestor.ingerir_estatisticas(ids)
        sleep(300)


if __name__ == '__main__':
    main()
