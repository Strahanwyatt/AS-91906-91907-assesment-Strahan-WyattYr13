from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class warhammerhelper(App):
    def build(self):
        return Button(text='hello world')

if __name__ =='__main__':
    warhammerhelper().run


"""class WidgetsExample(GridLayout): #blueprint
    def __init__(self, count, my_text):
        self.count = count
        self.my_text = my_text


    def on_button_click(self): # button
        print("button clicked")
        StringProperty("VICTORY POINTS" )
        self.countup += 1"""


