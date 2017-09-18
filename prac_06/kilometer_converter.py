from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Alan Liang'

MILES_TO_KM = 1.60934


class KilometerCollectorApp(App):
    """ This converts miles to kilometers """
    def build(self):
        Window.size = (580, 320)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('kilometer_converter.kv')
        return self.root

    """ Calculates the kilometer value of a mile input"""
    def handle_calculate(self):
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    """ Allows recalculation when up or down button is pressed and increments by 1 or -1"""
    def handle_increment(self, increment):
        value = self.get_validated_miles() + increment
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    """ Error checking to ensure the value entered is an integer"""
    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

KilometerCollectorApp().run()
