class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar with name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Return the age of the guitar."""
        current_year = 2024
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is vintage (50 years or older)."""
        return self.get_age() >= 50


    def __str__(self):
        """Return a string representation of the Guitar."""
        return f"{self.name} L-5 CES ({self.year}) : ${self.cost:,.2f}"
