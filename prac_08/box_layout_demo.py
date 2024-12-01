from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Demo app showcasing a simple Box Layout with input, output, and buttons."""

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Display a greeting using the text from the input field."""
        print("test")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"
        print("greet")

    def handle_clear(self):
        """Clear the input and output fields."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


BoxLayoutDemo().run()
