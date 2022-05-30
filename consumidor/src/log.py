from sys import stdout
from logging import INFO, basicConfig, StreamHandler, FileHandler


class LoggingUtilitario:
    @staticmethod
    def configura():
        # Configura o logger global
        basicConfig(level=INFO, format='%(asctime)s %(levelname)-8s %(message)s',
                    handlers=[StreamHandler(stdout), FileHandler('consumidor.log')])
