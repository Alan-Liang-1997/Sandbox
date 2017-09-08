from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """ This program shows how box layout format works, along with simple inputs and output labels"""
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    """ Prints to the output label the name entered in the input box"""
    def handle_greet(self):
        # print("Greet")
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    """ Clears the output label and input terminal"""
    def handle_clear(self):
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
