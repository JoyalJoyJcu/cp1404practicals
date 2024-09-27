MINIMUM_LENGTH = 8
password = input(f"Enter your password (the password should be least {MINIMUM_LENGTH} characters): ")
while len(password) < MINIMUM_LENGTH:
    print("longer Password")
    password = input(f"Enter your password (the password should be least {MINIMUM_LENGTH} characters): ")
print("*" * len(password))
