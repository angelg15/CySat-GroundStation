from kivy.app import App
from kivy.core.window import Window
from kivy.uix.relativelayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.utils import get_color_from_hex
from kivy.uix.filechooser import FileChooserIconLayout
from TLElogic import readingTLE

Builder.load_string("""
<HScr>:

	FloatLayout:
		Label:
			text: "CySat_Tracker"
			color: [0,1,0,1]
			font_size: 36
			halign: 'center'
			pos_hint: {'center_x': 0.5, 'top': 1.3 }
		Button:
			text: "Display"
			color: [0,1,0,1]
			pos_hint: {'right': 0.3, 'top': 0.66}
			size_hint: 0.2, 0.16
			on_press:
				root.manager.current = 'display_scr'
		Button:
			text: "Load TLE"
			color: [0,1,0,1]
			pos_hint: {'right': .9, 'top': 0.66}
			size_hint: 0.2, 0.16
			on_press:
				root.manager.current = 'tle_scr'
		Button:
			text: "Communicate"
			color: [0,1,0,1]
			pos_hint: {'right': 0.3, 'top': 0.33}
			size_hint: 0.2, 0.16
			on_press:
				root.manager.current = 'comms_scr'
		Button:
			text: "Options"
			color: [0,1,0,1]
			pos_hint: {'right': 0.9, 'top': 0.33}
			size_hint: 0.2, 0.16
			on_press:
				root.manager.current = 'opt_scr'
<TLE_Loader>
    FloatLayout:
        Button:
            text: "Back"
            color: [0,1,0,1]
            pos_hint: {'right':0.2, 'top':1.0}
            size_hint: 0.2, 0.16
            on_press:
                root.manager.current = 'home_scr'
        Button:
            text: "Load TLE"
            color: [0,1,0,1]
            pos_hint: {'right':0.6, 'top':0.55}
            size_hint: 0.2, 0.16
            on_press:
                root.manager.current = 'fs'
<FileScreen>
    BoxLayout:
        FileChooserIconView:
            canvas.before:
                Color:
                    rgb: .5, .4, .5
                Rectangle:
                    pos: self.pos
                    size: self.size
            on_selection:
                root.manager.current = 'tle_scr'
                root.reading(self.selection[0])

	"""	)

class HScr(Screen):
	pass

class Display(Screen):
	pass

class TLE_Loader(Screen):
	pass

class Communicator(Screen):
	pass

class Options(Screen):
	pass

class FileScreen(Screen):
    def reading(self, filename):
        readingTLE(filename)


sm = ScreenManager()
sm.add_widget(HScr(name = 'home_scr'))
sm.add_widget(Display(name = 'display_scr'))
sm.add_widget(TLE_Loader(name = 'tle_scr'))
sm.add_widget(Communicator(name = 'comms_scr'))
sm.add_widget(Options(name = 'opt_scr'))
sm.add_widget(FileScreen(name = 'fs'))

class PZApp(App):
	def build(self):
		return sm


if __name__ == '__main__':
	PZApp().run()