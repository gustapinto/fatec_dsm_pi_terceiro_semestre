from sqlite3 import Time
from turtle import pd
import requests


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
    Time.sleep(0.5)
    aux = aux + 1

obj = {'id':id, 'title':title, 'completed':anicompleted}

df = pd.DataFrame(data=obj)
