

a = input("Enter a sentence : ").split(' ')
k = a[::-1]
print(k)


#-------------------------------------------------------



a = input("Enter a sentence : ").split(' ')
k=0
print(a)
for word in a:
  if word==word[::-1]:
    k=k+1

print("Number of Palindrome Words are ",k)


#------------------------------------------------------



a = input("Enter a string:")

b ={}
for char in a:
  if char in b:
    b[char]+=1
  else:
    b[char]=1
print(b)


#--------------------------------------------------------



a = input("Enter a sentence: ").split(' ')

b ={}

for word in a:
  if word in b:
    b[word]+=1
  else:
    b[word]=1
print(b)


#---------------------------------------------------


