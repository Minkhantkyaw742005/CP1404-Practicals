MINIMUM_LENGTH = 7
password = input("Set password: ")
while len(password) < MINIMUM_LENGTH:
    print("Too short")
    password = input("Set password: ")
for i in range(len(password)):
    print("*",end="")
