
# coding: utf-8

# In[1]:


import googlemaps
import tsp
import pandas as pd


# In[12]:


gmaps = googlemaps.Client(key='KEY')
nomes = ['RH Curitiba', 'A priori ', 'RH NOSSA', 'Sé Assessoria', 'Agilidade Gestão de Pessoas']
#origem = ['R. Maj. Paladino 128 Galpão 12 São Paulo SP', 'Av. Pedro Álvares Cabral - Vila Mariana, São Paulo - SP', 'Av. Paulista, 1578 - Bela Vista, São Paulo - SP', 'Praça da Luz, 2 - Luz, São Paulo - SP', 'Praça da Luz, 2 - Luz, São Paulo - SP', 'R. Gonçalo Afonso - Vila Madalena, São Paulo - SP', 'Praça Ramos De Azevedo, s/n - República, São Paulo - SP', 'Av. Vital Brasil, 1500 - Butantã, São Paulo - SP']
destino= [1231 - Cajuru, Curitiba - PR','R. Monsenhor Célso, 211 - Centro, Curitiba - PR, 80010-920', 'Rua Maria Ficinsksa, 260 - Tarumã, Curitiba - PR, 82530-420', 'R. Lamenha Lins, 2232 - Rebouças, Curitiba - PR, 80220-080', 'R. Lourenço Pinto, 410 - Matriz, Curitiba - PR, 80010-160','R. José de Alencar, 590 - Alto da XV, Curitiba - PR, 80045-115']
consulta = [[] for i in destino]
for o in range(len(destino)):
    for d in range(len(destino)): 
        consulta[o].append(gmaps.distance_matrix(destino[o], destino[d]))


# In[13]:


d_matrix = [[]for i in destino]

for i in range(len(destino)):
    for j in range(len(destino)):
        d_matrix[i].append(consulta[i][j]['rows'][0]['elements'][0]['distance']['value'])
        


# In[14]:


r= range(len(d_matrix))
d=  {(i, j): d_matrix[i][j] for i in r for j in r}
print(r)
print(tsp.tsp(r, d))


# In[15]:


TSP = tsp.tsp(r, d)


# In[17]:


finalnomes = []
for i in range(len(destino)):
    finalnomes.append(nomes[TSP[1][i]])


# In[18]:


finalendereco = []
for i in range(len(destino)):
    finalendereco.append(destino[TSP[1][i]])


# In[19]:


dic = {'nomes': finalnomes, 'endereco':finalendereco}


# In[20]:


df = pd.DataFrame(data = dic)


# In[21]:


print(df)

