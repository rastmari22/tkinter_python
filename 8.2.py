from tkinter import *

window = Tk()

colorcode = [
    "#ff0000",
    "#ff7d00",
    "#ffff00",
    "#00ff00",
    "#007dff",
    "#0000ff",
    "#7d00ff",
]
colorname = [
    "красный",
    "оранжевый",
    "желтый",
    "зеленый",
    "голубой",
    "синий",
    "фиолетовый",
]
clr = dict(zip(colorcode, colorname))

frameForText = Frame(window)
frameForButton = Frame(window)

frameForText.pack(side=TOP)
frameForButton.pack(side=BOTTOM)

lb = Label(frameForText, text="color")
lb.pack()


class MyButton:
    def __init__(self, c):
        self.bt = Button(frameForButton, bg=c, width=10, height=5)
        self.bt.pack(side=LEFT)

    def setfunc(self, func):
        self.bt["command"] = eval("self." + func)

    def showinf(self):
        colr = self.bt.cget("bg")
        lb["text"] = clr[colr]
        lb["fg"] = colr
        lb.pack()


for i in clr.keys():
    print(i)
    MyButton(i).setfunc("showinf")

window.mainloop()
