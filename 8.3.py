
from tkinter import *
import random
window = Tk()
window.title("Задание 2")
window.geometry("500x200")
# 8 6 41 3 1

class Group_Widgets:
    def __init__(self, window):
        self.entry = Entry(window,bg="violet")
        self.button =Button(window, text="Преобразовать",bg="lightyellow")
        self.label = Label(window, text="",bg="lightblue")
        self.entry.pack(fill=X)
        self.button.pack(fill=X)
        self.label.pack(fill=X)
    def sort_ascending(self):
        data = self.entry.get().split()
        data_list=list(map(int,data))
        data_list.sort()
        self.label["text"] = data_list

    def sort_descending(self):
        data = self.entry.get().split()
        data_list = list(map(int, data))
        data_list.sort(reverse=True)
        self.label["text"] = data_list

    def shuffle_data(self):
        data = self.entry.get().split()
        random.shuffle(data)
        self.label["text"] = ' '.join(data)

    def process_input(self,type):
        if type=='up':
            self.button["command"]=self.sort_ascending
        if type=='down':
            self.button["command"]=self.sort_descending
        if type=='shuffle':
            self.button["command"]=self.shuffle_data

widget1 = Group_Widgets(window)
widget2 = Group_Widgets(window)
widget3 = Group_Widgets(window)

widget1.process_input("up")
widget2.process_input("down")
widget3.process_input("shuffle")

window.mainloop()
