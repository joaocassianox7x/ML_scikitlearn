import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt


from sklearn.model_selection import train_test_split as tra_spl
from sklearn.linear_model import LogisticRegression


from sklearn.metrics import classification_report as cr


from sklearn.metrics import confusion_matrix as cm


data=pd.read_csv('advertising.csv')

#sea.distplot(data.Age,bins=30)
# =============================================================================
# 
# sea.jointplot(x='Age',y='Area Income',data=data,kind='kde')
# 
# 
# sea.jointplot(x='Age',y='Daily Time Spent on Site',data=data,kind='kde')
# 
# 
# =============================================================================

#sea.pairplot(data,hue='Clicked on Ad')

#sea.heatmap(data.isnull())
#plt.tight_layout()

col=data.columns

data.drop(col[4],axis=1,inplace=True)
data.drop(col[5],axis=1,inplace=True)
data.drop(col[7],axis=1,inplace=True)

def func(i):
    a=i.split()[1].split(':')
    for j in range(len(a)):
        a[j]=float(a[j])
    a[0]=a[0]*60*60
    a[1]=a[1]*60
    return(sum(a))

data[col[8]]=data[col[8]].apply(func)    

xtre,xtes,ytre,ytes=tra_spl(data.drop(col[-1],axis=1),data[col[-1]],test_size=0.5)

modelo=LogisticRegression()

modelo.fit(xtre,ytre)

pred=modelo.predict(xtes)

print(cr(ytes,pred))

print(cm(ytes,pred))


