import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# SET THE APP SIZE
Window.size = (500, 700)


# DESIGNATE OUR .kv DESIGN FILE
Builder.load_file('calc.kv')          # PIRMASIS BUDAS


class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'
   

class CalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    CalculatorApp().run()