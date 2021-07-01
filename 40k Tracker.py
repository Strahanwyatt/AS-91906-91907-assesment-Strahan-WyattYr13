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

labelnumber = 1



class VPcounter(GridLayout):
    def __init__(self,**kwargs):
        super(VPcounter,self).__init__(**kwargs)

        self.labelnumber = 1
        self.vp_text = StringProperty(" Victory points" "1")

        self.plusone_button = Button(text = "+1", col = 3 , size_hint = (0.25, 0.25), on_press = self.on_Button_click1 )
        self.minusone_button = Button(text ="-1")

        self.add_widget(self.)
        self.add_widget(self.on_Button_click1)

    def on_Button_click1(self):
        print("blood for the blood god")
        self.labelnumber += 1
        self.vp_text = str(self.labelnumber)


    def on_Button_click2(self):
        print("skulls for the skull throne")
        self.labelnumber -= 1
        self.vp_text = str(self.labelnumber)


class app1(App):
    def build(self):
        return VPcounter()

if __name__ =="__main__":
    app1().run()

class Mainwidget(Widget):
    pass
class warhammerhelperApp(App):
    pass


warhammerhelperApp().run()
