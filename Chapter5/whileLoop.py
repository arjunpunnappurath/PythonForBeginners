number = 100
while number > 0:
    print(number)
    number = number//2

command = ""
while command.lower() != "quit":
    command = input("input : ")
    print("Echo",command)

#infinite loop  

while True:
    cmd = input(">")
    print(cmd)
    if cmd.lower() == "quit":
        break