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

#--------------------------------------------------


import numpy as np 
import pandas as pd 
from pandas import DataFrame as f 
global d

d = {'Item':['a','b','c','e'],\
    'Place':['MH','KL','JK','TN'],\
    'Total sale':[100,200,500,300]}

global df
df = f(d)

def ItemWise():

    print(df)
    p = input('enter a item name :')

    for i,j in zip(df.index,df['Item']):
        if j==p:
            print('Place Wise rank of ',p,' is ', df.rank()['Place'][i])

def placeWise():
    print(df)
    q= input('enter a place name: ') 
    
    for i,j in zip(df.index,df['Place']):
        if j==q:
            print('Place Wise rank of ',p,' is ', df.rank()['Item'][i]) 
            
while True:
    print('=================================')
    print('Choose option')
    print('1. Add data')
    print('2. Show ItemWise rank')
    print('3. Show place wise rank')
    print('4. Exit')

    ch = input('choose a number : ')

    if ch ==1:
        itm = input('Enter an Item name: ')
        plc = input('Enter a place name: ')
        sl = int(input('Enter total sale value: '))

        l1=[itm,plc,sl]
        arr1= np.array(l1).reshape(1,3)
        df1=f(arr1,columns=['Item','Place','Total sale'],index=[len(df)])
        df = df.append(df1)
        print(df)
    if ch==2:
        ItemWise()
    if ch==3:
        placeWise()
    if ch==4:
        break
    

    
