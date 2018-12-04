from Tkinter import *
import MySQLdb as db

class Record:
    def SaveRecord(self):
        name = self.name1.get()
        designation = self.desig.get()
        salary1= self.salary.get()
        con = db.connect("127.0.0.1",'ai','ai','ai')
        cur = con.cursor()
        query ="insert into ai1_emp (name,designation,salary)"  + " values('" + name +"','" + designation + "'," + str(salary1) + ")"
        print query
        cur.execute(query)
        con.commit()
        con.close()
        print "inserted 1 row:"
        self.name1.set('')
        self.salary.set('')
        self.desig.set('')
        self.getData()

    def getData(self):
        con = db.connect("127.0.0.1",'ai','ai','ai')
        cur = con.cursor()
        query ="Select * from ai1_emp"
        cur.execute(query)
        result = cur.fetchall()
        i = 11
        totalSalary = 0
        for res in result: #Rows
            i = i +1
            name1 = StringVar()
            name2 = StringVar()
            name3 = StringVar()
            name1.set(res[1])
            name2.set(res[2])
            name3.set(res[3])
            totalSalary += res[3]
            Entry(self.mainWindow,font = ("Times",12,'bold'), textvariable = name1).grid(row=i+1,column=0,columnspan=4)
            Entry(self.mainWindow, textvariable = name2).grid(row=i+1,column=3,columnspan=4)
            Entry(self.mainWindow, textvariable = name3).grid(row=i+1,column=6,columnspan=4)
        con.close()
        #=====total salary========
        totallabel = Label(self.mainWindow, text="Total salary:")
        totallabel.grid(row=i+2,column=1,columnspan=4)
        total = StringVar()
        total.set(totalSalary)
        Entry(self.mainWindow, textvariable = total).grid(row=i+2,column=4,columnspan=4)
        return result
    def CreateFram(self):
        self.mainWindow = Tk()
        self.mainWindow.title("Employee Data")
        self.mainWindow.geometry("600x500")

        self.name1 = StringVar()
        self.desig = StringVar()
        self.salary = IntVar()
        nameLabel = Label(self.mainWindow, text="Enter employee Name:")
        desigLabel = Label(self.mainWindow,text = "Enter employee Designation:")
        salaryLabel = Label(self.mainWindow, text = "Enter employee Salary:")

        e1 = Entry(self.mainWindow, textvariable = self.name1)
        e2 = Entry(self.mainWindow, textvariable = self.desig)
        e3 = Entry(self.mainWindow, textvariable = self.salary)

        nameLabel.grid(row=0,column=0,columnspan=4)
        e1.grid(row=0,column=5,columnspan=4)

        desigLabel.grid(row=2,column=0,columnspan=4)
        e2.grid(row=2,column=5,columnspan=4)

        salaryLabel.grid(row=4,column=0,columnspan=4)
        e3.grid(row=4,column=4,columnspan=5)

        btn = Button(self.mainWindow,bg="light blue",command = lambda : self.SaveRecord(),text = "Submit")
        btn.grid(row=7,column=4,rowspan = 4)

        self.getData() # Get data  
        self.mainWindow.mainloop()
s1 = Record()

s1.CreateFram()
