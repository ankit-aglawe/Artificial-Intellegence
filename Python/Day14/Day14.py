#---------QUE 1-------------------------------------

import re

fd = open('emp.csv', 'r').read().split('\n')
f1=open('sci.csv','w')

for data in fd:
    mo = re.search('scientist', data)
    if mo:
        f1.write(data+'\n')
        print(data)
f1.close()
        



#-----------QUE 2--------------------------------------------

import re

fd = open('emp.csv', 'r').read().split('\n')
f2=open('ini1.csv','w')
for data in fd:
    a= data.split('.',1)[0]

    if len(a)==1:
        print(a)
        f2.write(data+'\n')
f2.close()
        

#-----------QUE 2--------------------------------------------

import re

fd = open('emp.csv', 'r').read().split('\n')
f2=open('ini1.csv','w')

for data in fd:
    mo = re.match('^[A-Z]\\.',data)
    if mo:
        f2.write(data+'\n')
f2.close()

#-----------QUE 3---------------------------------------------



import re

fd = open('emp.csv', 'r').read().split('\n')
f3=open('ini2.csv','w')

for data in fd:
    mo = re.match('.*[A-Z]\\.',data)
    if mo:
        f3.write(data+'\n')
f3.close()


#---------------QUE 4-----------------------------------------

import re

fd = open('emp.csv', 'r').read().split('\n')
f4=open('empphno.csv','w')

for data in fd:
    #mo = re.match('[^,]+', data)
    mo = re.split((','), data)
    if mo:
        name=mo[0]
        no=mo[-1]
        no=re.sub('[^0-9]+','',no)
        f4.write('%s,%s\n' %(name,no))
f4.close()


#------------QUE 5-------------------------------------------

import re

fd = open('emp.csv', 'r').read().split('\n')
f5=open('empphno.csv','w')

for data in fd:
    mo=re.split(',', data)
    m01= re.match('[2-9][0-9][0-9]',mo[1])
    if m01:
        f5.write(data+'\n')
f5.close()

