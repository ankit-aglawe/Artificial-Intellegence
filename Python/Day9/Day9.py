class vector:
    def __init__(self, x, y):
        self.x= x
        self.y= y

    def display(self):
        print(self.x)
        print(self.y)

    def __add__(self, p):
        n1= self.x+p.x
        n2= self.y+p.y
        v= vector(n1, n2)
        return v


v1= vector(10, 20)
v2= vector(40, 60)

v3=v1+v2
v1.display()
v2.display()
v3.display()


#------------------------------------------------------------------------------------------------------------------------

class complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        ## self.c=c
        ## self.d=d
    def display(self):

        print("(%d + %d*i)"%(self.a, self.b))
        ## print("(%d + %d*i)"%(self.c, self.d))
        ## print("(%d + %d*i) + (%d + %d*i) = (%d)+(%d)*i"%(self.a, self.b, self.c, self.d, self.a+self.c, self.b+self.d))


    def __add__(self, other):
        n1=self.a+other.a
        n2= self.b+other.b
        ## n3=self.c+other.c
        ## n4= self.d+other.d

        p1=complex(n1,n2)
        ## p2=complex(n2,n4)
        return p1

z1=complex(5,6)
z2=complex(7,8)
z1.display()
z2.display()
z3=z1+z2
z3.display()


#-----------------------------------------------------------------------------------------------------------------------


class complexMulti:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def display(self):
         print("(%d + %d*i)"%(self.a, self.b))

    def __mul__(self, other):
         return complexMulti((self.a*other.a-self.b*other.b),(self.a*other.b+self.b*other.a))

h1=complexMulti(3,2)
h2=complexMulti(1,7)
h3=h1*h2

h1.display()
h2.display()
h3.display()


#--------------------------------------------------------------------------------------------------------------------------


import abc


class vehicle:
    __metaclass__ = abc.ABCMeta
    no = 100

    def __init__(self):
        vehicle.no += 1
        self.vowner = raw_input("owner?")
        self.vno = vehicle.no
        self.vym = input("yearofmake?")
        self.vbp = input("buyingprice in tousands?") * 1000
        self.vpv = self.vbp

    #    @abc.abstractmethod
    def cal_pv(self):
        pass

    def display(self):
        print
        " --- info ---\nType: %s, Vno : %s, owner : %s,\nNoofwheels : %s, yearofmake : %d, \nprice : %d, presentVal : %d " % (
        self.type, self.vno, self.vowner, self.vwheels, self.vym, self.vbp, self.vpv)


class car(vehicle):
    def __init__(self):
        self.type = "car"
        self.vwheels = 4
        vehicle.__init__(self)

    def cal_pv(self):
        self.vpv = self.vbp - (2018 - self.vym) * 5000


class bus(vehicle):
    def __init__(self):
        self.type = "bus"
        self.vwheels = 6
        vehicle.__init__(self)

    def cal_pv(self):
        self.vpv = self.vbp - (2018 - self.vym) * 1000


class truck(vehicle):
    def __init__(self):
        self.type = "truck"
        self.vwheels = 10
        vehicle.__init__(self)

    def cal_pv(self):
        self.vpv = self.vbp - (2018 - self.vym) * 12000


v1 = truck()
v1.cal_pv()
v1.display()


