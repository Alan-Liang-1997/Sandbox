from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

__author__ = 'Alan Liang'


class NameLooperApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = {"Bob", "Cassy", "Tom", "Sam", "Alli", "Alan", "Melina", "Chris"}

    def build(self):
        self.title = "Dynamic Strings"
        self.root = Builder.load_file('name_looper.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_button = Button(text=name)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.entriesBox.add_widget(temp_button)

    def press_entry(self, instance):
        self.status_text = "{}".format(instance.text)

    def add_widget(self):
        temp_button = Button(text="new one")
        temp_button.bind(on_release=self.press_entry)
        self.root.ids.entriesBox.add_widget(temp_button)

    def clear_all(self):
        self.root.ids.entriesBox.clear_widgets()

NameLooperApp().run()