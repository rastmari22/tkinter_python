from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

def insertText():
    try:
        file_name = fd.askopenfilename()
        with open(file_name, 'r') as fn:
            info = fn.read()
            text.insert(1.0, info)
    except FileNotFoundError:
        mb.showerror("Ошибка", "Файл не загружен")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка: {e}")

def extractText():
    file_name=fd.asksaveasfilename(filetypes=(("TXT files","*.txt"),
                                              ("HTML files","*.html"),
                                              ("All files","*.*")))
    try:
        with open(file_name,"w") as fn:
            info=text.get(1.0,END)
            fn.write(info)
    except FileNotFoundError:
        mb.showerror("Ошибка", "Файл не сохранен")
def clearText():
    confirm = mb.askyesno("Подтверждение", "Вы уверены, что хотите удалить всю информацию из текстового поля?")
    if confirm:
        text.delete(1.0, END)

window=Tk()
window.title("Редактор файлов")
# text=Text(width=50,height=25)
# text.grid(columnspan=2)

text = Text(window, wrap="word")
text.grid(columnspan=2)

open_button = Button( text="Открыть", command=insertText)
open_button.grid(row=1, column=0,sticky=E)
save_button = Button( text="Сохранить", command=extractText)
save_button.grid(row=1, column=1,sticky=W)
clear_button = Button(text="Очистить", command=clearText)
clear_button.grid(row=2, columnspan=2)

window.mainloop()