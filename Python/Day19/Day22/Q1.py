d1 ={'Name':['Ted','Barney','Robin','Lily'],\
           'State':['MH','JK','HR','DL'],\
           'year':[2000,2005,2004,2001]}

from pandas import DataFrame as f


f1= f(d1)


print(f1)

d2 = {'City':['Nagpur','Jammu','Rohtak','New Delhi']}

f1['city']=['Nagpur','Jammu','Rohtak','New Delhi']
