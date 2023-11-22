MINIMUM_LENGTH = 7
def main():
    password = get_valid_password()
    print_asterisks(password)


def print_asterisks(password):
    for i in range(len(password)):
        print("*", end="")


def get_valid_password():
    password = input("Set password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Too short")
        password = input("Set password: ")
    return password

main()