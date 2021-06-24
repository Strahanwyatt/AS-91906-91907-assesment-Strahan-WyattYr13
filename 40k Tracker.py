from operator import pos
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.core.audio import SoundLoader

class GridLayoutExample(GridLayout):
    pass


class VPcounter(GridLayout):
    def on_Button_click1(self):
        print("blood for the blood god ")

    def on_Button_click2(self):
        print("skulls for the skull throne")

class Mainwidget(Widget):
    pass
class warhammerhelperApp(App):
    pass


warhammerhelperApp().run()
