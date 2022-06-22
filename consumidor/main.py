from sys import argv

from time import sleep

from src.log import LoggingUtilitario
from src.carregadores.mongodb import MongoCarregador
from src.ingestores.jikan import JikanIngestor


def main():
    LoggingUtilitario.configura()

    try:
        conexao = argv[1]
    except IndexError:
        print('Executar consumidor como:')
        print('python main.py "mongodb://<usuário>:<senha>@<host>:<porta>"')
        return

    carregador = MongoCarregador('animes', conexao)
    ingestor = JikanIngestor(carregador)

    while True:
        dados = ingestor.ingerir_animes_populares()
        ingestor.ingerir_estatisticas(dados)
        sleep(300)


if __name__ == '__main__':
    main()
