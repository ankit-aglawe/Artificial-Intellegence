A<- data.frame(sname=c('Alex','Lilly','Mark' ), Age=c(25,31, 23), Height=c(177,163,190), Weight=c(57,69,83), Sex=c('F','F','M'))
A
B<- data.frame(Working=c('Yes','No','No'))
B
C<- cbind(A,B)

#------------------------------------------------------------------

class(A)
mean(A[,3])
#------------------------------------------------------------------

bmi<-(A[,4]*10000)/(A[,3]**2)
BMI<- data.frame(bmi)
D<-cbind(C,BMI)
Healthy<-ifelse(bmi<25,"Yes","No")
E<- cbind(D,Healthy)


#----------------------------------------------------------------


getwd()
r1<- read.table(file.choose())
h<-read.csv(file.choose())



#----------------------------------------------------------------



r<-c('r1','r2')
c<-c('c1','c2','c3')
m<-c('m1','m2','m3')
A<- array(1:20, dim=c(2,3,3),list(r,c,m))

#--------------------------------------------------------------------

mtcars
new<- data.frame(mpg=mtcars$mpg,cyl=mtcars$cyl,hp=mtcars$hp)

t1<- data.frame(head(mtcars, 5))
t2<- data.frame(tail(mtcars, 5))
n1<- rbind(t1,t2)

#---------------------------------------------------------------------


sum<-function(a,b)
{
  s=a+b
  print(s)
}

sum(5,4)



sum<-function(a=1,b=1)
{
  s=a+b
  print(s)
}

sum()
sum(10,20)

#---------------------------------------------------------------------------


print(getwd())

