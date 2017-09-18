from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty


class name_looper_app(App):
    """ Main program - Kivy app to demo dynamic widget creation """
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.words = ["Bob", "Cassy", "Tom", "Sam", "Alli", "Alan", "Melina", "Chris"]

    def build(self):
        self.title = "Dynamic String"
        self.root = Builder.load_file('name_looper.kv')
        for word in self.words:
            temp_label = Label(text=word)
            self.root.ids.entriesBox.add_widget(temp_label)

        return self.root

name_looper_app().run()
