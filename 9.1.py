from tkinter import *
from tkinter import messagebox as mb

window = Tk()

listbox_frame = Frame(window)
entry_btn_frame = Frame(window)
listbox = Listbox(listbox_frame, width=50, selectmode=MULTIPLE)
scroll = Scrollbar(listbox_frame, orient=VERTICAL, command=listbox.yview)

items_for_label = [
    "Python разработка веб-приложений",
    "Java объектно-ориентированное программирование",
    "JavaScript клиентская разработка",
    "SQL управление базами данных",
    "HTML/CSS веб-дизайн",
    "Git система контроля версий",
]

for i in items_for_label:
    listbox.insert(END, i)


def to_listbox():
    try:
        tl = entry.get()
        if tl:
            listbox.insert(END, tl)
            entry.delete(0, END)
        else:
            raise Exception
    except Exception:
        mb.showerror("Ошибка", "Вы пытаетесь добавить пустую строку")


def delete_item():
    try:
        nums = listbox.curselection()
        if nums:
            nums = list(nums)
            nums.reverse()
            for i in nums:
                listbox.delete(i)
        else:
            raise Exception
    except Exception:
        mb.showerror("Ошибка", "Не выбран элемент для удаления")


def save_inf():
    try:
        nums = listbox.curselection()
        if nums:
            confirm = mb.askyesno("Подтверждение", "Вы уверены?")
            if confirm:
                liststr = "\n".join([listbox.get(i) for i in nums])
                with open("newtext.txt", "w") as fn:
                    fn.write(liststr)
        else:
            raise Exception
    except Exception:
        mb.showerror("Ошибка:", "Нет выбранных элементов для сохранения")


listbox.config(yscrollcommand=scroll.set)
entry = Entry(entry_btn_frame)
btn1 = Button(entry_btn_frame, command=to_listbox, text="Добавить", width=10)
btn2 = Button(entry_btn_frame, command=delete_item, text="Удалить", width=10)
btn3 = Button(entry_btn_frame, command=save_inf, text="Сохранить", width=10)

listbox.pack(
    side=LEFT,
)
scroll.pack(side=LEFT, fill=Y)
listbox_frame.pack(side=LEFT, padx=30, pady=30)
entry.pack()
btn1.pack()
btn2.pack()
btn3.pack()
entry_btn_frame.pack(side=LEFT, padx=30, pady=30)

window.mainloop()
