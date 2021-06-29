from operator import pos
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.core.audio import SoundLoader

class GridLayoutExample(GridLayout):
    pass



class VPcounter(GridLayout):
    labelnumber = 1
    vp_text = StringProperty(" Victory points" "1")

    self.plusone_button = Button(text = +1)

    self

    def on_Button_click1(self):
        print("blood for the blood god")
        self.labelnumber += 1
        self.vp_text = str(self.labelnumber)


    def on_Button_click2(self):
        print("skulls for the skull throne")
        self.labelnumber -= 1
        self.vp_text = str(self.labelnumber)



class Mainwidget(Widget):
    pass
class warhammerhelperApp(App):
    pass


warhammerhelperApp().run()
