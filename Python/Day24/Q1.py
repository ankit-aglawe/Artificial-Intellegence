import pandas as pd
import numpy as np
from pandas import Series as s
from pandas import DataFrame as f

'''
a = np.random.randint(10,20,40).reshape(10,4)

f1 = f(a)

f1.columns=list('c1 c2 c3 c4'.split())

b=f1.sort_values(['c1','c3'],ascending=(True,False))

print(b)
'''

def data():
    d = {'Item':['a','b','c','e'],\
         'Place':['MH','KL','JK','TN'],\
         'Total sale':[100,200,500,300]}

    df = f(d)
    print(df)
    p = input('enter a item name :')

    for i,j in zip(df.index,df['Item']):
        if j==p:
            print(df.rank()['Item'][i])
            

    
data()
    
