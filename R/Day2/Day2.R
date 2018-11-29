x<- seq(1,19)
y<- seq(20,1,-1)
z<- c(x,y)
z

x<- c(4,6,3)
x

x<- c(4,6,3)
rep(x,10)


x<- c(4, 6, 3)
rep(x,length.out=31)


x<- rep(4,each=10)
y<- rep(6,20)
z<- rep(3,30)
a<- c(x,y,z)


R <- c(2.27, 1.98, 1.69, 1.88, 1.64, 2.14)
H <- c(8.28, 8.04, 9.06, 8.70, 7.58, 8.34)
V=(1/3)*3.14*R*R*H
V
round(V,2)
min(V)
max(V)



A<- sample(0:999,250)
B<- which(A>900)
B1<- A[B]
C<- sort(B1)

H<- c(180,165,160,193)
W<- c(87,58,65,100)
new_H<- H/100
BMI<- W/new_H^2
Y<- which(BMI>25)
Z<- BMI[Y]
mean(BMI)

a<- c(20,25,45,49,37,44,35,46,39,32)
p1<- mean(a)
p2<-median(a)

dry <- c(77, 93, 92, 68, 88, 75, 100)
sum(dry)
length(dry)
mean(dry)
sum(dry)/length(dry)
sort(dry)
median(dry)
sd(dry)
var(dry)
min(dry)
max(dry)
sd(dry)^2
summary(dry)


N<- sample(1:20,10, replace = TRUE)
A<- N%%2
B<- which(A==0)
N[B]







