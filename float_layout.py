import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
# from kivy.uix.floatlayout import FloatLayout      # IF YOU'D USE FLOAT LAYOUT HERE


# DESIGNATE OUR .kv DESIGN FILE
Builder.load_file('float_layout.kv')          # PIRMASIS BUDAS


class MyLayout(Widget):
    pass
   

class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1,)
        return MyLayout()


if __name__ == "__main__":
    AwesomeApp().run()