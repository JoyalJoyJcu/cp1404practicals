# line 1
# What you see: A random integer between 5 and 20 (inclusive).
# Smallest number: 5
# Largest number: 20

# line 2
# What you see: A random integer between 3 and 9, but only from the numbers that match the step size of 2, which means the possible numbers are 3, 5, 7, and 9.
# Smallest number: 3
# Largest number: 9
# No, because the step size of 2 ensures only odd numbers (3,5,7,9)

# line 3
# What you see: A random floating-point number between 2.5 and 5.5.
# Smallest number: 2.5
# Largest number: 5.5

import random

random_number = random.randint(1,100)