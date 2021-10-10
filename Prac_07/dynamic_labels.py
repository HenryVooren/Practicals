"""
CP1404/CP5632 Practical
Dynamically create and modify kivy GUI labels
Henry Vooren
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic label creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.name_to_label = {"Henry", "Alicia", "Dick Van-Dyke"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create buttons from dictionary entries and add them to the GUI."""
        for name in self.name_to_label:
            temp_button = Label(text=name)
            self.root.ids.main.add_widget(temp_button)


DynamicLabelsApp().run()
