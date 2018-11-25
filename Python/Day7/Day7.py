class employee:
    def store(self,name, empno, salary):
        self.name= name
        self.empno = empno
        self.salary = salary
    def display(self,name, empno, salary):
        print('Name is :',name)
        print('Employee No. :',empno)
        print('salary is :', salary)


class employee1:
    def __init__(self,name,empno,salary):
        self.name= name
        self.empno = empno
        self.salary = salary
    def display(self):
        print('Name is :',self.name)
        print('Employee No. :',self.empno)
        print('salary is :', self.salary)



p1= employee()
p1.display('ankit', 1, 100000)


p2= employee1('tom', 2, 30)
p2.display()




#--------------------------------------------------------------



class BankAccounts:
    cnt=0
    bank ={}

    def __init__(self,an, ab, at,name, add):
        self.AccountNumber = an
        self.AccountBalance = ab
        self.AccoutType = at
        self.name= name
        self.address = add

        bank=dict(AccountNumber=self.AccountNumber,AccountBalance=self.AccountBalance,AccoutType=self.AccoutType,name=self.name,address=self.address)
        print(bank)
        BankAccounts.cnt+=1
        print('total accounts are',BankAccounts.cnt)
        
    def deposit(self):
        print('Account No',self.AccountNumber)
        print('Account balance',self.AccountBalance)
        print('Account Type',self.AccoutType)
        

    def withdraw(self):
        print('Account No',self.AccountNumber)
        print('Account balance',self.AccountBalance)
        print('Account Type',self.AccoutType)
        
        
    def getdetails(self):
        print('Account User name',self.name)
        print('Users Address',self.address)
        print('Account balance',self.AccountBalance)
        print('Account Type',self.AccoutType)
        
        
    

p=BankAccounts(2,7500,"saving","Ankit","Wardha")

