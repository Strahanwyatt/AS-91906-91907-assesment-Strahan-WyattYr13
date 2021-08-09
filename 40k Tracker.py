import tkinter as tk
from tkinter import *
Root = Tk()
Root.title('Warhammer companion app')
Root.geometry('500x500')
var = StringVar()

class VPCounter:
    def __init__(self, VP):
        self.VP = VP

        self.add1_button = Button(VP,"+1", command=self.Plus1)
        self.add1_button.pack()

        self.minus1_button = Button(VP,"-1", command=self.Minus1)
        self.minus1_button.pack()

    def Minus1(self):
            print("-1")

    def Plus1 (self):
            print("-1")


git hub and classes 

Root.mainloop()



"""    





from tkinter import Tk, Label, Button

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop() 

"""






