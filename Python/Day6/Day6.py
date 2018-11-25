a= int(raw_input("enter a number :"))
f1=open('f1','w')
l1=[num*a for num in range(1,11)]
for i in range(1,11):
    c='%d X %d=%d'%(i,a,l1[i-1])
    f1.write(c)
    f1.write('\n')
    print(c)
f1.close()   

    

#-------------------------------------------

#!/usr/bin/env python
import sys

open(sys.argv[1],'w').write( "\n".join( ["%d x %s = %d"%(x,sys.argv[2],x*int(sys.argv[2])) for x in range(11)] ))