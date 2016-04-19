from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.clock import Clock
import datetime

class Counter_Timer(BoxLayout):
	days = StringProperty()
	hours = StringProperty()
	minutes = StringProperty()
	seconds = StringProperty()

	def build(self, datetimeOBJ):
		self.datetimeOBJ = datetimeOBJ

	def update(self, dt):
		delta = self.datetimeOBJ - datetime.datetime.now()
		self.days = str(delta.days)
		hour_string = str(delta).split(', ')[1]
		self.hours = hour_string.split(':')[0]
		self.minutes = hour_string.split(':')[1]
		self.seconds = hour_string.split(':')[2].split('.')[0]
		# self.days, self.hours, self.minutes, self.seconds

class Counter(App):

	def build(self , t):
		Counter = Counter_Timer(t)
		Clock.schedule_interval(Counter.update, 1.0)
		return Counter

#Hey so this one will have to have update called on it inside of a loop
class ManualCounter(App):
	def build(self,t):
		ManualCounter = Counter_Timer(t)
		return ManualCounter

if __name__=='__main__':
	Counter().run()