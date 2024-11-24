class Band:
    """Band class for storing the band's name and musicians."""

    def __init__(self, name=""):
        """Initialise a Band instance."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        musicians_str = ""
        for musician in self.musicians:
            musicians_str += f"{musician} "
        return f"{self.name} ({musicians_str.strip()})"

    def __repr__(self):
        """Return a string representation of a Band."""
        return str(vars(self))

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing their first instrument (or not)."""
        play_output = ""
        for musician in self.musicians:
            play_output += f"{musician.play()}\n"
        return play_output.strip()
