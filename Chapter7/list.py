letters = ["a","b","c"]
matrix = [[0,1],[2,3]]

#to create a list of 100 zeros
zeros = [0] * 100
print(zeros)

combined = zeros + letters   

#list of numbers from 0 to 20
numbers =  list(range(20))
print(numbers)

chars = list("Hello world")
print(chars)

print(len(chars))


#accessing lists
print(letters[0])
print(letters[-1])
print(letters[0:3])
print(letters[::2])

print(numbers[::2])
print(numbers[::-1])

#Unpacking lists
first,second,third, *other,last = numbers

print(first,second,third)
print(other)