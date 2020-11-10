import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sea

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

trei=pd.read_csv('titanic_train.csv')

# sea.pairplot(trei)
# plt.tight_layout()

#sea.heatmap(trei.isnull(),cbar=False)

#sea.countplot(x='Survived',data=trei,hue='Pclass')

#sea.distplot(trei['Age'])

def inp_idade(cols):
    idade=cols[0]
    classe=cols[1]
    
    if pd.isnull(idade):
        if classe==1:
            return 37
        elif classe==2:
            return 29
        else:
            return 24
    else:
        return idade
    
trei["Age"]=trei[['Age','Pclass']].apply(inp_idade,axis=1)

trei.drop('Cabin',inplace=True,axis=1)

#sea.heatmap(trei.isnull())

trei.dropna(inplace=True)

sex=pd.get_dummies(trei['Sex'],drop_first=True)
embark=pd.get_dummies(trei['Embarked'],drop_first=True)

trei.drop(['Sex','PassengerId','Name','Ticket','Embarked'],axis=1,inplace=True)

trei=pd.concat([trei,sex,embark],axis=1) #concatenando a galera

xtre,xtest,ytre,ytest=train_test_split(trei.drop(['Survived'],axis=1),trei['Survived'],test_size=0.4)

modelo=LogisticRegression()

modelo.max_iter=5000

modelo.fit(xtre,ytre)

predict=modelo.predict(xtest)

from sklearn.metrics import classification_report as cr

print(cr(ytest,predict))

from sklearn.metrics import confusion_matrix as cm

print(cm(ytest,predict))

