x <-3
y <-4
x*y

(8/2)-(3*4)


8/(2-3)*4

x <- seq(1,20)
x

y <- seq(20, 1, -1)
y

x <- "label"
y <- seq(1, 30)
paste(x,y)




x <- "The quick brown fox jumps over the lazy dog"
sub("brown", "red",x)

x <- "The quick brown fox jumps over the lazy dog"
substr(x,start =17 ,stop =19 )


b <- 10
h <- 20
perimeter <- (2*b+2*h)
perimeter


?rep


x <- c(4, 6, 3)
rep.int(x, 10)

a <- "Hello World"
print(a)

X <- TRUE
X
class(X)
is.numeric(X)
is.character(X)

x <- as.Date("2018-12-26")
x
class(x)
as.numeric(x)
as.character(x)

x <- as.POSIXct("1970-01-03 7:40")
x
class(x)
as.numeric(x)
?abs

x <- 2+3i
y <- 3+5i
x + y
class(x)

x <- "Anu"
y <- "Minu"
paste(x,y)