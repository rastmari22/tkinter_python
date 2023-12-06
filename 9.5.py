from tkinter import *
from tkinter import messagebox as mb

window = Tk()
window.title("Копирование")
window.configure(bg='lightgray')
window.geometry('400x300')

entry_frame = Frame(window,bg='lightgray')
listbox_label_frame = Frame(window,bg='lightgray')

entry = Entry(window, bg="white")
entry.pack(pady=10)

listbox = Listbox(listbox_label_frame, bg="white", width=30, height=10)
label = Label(listbox_label_frame, width=15, padx=10,bg="lightblue")

listbox.pack(side=LEFT,padx=10)
label.pack(side=LEFT)
listbox_label_frame.pack()


def copytext(event):
    try:
        txt = event.widget.get()
        if not txt:
            raise Exception
        listbox.insert(END, txt)
    except Exception:
        mb.showerror("Ошибка", "Вы ничего не ввели")


def txt_to_label(event):
    try:
        n = event.widget.curselection()
        if not n:
            raise Exception
        txt = event.widget.get(n)
        label.config(text=txt)
    except Exception:
        mb.showerror("Ошибка", "Вы ничего не выбрали")


entry.bind("<Return>", copytext)
listbox.bind("<Double-Button-1>", txt_to_label)
window.mainloop()
