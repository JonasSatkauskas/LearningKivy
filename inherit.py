import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder


# DESIGNATE OUR .kv DESIGN FILE
Builder.load_file('inherit.kv')          # PIRMASIS BUDAS


class MyLayout(Widget):
    pass
   

class AwesomeApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    AwesomeApp().run()