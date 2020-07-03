import math

#numbers

x = 1
y=1.1
z= 1+2j

print(10+3)
print(10-3)
print(10*3)
print(10/3)
print(10//3) # gets the values after the dot as well\
print(10%3)
print(10 ** 3)

x = x+3
x += 3

#some built-in numbers

print(round(2.9))
print(abs(-2.9))
print(math.ceil(2.2))

x = input("x: ") #By default we will get an input as string
y = int(x)+1 #Here we are converting the x to an integer
print(y)
# int(x)
# float(x)
# bool(x)
# str(x)

print(type(x))

#Boolean false values
#""
#0
#None

print(bool(0))
print(bool(1))
print(bool(""))
print(bool("False"))