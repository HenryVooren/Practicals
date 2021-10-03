"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles into km
Henry Vooren
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

__author__ = 'Henry Vooren'

MILES_TO_KM = 1.60934


class ConvertMilesApp(App):
    output_label = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def step_number(self, step):
        self.root.ids.number_label.text = str(int(self.root.ids.number_label.text) + step)

    def handle_update(self):
        try:
            self.root.ids.output_label.text = str(int(self.root.ids.number_label.text)*MILES_TO_KM)
        except ValueError:
            self.root.ids.output_label.text = str(0.0)


ConvertMilesApp().run()
