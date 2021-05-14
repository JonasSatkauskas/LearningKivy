import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder


# DESIGNATE OUR .kv DESIGN FILE
Builder.load_file('round_buttons.kv')          # PIRMASIS BUDAS


class MyLayout(Widget):
    pass
   

class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return MyLayout()


if __name__ == "__main__":
    AwesomeApp().run()