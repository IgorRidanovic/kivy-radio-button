#! /usr/bin/env python

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

# Kivy radio button example

class RadioButton(Widget):
	# State labels
	slabel1 = StringProperty()
	slabel2 = StringProperty()

	def savedstate(self):
		# Here we can retrieve user saved radio button state if one exists
		# Assign optional label values
		self.slabel1 = 'On'
		self.slabel2 = 'Off'
		return ['down', 'normal']

	def switchstate1(self):
		# Switch radio button 1 on and process event trigger
		# Force 'down' state to avoid deselecting all radio buttons (Kivy thing)
		self.ids.rbutton1.state = 'down'
		# Update optional label values
		self.slabel1 = 'on'
		self.slabel2 = 'off'
		print self.ids.rbutton1.state, self.ids.rbutton2.state

	def switchstate2(self):
		# Switch radio button 2 on and process event trigger
		# Force 'down' state to avoid deselecting all radio buttons (Kivy thing)
		self.ids.rbutton2.state = 'down'
		# Update optional label values
		self.slabel1 = 'off'
		self.slabel2 = 'on'
		print self.ids.rbutton1.state, self.ids.rbutton2.state

class RadioButtonApp(App):
	def build(self):
		return RadioButton()

if __name__ == '__main__':
	RadioButtonApp().run()
