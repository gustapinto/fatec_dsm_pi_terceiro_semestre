from src.extratores.jikan import JikanExtrator


def main():
    extrator = JikanExtrator()

    for anime in extrator.obtem_animes_populares(50):
        estatisticas = extrator.obtem_estatisticas_anime(anime['id'])
        print(estatisticas)

if __name__ == '__main__':
    main()
