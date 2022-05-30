from sys import stdout
import logging


def configura_logger():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)-8s %(message)s',
        handlers=[
            logging.StreamHandler(stdout),
            logging.FileHandler('consumidor.log'),
        ],
    )
