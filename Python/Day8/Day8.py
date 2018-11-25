class Employee :
    def __init__(self, name, empno, basicpay):
        self.name=name
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


n1 = input("name ?")
n2 = input("emp no is ")
n3=input("basic pay is ")
n4= input("tech allowances is ")
n5 = input("category  is ")
n6 = input("grade  is ")
n7= input("dept  is ")

s1=Scientist(n1, n2, n3, n4, n5)
s2=Officer(n1, n2, n3, n6, n7)
s1.display()
s2.display()