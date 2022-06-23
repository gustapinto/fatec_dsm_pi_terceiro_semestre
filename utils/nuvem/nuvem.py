
import pandas as pd
import requests
import time
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image

id =[16498,
1535,
5114,
30276,
11757,
31964,
22319,
20,
38000,
11061,
32281,
25777,
9253,
33486,
19815,
1735,
1575,
4224,
28851,
35760,
23273,
20507,
31240,
6547,
36456,
21,
40748,
22199,
38524,
23755,
10620,
31043,
21881,
9919,
24833,
32182,
30831,
20583,
37779,
269,
22535,
1,
199,
40028,
27899,
6702,
2904,
30,
28223,
18679]
title=[]
anicompleted = []
aux = 0

print(id[49])
while aux < 50:
    i = str(id[aux])

    anime = requests.get('https://api.jikan.moe/v4/anime/'+i)
    anime = anime.json()
    title.append(anime['data']['title'])
    completed = requests.get('https://api.jikan.moe/v4/anime/'+i+'/statistics')
    completed1 = completed.json()
    anicompleted.append(completed1['data']['completed'])
    time.sleep(2)
    aux = aux + 1
obj = {'title':title, 'completed':anicompleted}

df = pd.DataFrame(data=obj)

qtd=[]
nome = []
lista =[]
qtd = obj.get('completed')
nome = obj.get('title')
aux = 0
while aux < 25:
    lista.append(nome[aux] * qtd[aux])
    aux = aux + 1

print(lista)     

mask = np.array(Image.open(r'C:\Users\Guilherme\Downloads\anime.jpg'))

wc = WordCloud(stopwords = STOPWORDS,
               mask = mask, background_color = "black",
               max_words = 2000, max_font_size = 500,
               random_state = 42, width = mask.shape[1],
               height = mask.shape[0])

lista = str(lista)

wc.generate(lista)
plt.imshow(wc, interpolation="None")
plt.axis('off')
plt.savefig('foo.png', bbox_inches='tight', dpi=1200)
plt.show()