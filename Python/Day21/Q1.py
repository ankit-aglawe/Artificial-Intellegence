import numpy as np
import pandas as pd

dt1 = np.dtype({'names':['ename','eno','edesig','esalary','ephno'],'formats':['S20','i8','S20','f8','S20']})

f1 = np.loadtxt('emp.csv', delimiter=',', dtype=dt1, skiprows=1)
g1 = np.array(f1)
#print(f1)

def action(num):
    global g1
    f1 = np.loadtxt('emp.csv', delimiter=',', dtype=dt1, skiprows=1)
    
    if num==1 :
        print(g1)
    elif num==2:
        f1 = np.loadtxt('emp.csv', delimiter=',', dtype=dt1, skiprows=1)
        name = str(input('enter a emp name:'))
        no = int(input('enter a emp number :'))
        desig = str(input('enter a emp designation :'))
        salary = float(input('enter a emp salary :'))
        phone =str(input('enter phone num :'))
        
        data=np.array([(name,no,desig,salary,phone)], dtype=dt1)
        #print(data)
        g1 = np.concatenate([g1,data], axis=0)
        print(g1)
    elif num==3:
        em = input('enter an employee number :')
        for i in range(g1.shape[0]):
            if g1['eno'][i]==em:
                g1 = np.delete(g1, (i), axis=0)
        print(g1)

    elif num==4:
        rec = input('enter employee name or number :')

        for i in range(g1.shape[0]):
            if g1['ename'][i]==rec:
                print(g1[i])
            elif g1['eno'][i]==rec:
                print(g1[i])
    elif num==5:
        totalemp =0
        print('total empoyee are ',g1.shape[0])
        print('total salary is',g1['esalary'].sum())

    elif num==6:
        np.savetxt('f2', g1,  delimiter=',')

    elif num==7:
        global cond
        cond = False
        
cond = True

while cond:
    print('==========================')
    print('CHOOSE A DIGIT ')
    print('1 - Load Data')
    print('2 - Append Data')
    print('3 - Remove Employee Records')
    print('4 - Display Employee Records')
    print('5 - Display Summary')
    print('6 - Save All')
    print('7 - Exit')
    choose = input('Choose a Digit : ')
    choose = int(choose)
    for i in range(8):
        if i == choose:
            action(i)



        
        
