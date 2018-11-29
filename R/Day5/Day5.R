m <- sample(1:20,4, replace=TRUE)

mov<-c('Comedy','Action','Romance', 'Science fiction')
pie(m,mov,col=rainbow(4),radius = 1,main = "data",clockwise = TRUE)
colors<-c("Red","Green","Cyan","Purple")
legend("topright",mov,fill = colors, cex=1)

#-------------------------------------------------


barplot(m,xlab = "Movies Type", ylab = "Data", main = "Bar chart", names.arg = mov,col = rainbow(4))


#--------------------------------------------------

k<- sample(1:20,12, replace=TRUE)
M<- matrix(k,nrow = 4, ncol = 3)

barplot(M, xlab = "Products", ylab = "Quarters", main = "Bar Chart", names.arg = c('A','B','C'), col=rainbow(4))
legend("topleft", c("1st","2nd", "3rd","4rth"), fill = c('Red','Green','Cyan','Purple'),cex=0.9)


#-----------------------------------------------------


mtcars
hist(mtcars$mpg, col = rainbow(4),main = "Histogram")



#---------------------------------------------------------


plot.new()
plot.window(xlim = c(0,20), ylim = c(0,20))
axis(1)
axis(2)
x<- sample(1:20, 5, replace = TRUE)
y<- sample(1:20, 5, replace = TRUE)

points(x,y)
abline(h=20)
abline(v=20)

#-------------------------------------------


drugA <- c(16, 20, 27, 40, 60)
drugB <- c(15, 18, 25, 31, 40)

plot(drugA, type="b", col="Red")
lines(drugB,type="b", col="Green")


#--------------------------------------------------

airquality

boxplot(Temp~Month, data= airquality)

#--------------------------------------------------

plot(iris$Sepal.Length,iris$Sepal.Width, col=rainbow(2))


#----------------------------------------------------
iris
pairs(~Sepal.Length+Sepal.Width+Petal.Length+Petal.Width, data=iris)
