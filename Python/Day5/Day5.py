def div_f(dividend,divisor=2):
    q=dividend/divisor
    r=dividend%divisor
    return 'Quotient is',q, 'and Reminder is',r
    print('Quotient is',q, 'and Reminder is',r)

div_f(10)


#-----------------------------------------------------------------------------------
    

def div_f(dividend,divisor):
    q=dividend/divisor
    r=dividend%divisor
    return 'Quotient is',q, 'and Reminder is',r
    print('Quotient is',q, 'and Reminder is',r)

div_f(10,5)

#---------------------------------------------------------------------------------------


from mod import *


def mod(k):
    if k==1:
        import mod
        
    elif k==2:
        con = a + 10*b*c - 5*d / e
        print(con)
    elif k==3:
        reload(mod)
        con = a + 10*b*c - 5*d / e
        print(con)
    elif k==0:
        next
    else:
        print('ERROR-INVALID INPUT')
        
        


    
