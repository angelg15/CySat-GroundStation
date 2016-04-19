from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.properties import StringProperty
Builder.load_string("""
<Ex21>:
    cols: 3
    canvas:
        Color:
            rgb: .2,.2,.2
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        text: 'A checkbox'
    CheckBox:
        on_active: root.checkActive(*args)
    Label:
        text: root.Status
    Label:
        text: 'A group checkbox'
    CheckBox:
        group: 'my_check_group'
        on_active: root.checkActive1(*args)
    Label:
        text: root.Status1
    Label:
        text: 'A group checkbox'
    CheckBox:
        group: 'my_check_group'
        on_active: root.checkActive2(*args)
    Label:
        text: root.Status2
    Label:
        text: 'Python is the best language'
    CheckBox:
        id: pythonLang
        active: True
        on_active: root.checkActive3(*args)
    Label:
        text: 'Right on'
""")
class Ex21(GridLayout):
    Status=StringProperty("I am inactive")
    Status1=StringProperty("I am the inactive member of the group")
    Status2=StringProperty("I am the inactive member of the group")
    def checkActive(self,*args):
        if args[1]==True: self.Status="I am active"
        else: self.Status="I am inactive"
    def checkActive1(self,*args):
        if args[1]==True: self.Status1="I am the active member of the group"
        else: self.Status1="I am the inactive member of the group"
    def checkActive2(self,a,b):
        if b==True: self.Status2="I am active member of the group"
        else: self.Status2="I am the inactive member of the group"
    def checkActive3(self,*args):
        if args[1]==False: self.ids['pythonLang'].active=True       

class Ex21App(App):
    def build(self):
        self.title="Checkboxes"
        return Ex21()

if __name__=='__main__':
    Ex21App().run()





