def greet(name):
    message = name #here message is a local variable so it exits only here
    print message

#print(message) # this is outside of the scope of the greet function so it will throw error


#Here the msg wil print as a as the change in value of 
# msg has happened only locally inside the function.
msg = "a"
def send_email(name):
    msg = "b"

greet("Mosh")
print(msg)
send_email("john")
print(msg)