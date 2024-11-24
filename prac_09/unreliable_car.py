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
        random_number = random.uniform(0, 100)
        if random_number < self.reliability:
            return super().drive(distance)
        return 0
