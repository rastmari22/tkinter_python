from tkinter import *
from tkinter import messagebox as mb
from collections import Counter

my_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
element_count = Counter(my_list)
print(element_count)


window = Tk()

listbox_frame = Frame(window)
listbox2_frame = Frame(window)
entry_btn_frame = Frame(window)
listbox = Listbox(listbox_frame, width=50, selectmode=MULTIPLE)
scroll = Scrollbar(listbox_frame, orient=VERTICAL, command=listbox.yview)
check_listbox = Listbox(listbox2_frame, width=50, selectmode=MULTIPLE)
items_for_label = [
    "Learn Python the Hard Way",
    "Eloquent JavaScript",
    "Head First Java",
    "Ruby on Rails Tutorial",
    "Learning PHP, MySQL, JavaScript, and CSS",
    "C++ Primer",
    "HTML and CSS: Design and Build Websites",
    "Learning Perl",
    "Scala for the Impatient",
    "Swift for Beginners",
]

for i in items_for_label:
    listbox.insert(END, i)


def to_listbox():
    try:
        tl = listbox.curselection()
        if tl:
            for i in tl:
                check_listbox.insert(END, listbox.get(i))
        else:
            raise Exception
    except Exception:
        mb.showerror("Ошибка", "Выберите товар")


def delete_item():
    try:
        nums = check_listbox.curselection()
        if nums:
            nums = list(nums)
            nums.reverse()
            for i in nums:
                check_listbox.delete(i)
        else:
            raise Exception
    except Exception:
        mb.showerror("Ошибка", "Не выбран элемент для удаления")


def save_inf():
    try:
        nums = check_listbox.curselection()
        if nums:
            confirm = mb.askyesno("Подтверждение", "Вы уверены?")
            if confirm:
                liststr=["аш заказ:"]
                element_count = Counter([check_listbox.get(i) for i in nums])
                for elem, count in element_count.items():
                    newstr=f"{elem} - {count} шт."
                    liststr.append(newstr)
                liststrr = "\n".join(liststr)

                with open("buy.txt", "w") as fn:
                    fn.write(liststrr)
        else:
            raise Exception
    except Exception:
        mb.showerror("Ошибка:", "Нет выбранных элементов для сохранения")


listbox.config(yscrollcommand=scroll.set)

btn1 = Button(entry_btn_frame, command=to_listbox, text="Добавить в корзину", width=20)
btn2 = Button(entry_btn_frame, command=delete_item, text="Удалить из корзины", width=20)
btn3 = Button(entry_btn_frame, command=save_inf, text="Оформить заказ", width=20)

listbox.pack(
    side=LEFT,
)
check_listbox.pack(
    side=LEFT,
)
scroll.pack(side=LEFT, fill=Y)
listbox_frame.pack(side=LEFT, padx=30, pady=30)

btn1.pack()
btn2.pack()
btn3.pack()
entry_btn_frame.pack(side=LEFT, padx=30, pady=30)
listbox2_frame.pack(side=LEFT, padx=30, pady=30)

window.mainloop()
