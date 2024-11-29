import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
PICK_LENGTH = 6

number_of_picks = int(input("How many quick picks? "))

for i in range(number_of_picks):
    numbers = []
    for i in range(PICK_LENGTH):
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while number in numbers:
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        numbers.append(number)
    numbers.sort()
    numbers_string = ' '.join([f'{number:2}' for number in numbers])
    print(numbers_string)



