MINIMUM_LENGTH = 8

def main():
    """Runs the password input and asterisk print process."""
    password = get_password()
    print_asterisks(password)

def get_password():
    """Gets a password of at least MINIMUM_LENGTH."""
    password = input(f"Enter your password (min {MINIMUM_LENGTH} chars): ")
    while len(password) < MINIMUM_LENGTH:
        print("Password too short.")
        password = input(f"Enter your password (min {MINIMUM_LENGTH} chars): ")
    return password

def print_asterisks(password):
    """Prints asterisks matching the password length."""
    print('*' * len(password))

main()
