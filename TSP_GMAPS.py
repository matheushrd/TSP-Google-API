#!/usr/bin/env python
# coding: utf-8

# In[2]:


import gmaps
import requests
import tsp
import googlemaps
import pandas as pd


df = pd.read_csv('C:/Users/Casa/Desktop/df.csv', delimiter=';')
print(df)
gmaps.configure(api_key='KEY')
gmaps1 = googlemaps.Client(key='KEY')

#nomes = ['Ponto de partidad/chegada', 'Ibirapuera', 'Museu da Arte', 'Pinacoteca', 'Mercado Central', 'Batman', 'Teatro Municipal', 'butata' ]
#origem = ['R+Maj+Paladino+128+Galpão+12+São+Paulo+SP', 'Av+Pedro Álvares+Cabral+Vila+Mariana+São+Paulo+SP', 'Av. Paulista, 1578 - Bela Vista, São Paulo - SP', 'Praça da Luz, 2 - Luz, São Paulo - SP','R. Gonçalo Afonso - Vila Madalena, São Paulo - SP', 'Praça Ramos De Azevedo, s/n - República, São Paulo - SP', 'Av. Vital Brasil, 1500 - Butantã, São Paulo - SP']
#destino= ['R. Maj. Paladino 128 Galpão 12 São Paulo SP', 'Av. Pedro Álvares Cabral - Vila Mariana, São Paulo - SP', 'Av. Paulista, 1578 - Bela Vista, São Paulo - SP', 'Praça da Luz, 2 - Luz, São Paulo - SP','R. Gonçalo Afonso - Vila Madalena, São Paulo - SP', 'Praça Ramos De Azevedo, s/n - República, São Paulo - SP', 'Av. Vital Brasil, 1500 - Butantã, São Paulo - SP']
nomes = []
origem = []
destino =[]

for i in range(len(df)):
    nomes.append(df['Nomes'][i])
for i in range(len(df)):
    origem.append(df['Endereço'][i])
    
for i in range(len(df)):
    destino.append(df['Endereço'][i])

consulta = [[] for i in range(len(origem))]
def matriz_dist(origem, destino):
    consulta = [[] for i in destino]
    for o in range(len(origem)):
        for d in range(len(destino)): 
            consulta[o].append(gmaps1.distance_matrix(origem[o], destino[d]))
    return consulta


def recebe_latlong(orgiem):
    GOOGLE_GEOCODING_API_URL = []
    for i in range(len(origem)):
        GOOGLE_GEOCODING_API_URL.append('https://maps.googleapis.com/maps/api/geocode/json?address='+origem[i]+'&key=AIzaSyDNy8UO7dIJDnPG49eEUV-vHIyv_8tHLgM')
    req = []
    for i in range(len(origem)):
        req.append(requests.get(GOOGLE_GEOCODING_API_URL[i]))

    res = []
    for i in range(len(origem)):
        res.append(req[i].json())

    result=[]
    for i in range(len(origem)):
        result.append(res[i]['results'][0])

    geodata = [[] for i in range(len(origem))]
    for i in range(len(origem)):
        geodata[i].append(result[i]['geometry']['location']['lat'])
        geodata[i].append(result[i]['geometry']['location']['lng'])
    return geodata

consulta = matriz_dist(origem, destino)

dist = [[] for i in range(len(origem))]
for i in range(len(origem)):
    for j in range(len(origem)):
        dist[i].append((consulta[i][j]['rows'][0]['elements'][0]['distance']['value']))


r = range(len(origem))
# Dictionary of distance
dist = {(i, j): dist[i][j] for i in r for j in r}

tsp1 = tsp.tsp(r, dist)[1]
print(tsp1)


geodata = recebe_latlong(origem)
fig = gmaps.figure()
layer = []
for i in range(len(origem)):
    if i == len(origem)-1:
        layer.append(gmaps.directions.Directions(geodata[tsp1[i]], geodata[tsp1[0]]))
        print(nomes[tsp1[i]]+'       '+nomes[tsp1[0]])
        continue
    print(i)
    layer.append(gmaps.directions.Directions(geodata[tsp1[i]], geodata[tsp1[i+1]]))
    print(nomes[tsp1[i]]+'       '+nomes[tsp1[i+1]])
for i in range(len(origem)):
    fig.add_layer(layer[i])
fig.add_layer(gmaps.directions.Directions(geodata[tsp1[0]], geodata[tsp1[1]]))






