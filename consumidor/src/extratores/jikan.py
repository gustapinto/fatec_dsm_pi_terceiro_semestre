import logging

from requests import get


class JikanExtrator:
    def __init__(self):
        self.URL = 'https://api.jikan.moe/v4'

    def __formata_anime(self, anime):
        return {
            'id': anime['mal_id'],
            'nome': anime['title'],
            'posicao': anime['rank'],
            'popularidade': anime['popularity'],
        }

    def obtem_animes_populares(self, qtd):
        url = f'{self.URL}/top/anime'
        paginas = 1 if qtd < 25 else qtd // 25

        ids = []
        for pagina in range(1, paginas + 1):
            parametros = {'page': pagina, 'filter': 'bypopularity'}

            logging.info(f'Extraindo animes populares, página {pagina}')
            r = get(url, params=parametros)
            if not r.ok:
                logging.error(f'Falha ao extrair animes populares, página {pagina}, código {r.status_code}')
                break

            rjson = r.json()
            animes = rjson['data']

            ids.extend([self.__formata_anime(anime) for anime in animes])

        return ids[:qtd]

    def obtem_estatisticas_anime(self, id, name):
        url = f'{self.URL}/anime/{id}/statistics'

        logging.info(f'Extraindo estatisticas do anime {id}')
        r = get(url)
        if not r.ok:
            logging.error(f'Falha ao extrair estatísticas do anime {id}, código {r.status_code}')
            return None

        rjson = r.json()
        estatisticas = rjson['data']
        estatisticas['title'] = name

        return estatisticas
