import random
from car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car based on reliability."""
        # Generate a random number between 0 and 100
        random_number = random.uniform(0, 100)
        # Check if the car is reliable enough to drive
        if random_number < self.reliability:
            return super().drive(distance)  # Call the parent method
        return 0  # Car did not drive
