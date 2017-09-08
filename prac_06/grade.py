from kivy.app import App
from kivy.lang import Builder


class GradeCalculator(App):
    """ This program shows how box layout format works, along with simple inputs and output labels"""
    def build(self):
        self.title = "Grade Calculator App"
        self.root = Builder.load_file('grade.kv')
        return self.root

    """ Prints to the output label the name entered in the input box"""
    def handle_greet(self):
        # print("Greet")
        value = self.get_validated_score()
        if value >= 85:
            self.root.ids.output_label.text = "High Distinction"
        elif value >= 75:
            self.root.ids.output_label.text = "Distinction"
        elif value >= 65:
            self.root.ids.output_label.text = "Credit"
        elif value >= 50:
            self.root.ids.output_label.text = "Pass"
        else:
            self.root.ids.output_label.text = "Fail"

    """ Clears the output label and input terminal"""
    def handle_clear(self):
        self.root.ids.output_label.text = ""
        self.root.ids.input_score.text = ""

    def get_validated_score(self):
        try:
            value = int(self.root.ids.input_score.text)
            if 0 < value > 100:
                value = 0

            return value
        except ValueError:
            return 0


GradeCalculator().run()
