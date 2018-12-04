import numpy as np
import pandas as pd


dt1 = np.dtype({'names':['ename','eno','edesig','esalary','ephno'],'formats':['S20','i8','S20','f8','S20']})

f1 = np.loadtxt('emp.csv', delimiter=',', dtype=dt1, skiprows=1)


r1 = np.rec.array(f1)
print(r1.ename)


#------------------------------------------


print(r1.esalary.sum())

#------------------------------------------

a3 = r1.edesig=='officer'

a4=np.where(a3,r1.edesig,0)
a4=np.where(a3,r1.ename, 0)

#------------------------------------------

b1=np.where(b1,r1.edesig,0)

ind =[]
for i in range(10):
    if b1[i]=='scientist':
        ind.append(i)

for i in ind:
    print(f1[i])

#-------------------------------------------
c1 = r1.edesig=='engineer'

c2 =np.where(c1,r1.esalary,0).sum()


#-------------------------------------------
d1 = r1.esalary
d1.sort()
e1=f1.copy()
e1.sort(order='edesig')

#-------------------------------------------
 e1=f1.copy()
 e1.sort(order='edesig')
 e1.sort(order='esalary')


#-----------------------------------------

r1.esalary.min()

#-----------------------------------------
k1=f1[r1.edesig=='scientist']

x = k1['esalary'].min()

z =k1[k1['esalary']==x]

 

