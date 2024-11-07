from prac_07.guitar import Guitar


def main():
    guitars = []
    with open('guitars.csv', 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)

    print("These are the guitars currently loaded:")
    for guitar in guitars:
        print(guitar)

    print("\nAdd a new guitar:")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")

        name = input("Name: ")

    with open('guitars.csv', 'w') as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
    print("\nUpdated guitars.csv.")


main()
