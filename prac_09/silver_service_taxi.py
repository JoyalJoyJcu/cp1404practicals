from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi with additional fanciness and flagfall charges."""

    flagfall = 4.50  # Extra charge for each fare

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * self.fanciness  # Custom price per km

    def get_fare(self):
        """Calculate the fare, including flagfall and distance."""
        fare = super().get_fare() + self.flagfall
        return fare

    def __str__(self):
        """Return a string representation of the SilverServiceTaxi, including flagfall."""
        return f"{super().__str__()}, plus flagfall of ${self.flagfall:.2f}"
