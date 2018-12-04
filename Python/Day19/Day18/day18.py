import numpy as np

a1= np.arange(6, dtype='i4').reshape(2,3)

print(a1.dtype)

a1c = a1.copy()

print(a1c.astype('f8'))


a2c = a1.copy()

np.str(a2c)


a1= np.arange(6).reshape(2,3)


b1[0,:]
b1[2,:]
b1[:,1]
b1[2:,:2]
b1[:,2]

c1 = np.arange(11,51).reshape(8,5)
c1[c1%5==0]=-1

#----------------------------------
def dia(array):
    mod =[]
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if i==j:
                mod.append(array[i][j])
                
    print(mod)

#------------------------------------------


def occ(array,num):
    k=0
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if c1[i][j] == num:
                k+=1
    print(k)
    
        
        
    
