
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