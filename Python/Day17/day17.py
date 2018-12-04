import numpy as np

l1=[1,2,3,4,5]

a= np.array(l1)

print(a)

#------------------------------------------------

b = np.arange(6)

print(b)

#------------------------------------------------

c = np.ones((2,5,4))

print(c.size)

#-------------------------------------------------
l2 =[6,7,8,9,10]

a1 =np.asarray([l1,l2])

a2 = np.array([l1,l2])

#------------------------------------------------------

d = np.eye(100)
print(d)


#-------------------------------------------------------

e = np.zeros((2,5,4))

print(c.size)


#------------------------------------------------------


print(a.size)
print(b.size)
print(c.size)
print(d.size)
print(e.size)
print(a2.size)

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(e.ndim)
print(d.ndim)
print(a2.ndim)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(a2))

print(a.shape)
print(b.shape)
print(c.shape)
print(d.shape)
print(a2.shape)
print(e.shape)


