import pandas as pd
import numpy as np

data=pd.read_csv('players_20.csv')
col=data.columns


lista=[]

nomes=data[col[2]]


for i in [0,1,3]:
    lista.append(col[i])

for i in range(26):
    lista.append(col[-i])

data.drop(lista,axis=1,inplace=True)
data.drop(['dob'],axis=1,inplace=True)

data = data.select_dtypes(exclude=['object'])

lista2=data.overall>=88

data=data[:sum(1*lista2)]
data=data.fillna(0)

nomes=nomes[:sum(1*lista2)]




from sklearn.decomposition import PCA
from sklearn import preprocessing as pre


valores=data.values
escal=pre.MinMaxScaler()
x_esc=escal.fit_transform(valores)
x_normalizado=pd.DataFrame(x_esc)

pca=PCA(n_components=2) 

reduced=pd.DataFrame(pca.fit_transform(x_normalizado))

reduced['x']=reduced[0]
reduced['y']=reduced[1]


from sklearn.cluster import KMeans as km

rede=km(n_clusters=4)

rede.fit(reduced)

lista=np.array([rede.labels_,nomes.to_numpy()])

reduced['cluster']=rede.labels_.tolist()
reduced['nomes']=nomes


import matplotlib.pyplot as plt

plt.scatter(reduced['x'],reduced['y'],c=reduced['cluster'],s=150)
[plt.text(reduced['x'][i],reduced['y'][i], nomes.to_numpy()[i]) for i in range(len(nomes))]