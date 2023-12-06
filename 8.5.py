import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb

window = tk.Tk()
window.title("Редактор файлов")
window.configure(background="orange")

label_entry_frame=tk.Frame(window)
label_name = tk.Label(label_entry_frame, text="Введите название файла: ")
label_name.pack(side=tk.LEFT)
entry = tk.Entry(label_entry_frame)
entry.pack(side=tk.LEFT)
label_entry_frame.pack(fill=tk.X)


text_scroll_frame=tk.Frame(window)
text=tk.Text(text_scroll_frame,width=32,height=15,bg='violet',wrap=tk.WORD)
text.pack(side=tk.LEFT)
scroll=tk.Scrollbar(text_scroll_frame,orient=tk.VERTICAL,command=text.yview)
scroll.pack(side=tk.RIGHT,fill=tk.Y)
text.config(yscrollcommand=scroll.set)
text_scroll_frame.pack(fill=tk.X)

def open_file():
    try:
        file_name=entry.get()
        with open(file_name) as fn:
            t = fn.read()
            text.insert(1.0, t)
    except FileNotFoundError as e:
        mb.showerror(title="Ошибка", message=f"Файл не найден")
        # print(f"Произошла ошибка: {e}")

def save_file():
    file_name = entry.get()
    with open(file_name,"w") as fn:
        t = text.get(1.0,tk.END)
        fn.write(t)
def clear_text():
    text.delete(1.0,tk.END)
    entry.delete(0,tk.END)


button_frame=tk.Frame(window,bg="orange")

open_button = tk.Button(button_frame, text="Открыть", command=open_file)
open_button.pack(side=tk.LEFT, padx=5)
save_button = tk.Button(button_frame, text="Сохранить", command=save_file)
save_button.pack(side=tk.LEFT, padx=5)
clear_button = tk.Button(button_frame, text="Очистить", command=clear_text)
clear_button.pack(side=tk.LEFT, padx=5)

button_frame.pack(side=tk.BOTTOM,pady=10)


window.mainloop()