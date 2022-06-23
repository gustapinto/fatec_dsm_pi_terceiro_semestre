from diagrams import Cluster, Diagram
from diagrams.programming.framework import Django
from diagrams.programming.language import Python
from diagrams.onprem.compute import Server
from diagrams.onprem.database import MongoDB


with Diagram('Arquitetura de módulos e serviços', show=False):
    consumidor = Python('Consumidor')
    site = Django('Anitrends')

    with Cluster('Fontes de dados'):
        api = Server('API')
        bd = MongoDB('Banco de dados')

        cluster = [api >> consumidor >> bd]

    cluster >> site
