class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage with name, typing, reflection, and year."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language has dynamic typing."""
        return self.typing == 'dynamic'

    def __str__(self):
        """Return a string representation of the ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
