import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
# from kivy.uix.floatlayout import FloatLayout      # IF YOU'D USE FLOAT LAYOUT HERE


# DESIGNATE OUR .kv DESIGN FILE
Builder.load_file('update_label.kv')          # PIRMASIS BUDAS


class MyLayout(Widget):
    def press(self):
        # CREATE A VARIABLE FOR OUR WIDGET
        name = self.ids.name_input.text

        # UPDATE THE LABEL
        self.ids.name_label.text = f'Hello {name}!'

        # CLEAR INPUT BOX
        self.ids.name_input.text = ''
        
   

class AwesomeApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    AwesomeApp().run()