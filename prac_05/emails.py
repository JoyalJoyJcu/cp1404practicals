def main():
    email = input("Email:")
    name_to_email = {}
    while email != '':
        if email not in name_to_email:
            name = extract_name(email)
            confirm = input(f"Is your name {name}? (Y/n) ").lower()

            if confirm == 'n':
                name = input("Name:")

            name_to_email[email] = name

        email = input("Email: ")

    print()
    for email, name in name_to_email.items():
        print(f"{name} ({email})")

def extract_name(email):
    name_part = email.split('@')[0]
    name = name_part.replace('.', '')
    return name


main()