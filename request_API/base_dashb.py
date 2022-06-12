import pandas as pd
import requests
import time


#Carrega o top 10 de todos os tempos
topanime = requests.get("https://api.jikan.moe/v4/top/anime")
topanime = topanime.json()
topanime = topanime['data']
aux = 0
while aux < 10:
    anime1 = topanime[aux]
    print(anime1['title'])
    print(anime1['rank'])
    aux = aux + 1

#anime por estacao
animespring = requests.get("https://api.jikan.moe/v4/seasons/2022/winter")
animespring = animespring.json()
animespring = animespring['data']
aux = 0
while aux < 25:
    anime1 = animespring[aux]
    print(anime1['title'])
    aux = aux + 1


#Cria a base para os animes mais vistos da primavera de 2022    
df = pd.DataFrame(columns=['id', 'title', 'completed'])

animespring = requests.get("https://api.jikan.moe/v4/seasons/2022/spring")
animespring = animespring.json()
animespring = animespring['data']

id =[]
title=[]
anicompleted = []
aux = 0
while aux < 25:
    anime1 = animespring[aux]
    id.append(str(anime1['mal_id']))  
    title.append(anime1['title'])
    i = str(anime1['mal_id'])
    completed = requests.get('https://api.jikan.moe/v4/anime/'+i+'/statistics')
    completed1 = completed.json()
    anicompleted.append(completed1['data']['completed'])
    time.sleep(0.5)
    aux = aux + 1

obj = {'id':id, 'title':title, 'completed':anicompleted}

df = pd.DataFrame(data=obj)
