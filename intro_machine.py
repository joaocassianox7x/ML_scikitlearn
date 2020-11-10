import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sea
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# =============================================================================
# 
# pri=pd.read_csv('USA_Housing.csv') #todas relacoes
# 
# #sea.pairplot(pri) #todas possiveis correlacoes
# #sea.heatmap(pri.corr()) #encontrar as correlações
# 
# x=pri[pri.columns[:-3]]
# y=pri['Price']
# 
# xtrei,xtest,ytrei,ytest=train_test_split(x,y,test_size=0.9, random_state=101) #divide entre
# #treino e teste, usei 30% dos dados para o teste
# 
# lm=LinearRegression()
# 
# lm.fit(xtrei,ytrei)
# 
# data=pd.DataFrame(lm.coef_,x.columns,columns=['Coefs'])
# 
# predict=lm.predict(xtest)
# #plt.scatter(ytest,predict)
# sea.distplot(ytest-predict)
# =============================================================================
# =============================================================================
# 
# cli=pd.read_csv('Ecommerce Customers')
# 
# cli=cli[cli.columns[3:]]
# #sea.heatmap(cli.corr())
# plt.tight_layout()
# #sea.pairplot(cli)
# #sea.lmplot(x=cli.columns[-2],y=cli.columns[-1],data=cli)
# 
# y=cli['Yearly Amount Spent']
# x=cli[cli.columns[:-1]]
# 
# xtrei,xtest,ytrei,ytest=train_test_split(x,y,test_size=0.3)
# 
# 
# lm=LinearRegression()
# lm.fit(xtrei,ytrei)
# 
# predict=lm.predict(xtrei)
# plt.scatter(predict,ytrei)
# 
# 
# coef=pd.DataFrame(lm.coef_,x.columns,columns=["Coefs"])
# =============================================================================

