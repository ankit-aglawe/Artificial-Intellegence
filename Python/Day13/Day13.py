import xml.dom.minidom as dm

doc = dm.Document()

e1 = doc.createElement('eno')
e2 = doc.createElement('ename')
e3 = doc.createElement('edesign')
e4 = doc.createElement('esalary')


#---------------------------------------------------------------------------------------------


import MySQLdb as db
class MysqlDb:
    def __init__(self):
        self.con = db.connect("127.0.0.1",'ai','ai','ai')
        self.cur = self.con.cursor()
       
    def createTable(self):
        try :
            tableName = input("enter table name:")
            query = "create table "  + tableName + "(eno int, ename varchar(20), edesig char(20),esalary int,primary key (eno))"
            self.cur.execute(query)
            self.con.close()
        except Exception,arg:
            print arg

    def insertData(self):
        try :
            tableName = input("enter table name to store data:")
            id2 = input("employee number:")
            name = input("enter name:")
            designation = input("enter designation:")
            salary = input("enter salary:")
            query ="insert into " + tableName + " values(" + str(id2) +",'" + name + "','" + designation + "'," + str(salary) + ")"
          
            self.cur.execute(query)
            self.con.commit()
            self.con.close()
            print "inserted 1 row:"
        except Exception,arg:
            print arg

       
s1 = MysqlDb()
#s1.createTable()
s1.insertData()


