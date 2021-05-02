import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGridLayout(Widget):

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    
    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        # print(f'Hello {name}, you like {pizza} pizza, and your favorite color is {color}.')
        # Print it to the screen
        # self.add_widget(Label(text=f'Hello {name}, you like {pizza} pizza, and your favorite color is {color}.'))
        print(f'Hello {name}, you like {pizza} pizza, and your favorite color is {color}.')

        # Clear the input boxes
        self.name.text = ''
        self.pizza.text = ''
        self.color.text = ''


# my.(kv) failas yra pavadintas taip dėl to, kad šios klasės pavadinimas yra MyApp(kažkodėl .kv failuose negalima
# naudoti žodžio app. Jei klasė vadintųsi "class", tai .kv failas vadintųsi class.(kv))
class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    MyApp().run()