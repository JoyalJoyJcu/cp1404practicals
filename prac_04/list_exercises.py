
numbers = []

for i in range(5):
    number = int(input('Enter a number: '))
    numbers.append(number)

first_number = numbers[0]
last_number = numbers[-1]
smallest_number = min(numbers)
biggest_number = max(numbers)
average = sum(numbers) / len(numbers)

print(f"the first number is {first_number}")
print(f"the last number is {last_number}")
print(f"the smallest number is {smallest_number}")
print(f"the biggest number is {biggest_number}")
print(f"the average number is {average}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("What is your username? ")
if username in usernames:
    print(f"access granted")
else:
    print("access denied")
