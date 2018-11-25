
def oe(num):
  if num%2==0:
    print("even")
  else: 
    print("odd")


oe(10)

#---------------------------------------------------------------------------------------------


def numbers(x, y, z):
  if (x > y) and (x > z) :
    print(x," is the gretest no. among three")
  elif (y > x) and (y > z) :
    print(y," is the greatest no. among three")
  elif (z > x) and (z > y) :
    print(z," is the greatest no. among three")

numbers(10,20,30)
#---------------------------------------------------------------------------------------------


num = 11
num = int(input("enter a number:"))

if num%2==0:
    print("even")
else: 
    print("odd")

#---------------------------------------------------------------------------------------------

x=20
y=30
z=60
if (x > y) and (x > z) :
    print(x," is the gretest no. among three")
elif (y > x) and (y > z) :
    print(y," is the greatest no. among three")
elif (z > x) and (z > y) :
    print(z," is the greatest no. among three")


#-----------------------------------------------------------------------------------------------

name = input("Enter your name ? :")
marks = input("Enter Your Score ? :")
marks = int(marks)
print(name," score ",marks," out of 100")


name = input("Enter your name ? :")
marks =input("Enter Your Score ? :")
marks = int(marks)
print(name," score ",marks," out of 100")

#----------------------------------------------------------------------------------------------

a = input("enter some numbers :")
a = int(a)
b = a.sort()
print(a)


#-----------------------------------------------------------------------------------------------


num = []
for i in range(1,11):
  num.append(int(input("enter a number : ")))
print(num)


a, b, c = input("enter three numbers with commas :").split(',')


#------------------------------------------------------------------------------------------


a = input("enter numbers with commas :").split(',')

print(c)
c= a.sort()
print(c)



#-----------------------------------------------------------------------------------------


#factorial 

num = input("enter a number :")
num = int(num)
k = 1
for i in range(num-1):
  k = k*num
  num=num-1
 
  
print(k)


#------------------------------------------------------------------------------------------------

#factorial
def factorial(num):
  if num == 1:
    return 1
  else:
    return  num*factorial(num-1)

#---------------------------------------------------------------------------------------------------

#factorial
num = input("enter a number :")
num = int(num)
while num>= 1 :
  k = num*num
  print(k)


#----------------------------------------------------------------------------------------------------

#prime
num = input("enter a number :")
num = int(num)

i = 2
k = 0

while num>i :
  if num%i==0 :
    k = 1
    print("composite number")
  i = i+1

if k==0:
  print("prime number")















