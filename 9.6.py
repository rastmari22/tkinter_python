from tkinter import *
from tkinter import messagebox as mb

class changedText:
    def __init__(self,wnd):
        self.window=wnd
        self.window.title("Изменение размеров текстового поля")
        self.set_frame=Frame(window)
        self.set_frame.pack()

        self.create_input()
        # self.create_btn()
        self.set_text_size()
    def create_input(self):
        Label(self.set_frame, text="Ширина:").grid(row=0, column=0, padx=5, pady=5)
        Label(self.set_frame, text="Высота:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_x = Entry(self.set_frame)
        self.entry_y = Entry(self.set_frame)

        self.entry_x.bind("<FocusIn>", self.change_entry_color)
        self.entry_x.bind("<FocusOut>", self.restore_entry_color)
        self.entry_y.bind("<FocusOut>", self.restore_entry_color)
        self.entry_y.bind("<FocusIn>", self.change_entry_color)
        self.entry_x.bind('<Return>',self.set_text_width)
        self.entry_y.bind('<Return>',self.set_text_height)
        self.change_button=Button(self.set_frame,width=15,text="Изменить")
        self.change_button.bind('<Button-1>',self.change_text_size)

        self.entry_x.grid(row=0, column=1)
        self.entry_y.grid(row=1, column=1)
        self.change_button.grid(row=0, column=2, rowspan=2, padx=5, pady=5)
    def change_entry_color(self,event):
        event.widget.config(bg="lightgrey")
    def restore_entry_color(self,event):
        event.widget.config(bg="white")
    def set_text_size(self,w=30,h=10):
        # w,h=arg
        self.text=Text(self.window,width=w,height=h)
        self.text.pack()
    def set_text_width(self,event):
        nw = self.entry_x.get()
        self.text.config(width = nw)
        try:
            nh=self.entry_y.get
            self.text.config(height=nh)
        except Exception:
            pass
    def set_text_height(self,event):
        nh = self.entry_y.get()
        self.text.config(height=nh)
        try:
            nw = self.entry_x.get
            self.text.config(width=nw)
        except Exception:
            pass
    def change_text_size(self,event):
        try:
            nw=self.entry_x.get()
            nh=self.entry_y.get()
            self.text.config(height=nh,width=nw)
        except Exception:
            mb.showerror("Ошибка", "Введите все значения")
            self.entry_x.focus_set()
window=Tk()
WND=changedText(window)

window.mainloop()


# set_frame=Frame(window)
# text=Text(window, wrap="word")
# entry_x=Entry(set_frame)
# entry_y=Entry(set_frame)

# def set_text_size(event):
#     text["width"]=entry_x.get()
#     text["height"] = entry_y.get()
# def set_text_width(event):
#     text["width"]=entry_x.get()
# def set_text_height(event):
#     text["height"] = entry_y.get()
# def change_entry_color(event):
#     event.widget.config(bg="lightgrey")
# def restore_entry_color(event):
#     event.widget.config(bg="white")
# change_button=Button(set_frame,width=15)
# Label(set_frame, text="Ширина:").grid(row=0, column=0, padx=5, pady=5)
# Label(set_frame, text="Высота:").grid(row=1, column=0, padx=5, pady=5)
# change_button.bind('<Button-1>',set_text_size)
# entry_x.bind('<Return>',set_text_width)
# entry_y.bind('<Return>',set_text_height)
# entry_x.bind("<FocusIn>", change_entry_color)
# entry_y.bind("<FocusOut>", restore_entry_color)
# entry_y.bind("<FocusIn>", change_entry_color)
# entry_x.bind("<FocusOut>", restore_entry_color)
# entry_x.grid(row=0, column=1)
# entry_y.grid(row=1, column=1)
# change_button.grid(row=0, column=2, rowspan=2, padx=5, pady=5)
#
# set_frame.pack()
# text.pack()