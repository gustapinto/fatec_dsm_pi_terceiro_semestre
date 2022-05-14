from requests import JSONDecodeError, get


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

            r = get(url, params=parametros)
            if not r.ok:
                break

            rjson = r.json()
            animes = rjson['data']

            ids.extend([self.__formata_anime(anime) for anime in animes])

        return ids[:qtd]

    def obtem_estatisticas_anime(self, id):
        url = f'{self.URL}/anime/{id}/statistics'

        r = get(url)
        if not r.ok:
            return None

        rjson = r.json()
        estatisticas = rjson['data']

        return estatisticas
