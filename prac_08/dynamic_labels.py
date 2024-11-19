from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Simple app to demonstrate dynamic creation of labels."""

    def __init__(self, **kwargs):
        """Initialize the app with a predefined list of names."""
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Edward"]

    def build(self):
        """Build the Kivy GUI and create dynamic labels."""
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Dynamically create labels for each name and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


if __name__ == "__main__":
    DynamicLabelsApp().run()
