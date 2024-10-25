#area of traiangle

a=float(input('enter the number 1'))
b=float(input('enter the number 2'))
c=float(input('enter the number 3'))

s=(a+b+c)/2

area=(s*(s-a)*(s-b)*(s-c))**0.5
print"The area of the triangle is %0.2f" % area 
