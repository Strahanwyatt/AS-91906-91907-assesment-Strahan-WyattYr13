import tkinter as tk
from tkinter import *
import time
root = Tk()
root.title
root.geometry ("1280x720")

my_menu = Menu(root)
root.config(menu=my_menu)

#click command
def our_command():
    pass

file_menu = Menu(my_menu)
my_menu.add_cascade(Label="file", menu=file_menu)
file_menu.add_command(Label="new...", command=our_command)

#put a main menu here
var = StringVar()


class UPDOWNtrackers(tk.Tk):

    en1 = tk.Entry(root) #Pulls up the input box in a window
    en1.insert(0,1)
    en1.grid(column=0, row=0)

    def add1(self):
        value = int(en1.get)
        value += 1
        en1.delete(0, 'end')
        en1.insert(0, value)

    def minus1(self):
        value = int(en1.get)
        value -= 1
        en1.delete(0, 'end')
        en1.insert(0, value)




    bt1 = tk.Button(root, text="+1", command=add1)
    bt1.grid(column=1, row=1)


    bt2 = tk.Button(root, text="-1", command=minus1)
    bt2.grid(column=2, row=1)

#Method Here

Def



root.mainloop()


