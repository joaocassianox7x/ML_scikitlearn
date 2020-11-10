import pandas as pd
import numpy as np
import seaborn as sea
import matplotlib.pyplot as plt


data=pd.read_csv('kyphosis.csv')

x=data.drop('Kyphosis',axis=1)
y=data.Kyphosis





from sklearn.model_selection import train_test_split as tt

xtre,xtes,ytre,ytes=tt(x,y,test_size=0.3)




#arvore de decisão ========================================
from sklearn.tree import DecisionTreeClassifier

dtree=DecisionTreeClassifier()

dtree.fit(xtre,ytre)

from sklearn.metrics import classification_report, confusion_matrix

pred=dtree.predict(xtes)

print(classification_report(ytes, pred))

print(confusion_matrix(ytes, pred))

#arvore de decisão ========================================






#flores aleatori ============================================

from sklearn.ensemble import RandomForestClassifier

drtree=RandomForestClassifier(n_estimators=500)

drtree.fit(xtre,ytre)

predr=drtree.predict(xtes)

print(classification_report(ytes, predr))

print(confusion_matrix(ytes, predr))


#flores aleatori ============================================