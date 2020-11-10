#projeto árvores aleatórias

import pandas as pd
import numpy as np
import seaborn as sea
from sklearn.metrics import classification_report, confusion_matrix

data=pd.read_csv('loan_data.csv')

col=data.columns

data = data.select_dtypes(exclude=['object'])

data.drop(col[0],axis=1,inplace=True)
data.drop(col[11],axis=1,inplace=True)

from sklearn.model_selection import train_test_split as tt

print(col)


y=data[col[-1]]

x=data.drop(col[-1],axis=1)


xtre,xtes,ytre,ytes=tt(x,y,test_size=0.1)


from sklearn.ensemble import RandomForestClassifier

drtree=RandomForestClassifier(n_estimators=5000)

drtree.fit(xtre,ytre)

predr=drtree.predict(xtes)

print(classification_report(ytes, predr))

print(confusion_matrix(ytes, predr))


from sklearn.tree import DecisionTreeClassifier

dtree=DecisionTreeClassifier()

dtree.fit(xtre,ytre)

pred=dtree.predict(xtes)

print(classification_report(ytes, pred))

print(confusion_matrix(ytes, pred))


