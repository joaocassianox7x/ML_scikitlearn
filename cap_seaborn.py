import pandas as pd
import numpy as np
import seaborn as sea

#PRIMEIRA AULA
# =============================================================================
# 
# tips=sea.load_dataset("tips")
# 
# #sea.distplot(tips['total_bill'],kde=True,bins=30) #gaussiana com histograma
# #sea.jointplot(x="total_bill", y="tip",data=tips,kind="kde") #plota um pelo outro
# #sea.pairplot(tips,hue="sex") #todas possiveis correlações
# sea.rugplot(tips['total_bill'])
# 
# 
# 
# #alea=np.random.normal(size=100000) #matriz normal
# #sea.distplot(alea,kde=True,rug=True) #plot com KDE para a matriz acima
# 
# 
# =============================================================================


#SEGUNDA AULA
# =============================================================================
# 
# tips=sea.load_dataset("tips")
# 
# #sea.barplot(x='sex',y='total_bill',data=tips,estimator=np.std) #plot + std
# 
# #sea.boxplot(x='day',y='total_bill',data=tips,hue='sex')
# 
# #sea.boxplot(x='tip',y='total_bill',data=tips,hue='sex')
# 
# #sea.violinplot(x='day',y='tip',data=tips,hue='sex',split=True) #plot em violino
# 
# #sea.stripplot(x='day',y='tip',data=tips,jitter=True,hue='sex',split=True) #plot por ponto em linha
# 
# sea.swarmplot(x='day',y='tip',data=tips) #plot em linha, sem sobreposicao
# 
# sea.factorplot(x='sex',y='total_bill',data=tips,kind='bar')
# =============================================================================

#TERCEIRA AULA
# =============================================================================
# fly=sea.load_dataset('flights')
# tips=sea.load_dataset('tips')
# 
# fly=pd.DataFrame(fly)
# tips=pd.DataFrame(tips)
# 
# cor=tips.corr() #calcula todas correlações no dataframe
# 
# #sea.heatmap(cor)
# 
# flyp=fly.pivot_table(values='passengers', index='month',columns='year') #cria uma matriz
# 
# 
# sea.heatmap(flyp)
# =============================================================================
# =============================================================================
# #QUARTA AULA
# tips=sea.load_dataset('tips')
# sea.lmplot(x='total_bill',y='tip',data=tips,hue='sex',palette='coolwarm',col='sex',row='time') #segrega entre sexo e horário
# 
# =============================================================================
# =============================================================================
# 
# #EXERCICIOS
# 
# sea.set_style('whitegrid')
# titanic=sea.load_dataset('titanic')
# 
# #sea.jointplot(x='fare', y='age', data=titanic)
# 
# #sea.boxenplot(x='class',y='age',data=titanic,hue='sex')
# 
# #sea.stripplot(x='class',y='age',data=titanic,hue='sex',split=True,color='k')
# #sea.violinplot(x='class',y='age',data=titanic,hue='sex',split=False)
# 
# 
# =============================================================================
