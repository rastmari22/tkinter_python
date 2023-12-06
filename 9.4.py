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
mainmenu=Menu(window)

options_menu=Menu(mainmenu,tearoff=0)
options_menu.add_command(label="Открыть", command=insertText)
options_menu.add_separator()
options_menu.add_command(label="Сохранить", command=extractText)

mainmenu.add_cascade(label="Опции", menu=options_menu)
mainmenu.add_command(label="Очистить", command=clearText)

window.config(menu=mainmenu)

text = Text(window, wrap="word")
text.pack()

window.mainloop()