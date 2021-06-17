
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button

class WidgetsExample(GridLayout): #blueprint
    def __init__(self, count, my_text):
        self.count = count
        self.my_text = my_text

        StringProperty("VICTORY POINTS")



    def on_button_click(self): # button
        print("button clicked")
        self.count += 1
        self.my_text = str(self.count )





    "button.config"
    "self.my_text = str(self.count VP."
    "self.count += 1"


class BoxLayoutExample(BoxLayout):
   pass
   """ def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        b1 = Button(text="A")
        b2 = Button(text="b")
        
        self.add_widget(b1)
        self.add_widget(b2)"""

class GridLayoutExample(GridLayout):
    pass

class MainWidget(Widget):
    pass

class WarhammerHelperApp(App):
    pass

WarhammerHelperApp().run()
