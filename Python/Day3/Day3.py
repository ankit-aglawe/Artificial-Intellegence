#-----------------------

a = input("enter a string:")
k=0

for char in a:
        k=k+1
print(k)


#-----------------------------------


a = input("enter a string: ")

b = a[::-1]

print(b)



#-----------------------------------


a = input("enter a string: ")

b = input("enter a character : ")
k=0

for char in a :
  if b==char:
    k=k+1
print(k)


#------------------------------------


s = input("Enter a string: ").lower()
k =0
b = 'aeiou'

for char in s :
  if char in b:
    print(char)
    k=k+1
if k>=2:
  print("This String have at least two vowels")



#------------------------------------------









