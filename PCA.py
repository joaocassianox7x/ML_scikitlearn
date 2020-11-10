import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sea

from sklearn.datasets import load_breast_cancer

cancer=load_breast_cancer()

df=pd.DataFrame(cancer['data'],columns=cancer['feature_names'])

from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()

scaler.fit(df)

data_norm=scaler.transform(df)


from sklearn.decomposition import PCA

pca=PCA(n_components=2)

pca.fit(data_norm)

x_pca=pca.transform(data_norm)
plt.scatter(x_pca[:,0],x_pca[:,1])

plt.figure()
plt.scatter(x_pca[:,0],x_pca[:,1],c=cancer['target'])

datanew=pd.DataFrame(pca.components_,columns=cancer['feature_names'])

plt.figure()

sea.heatmap(datanew)