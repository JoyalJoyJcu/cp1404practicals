from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverter(App):
    """App to convert miles to kilometers."""

    message = StringProperty()

    def build(self):
        """Build the Kivy GUI."""
        self.title = 'Miles to Km'
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = 'Convert miles to km'
        return self.root

    def handle_calculate(self):
        """Handle calculation and display the result in the output label."""
        miles = self.get_validated_miles()
        kilometers = miles * MILES_TO_KM
        self.root.ids.output_label.text = str(kilometers)

    def handle_increment(self, increment):
        """Adjust miles by the given increment and update the calculation."""
        miles = self.get_validated_miles() + increment
        self.root.ids.input_miles.text = str(miles)
        self.handle_calculate()

    def get_validated_miles(self):
        """Get the miles input, validate it, and return a number (0 if invalid)."""
        try:
            miles = int(self.root.ids.input_miles.text)
            return miles
        except ValueError:
            return 0


MilesConverter().run()
