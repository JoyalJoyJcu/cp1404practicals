name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    result = first_number + second_number # adding both numbers
    print(f"the result is: {result}")

total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += int(line)
    print(f"the total of all numbers is: {total}")
