class Employee :
    def __init__(self, name, empno, basicpay):
        self.name = name
        self.empno =empno
        self.basicpay = basicpay

class  Scientist(Employee) :
    def __init__(self,name, empno, basicpay, techall, category):
        Employee.__init__(self, name, empno, basicpay)
        self.techall = techall
        self.category = category
    def display(self):
        print("Your name is ", self.name)
        print("emp no is ", self.empno)
        print("basic pay is ", self.basicpay)
        print("tech allownces is ", self.techall)
        print("category  is ", self.category)


class Officer(Employee) :
    def __init__(self,name, empno, basicpay, grade, dept):
        Employee.__init__(self, name, empno, basicpay)
        self.grade= grade
        self.dept= dept
    def display(self) :
        print("name is ", self.name)
        print("emp no is ", self.empno)
        print("basic pay is ", self.basicpay)
        print("grade  is ", self.grade)
        print("dept  is ", self.dept)

# class newClass(Scientist, Officer):
#     def __int__(self,insta):
#         self.insta = insta
#     def str1(self,name, empno, basicpay,techall, category,grade, dept):
#         Employee.__init__(self, name, empno, basicpay)
#         Scientist.__init__(self,techall, category)
#         Officer.__init__(self,grade, dept)
#
#
#         if insta=="Scientist":
#
#             print("name is ", self.name)
#             print("id is ", self.empno)
#             print("salary is ", self.basicpay)
#
#         elif insta=="Officer":
#             print("name is ", self.name)
#             print("id is ", self.empno)
#             print("salary is ", self.basicpay)
#

class newClass(Employee):
    def str(self,name, empno, basicpay, insta) :
        self.insta= insta
        Employee.__init__(self, name, empno, basicpay)
        if insta == "Scientist":

                print("name is ", self.name)
                print("id is ", self.empno)
                print("salary is ", self.basicpay)

        elif insta=="Officer":
                print("name is ", self.name)
                print("id is ", self.empno)
                print("salary is ", self.basicpay)



n1 = input("name ?")
n2 = input("emp no is ")
n3=input("basic pay is ")
n4= input("tech allowances is ")
n5 = input("category  is ")
n6 = input("grade  is ")
n7= input("dept  is ")
insta =input("enter profession :")

s1=Scientist(n1, n2, n3, n4, n5)
s2=Officer(n1, n2, n3, n6, n7)
s1.display()
s2.display()

s3=newClass(n1, n2, n3, insta)

s3.str()
