from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
<Menu>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: "Title"
            color: [0,1,0,1]
            font_size: 150
        Button:
            text: "function 1"
            color: [0,1,0,1]
            on_press: root.manager.current = 'f1'
        Button:
            text: "function 2"
            color: [0,1,0,1]
            on_press: root.manager.current = 'f2'

<Function1>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text:"f1"
            color: [0,1,0,1]
        TextInput:
        Button:
            text:"back"
            color: [0,1,0,1]
            on_press: root.manager.current = 'menu'
<Function2>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text:"f2"
            color: [0,1,0,1]
        Button:
            text:"back"
            color: [0,1,0,1]
            on_press: root.manager.current = 'menu'



""")

class Function1(Screen):
    pass
class Function2(Screen):
    pass
class Menu(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Menu(name='menu'))
sm.add_widget(Function1(name='f1'))
sm.add_widget(Function2(name='f2'))

class UserInterface(App):

    def build(self):
        return sm;



if __name__ == '__main__':
    UserInterface().run()