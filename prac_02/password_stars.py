MINIMUM_LENGTH = 8

def main():
    password = get_password()
    print_asterisks(password)

def get_password():
    password = input(f"Enter your password (the password should be at least {MINIMUM_LENGTH} characters): ")
    while len(password) < MINIMUM_LENGTH:
        print("longer password.")
        password = input(f"Enter your password (the password should be at least {MINIMUM_LENGTH} characters): ")
    return password

def print_asterisks(password):
    print('*' * len(password))


main()
