from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self, button):
        self.root.ids.my_label.text = "Greetings "+self.root.ids.input_name.text

    def clear_fields(self, button):
        self.root.ids.my_label.text = ""
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
