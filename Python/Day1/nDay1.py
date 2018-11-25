import math

print("Hello World")

#-------------------------------------------------------------------------------

x = 120
y = 12

print(x)
print(y)

#-------------------------------------------------------------------------------

def displaymessage():
 print("Hello World")

displaymessage()

#-------------------------------------------------------------------------------

def power():
 n1 = input("Enter the base: ")
 n2 = input("Enter the radical: ")
 print(n1**n2)

power()

#-------------------------------------------------------------------------------


def pwr(a, b):
 print(a**b)

n1 = input("Enter the base: ")
n2 = input("Enter the radical: ")
pwr(n1, n2)

#-------------------------------------------------------------------------------

def dist(x1, y1, x2, y2):
 a = (x2 - x1)**2
 b = (y2 - y1)**2
 c = a + b
 d = math.sqrt(c)
 print(c)

a  = input("Enter x1: ")
b  = input("Enter y1: ")
c  = input("Enter x2: ")
d  = input("Enter y2: ")

dist(a, b, c, d)


