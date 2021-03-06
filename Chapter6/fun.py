#Functions that perform a task
def greet():
    print("Hi there")
    print("Welcome aboard")


greet()

#Parameterized functions
def greetings(first_name, last_name):
    print("Hi "+ first_name,last_name)

greetings("john","doe")


#Functions that return a value

def get_greeting(name):
    return "Hi "+name

message = get_greeting("Mosh")
print(message)

#function declaration with a default parameter
def increment(number,by=1):
    return number+by

res= increment(2)
result = increment(number=2,by=2)
print(res)
print(result)
#another way to print the result is as shown below,
print(increment(2,6))

#function with variable number of params
def multiply(*numbers):
    total = 1
    for num in numbers:
        total *= num
    return total
  
print(multiply(2,3,4,5))

def save_user(**user):
    print(user["name"])
save_user(id=1, name ="John", age = 22)


