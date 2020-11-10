import numpy as np
import pandas as pd #usual

# =============================================================================
# Primeira aula
# labels=['a','b','c']
# lista=[10,20,30]
# arr=np.array(lista)
# d={'a':10,'b':20,'c':30}
# 
# labels_series=pd.Series(lista,labels)
# 
# 
# =============================================================================


# =============================================================================
# Segunda aula
# np.random.seed(101)
# 
# df=pd.DataFrame(np.random.randn(5,4),index="A B C D E".split(),columns="W X Y Z".split())
# 
# bol=df>0.0
# 
# df=df[bol]
# 
# df=pd.DataFrame(np.random.randn(5,4),index="A B C D E".split(),columns="W X Y Z".split())
# 
# estados="MG SP RJ AM SC".split()
# df["Estados"]=estados
# df.set_index("Estados",inplace=True)
# 
# =============================================================================

# =============================================================================
# 
# Terceira aula
# outside="G1 G1 G1 G2 G2 G2".split()
# inside=[1,2,3,1,2,3]
# hier_index=list(zip(outside,inside))
# hier_index=pd.MultiIndex.from_tuples(hier_index)
# 
# df=pd.DataFrame(np.random.randn(6,2),index=hier_index,columns="A B".split())
# 
# df.index.names=["Grupo","Numero"]
# 
# df.xs('G1')
# 
# 
# print(df)
# 
# 
# =============================================================================
# =============================================================================
# Quarta Aula
# 
# d={'A':[1,2,np.nan],'B':[1,np.nan,np.nan],'C':[np.nan,2,4]}
# 
# 
# df=pd.DataFrame(d)
# 
# #df.fillna(0,inplace=True) #substitui nan por 0
# 
# df[:]=df[:].fillna(df[:].mean()) #substitui nan pela media da coluna
# 
# 
# =============================================================================
# =============================================================================
# Quinta Aula, GroupBy
# data={"Empresa":["GG","GG","MF","MF","FA","FA"],"Nome":["Sam","Charlie","Amy","Vanessa","Carl","Sarah"],"Venda":[200,120,340,124,243,350]}
# 
# df=pd.DataFrame(data)
# 
# grupo=df.groupby("Empresa")
# 
# soma=grupo.describe()
# print(df)
# =============================================================================

#value_counts comando retorna quantas vezes cada valor apareceu no modo valor numero de vezes
