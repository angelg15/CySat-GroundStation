from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
<Menu>:
    RelativeLayout:
        size: 600,600
        Label:
            text: "Title"
            color: [0,1,0,1]
            font_size: 150
        Label:
            text: "Random"
            pos: -400,0
        Button:
            text: "Button"
            size: 1,1
            pos: 0,200



""")


class Menu(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Menu(name='menu'))


class UserInterface(App):

    def build(self):
        return sm;



if __name__ == '__main__':
    UserInterface().run()