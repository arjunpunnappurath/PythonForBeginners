
course = "Python Programming"

message = """ 
Hi John,

This is a test message
"""

#To find the length of a string
print(len(course))

#To access the first character in the string
print(course[0])

#Negative indexes are used to pick values from the end of the string
print(course[-1])

#Prints first 3 characters
print(course[0:3])

#Same result as of above
print(course[:3])

#how to place a double quotes in the middle of a string (Place using \"")
#The back-slash is an escape character. eg: \", \', \\
cc = "Python \" Programming"
cd = "Python \' Programming"
ce = "Python \\ Programming"
cf = "Python \n Programming"
print cc
print cd
print ce
print cf


#Simple string concatenations

first = "John"
last = "Doe"
full = first + " " + last
print (full)

#String methods
python = "python programming"
print(len(python))

#convert the text to uppercase  but the original string is not affected
print(python.upper())
print(python)

capPython = python.upper()
print(capPython)

print(python.lower())

#converts the first letter of every work capitial
print(python.title)

#removes the white spaces
print(python.strip())

#To get the index of a character use find method
print(python.find("pro"))

#Replace a character or a sequence of character
print(python.replace("p","j"))

#This returns a boolean value
print("pro" in python)

#not operator
print("swift" not in python)