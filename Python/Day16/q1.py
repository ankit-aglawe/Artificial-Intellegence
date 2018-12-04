
from Tkinter import *

mwin = Tk()

exp =''

def click(p):
    global exp
    if (p == '='):
        t1.set(str(eval(exp)))
        exp=''

    else:
        exp = exp + p
        t1.set(exp)
        
def clear(): 
    global expression 
    expression = "" 
    t1.set("")
 
def clear1():
    
    global vexp
    s = e1.get()
    vexp = s[:-1]
    t1.set(vexp)

    
mwin.title('Best Calculator')
mwin.geometry('265x300')

t1=StringVar()
e1=Entry(mwin,textvariable=t1).grid(row=0,column=0, columnspan=5)

b1=Button(mwin,text='1',command= lambda: click('1')).grid(row=1,column=0)
b4=Button(mwin,text='4',command= lambda: click('4')).grid(row=2,column=0)
b7=Button(mwin,text='7',command= lambda: click('7')).grid(row=3,column=0)

b2=Button(mwin,text='2',command= lambda: click('2')).grid(row=1,column=1)
b5=Button(mwin,text='5',command= lambda: click('5')).grid(row=2,column=1)
b8=Button(mwin,text='8',command= lambda: click('8')).grid(row=3,column=1)

b3=Button(mwin,text='3',command= lambda: click('3')).grid(row=1,column=2)
b6=Button(mwin,text='6',command= lambda: click('6')).grid(row=2,column=2)
b9=Button(mwin,text='9',command= lambda: click('9')).grid(row=3,column=2)

b0=Button(mwin,text='0',command= lambda: click('0')).grid(row=4,column=1)


add=Button(mwin,text='+',command= lambda: click('+')).grid(row=1,column=3)
multi=Button(mwin,text='x',command= lambda: click('*')).grid(row=1,column=4)
sub=Button(mwin,text=' - ',command= lambda: click('-')).grid(row=2,column=3)
div=Button(mwin,text='/',command= lambda: click('/')).grid(row=2,column=4)
equal=Button(mwin,text='=',command= lambda: click('=')).grid(row=3,column=3)

clear=Button(mwin,text='AC',command=clear).grid(row=4,column=2)
back=Button(mwin,text='B',command= clear1).grid(row=4,column=3)






mwin.mainloop()
