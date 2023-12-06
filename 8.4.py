import tkinter as tk
from tkinter import messagebox as mb

window = tk.Tk()
window.title("Суммирование чисел")
window.geometry("500x200")
def getdata():
    try:
        t=input_entry.get()
        if not t:
            raise ValueError
        if not (t.lstrip('-').replace('.', '', 1).isdigit() or t.replace('.', '', 1).isdigit()):
            raise TypeError
        result_sum.append(float(t))
        output_entry.delete(0, 'end')
        output_entry.insert(0,result_sum)
    except TypeError:
        mb.showerror(title="неверный ввод", message="Введите число")
    except ValueError:
        mb.showinfo(title="Ошибка",message="Вы не ввели значение")

    input_entry.delete(0,'end')
def getresult():
    res=sum(result_sum)
    mb.showinfo(title="Зезультат", message=f"Итоговая сумма: {res} ")
    # output_entry.delete(0,'end')
    # output_entry.insert(0,res)

def clearall():
    input_entry.delete(0, 'end')
    output_entry.delete(0, 'end')
    result_sum = []
def destroywnd():
    window.destroy()

input_frame=tk.Frame(window)
input_label=tk.Label(input_frame,text="Введите число: ",width=25)
input_entry=tk.Entry(input_frame)
input_button=tk.Button(input_frame,text="Ввод",width=10,command=getdata)

output_frame=tk.Frame(window)
output_label=tk.Label(output_frame,text="Вы ввели числа:",width=25)
output_entry=tk.Entry(output_frame)
output_button=tk.Button(output_frame,text="Результат",width=10,command=getresult)


clear_button=tk.Button(window,text="Очистка данных",command=clearall)
exit_button=tk.Button(window,text="Выход из программы",command=destroywnd)
result_sum=[]

input_label.pack(side="left")
input_entry.pack(side="left")
input_button.pack(side="left",padx=20,pady=10)


output_label.pack(side="left")
output_entry.pack(side="left")
output_button.pack(side="left",padx=20,pady=10)

input_frame.pack(side="top")
output_frame.pack(side="top")

exit_button.pack(side="bottom",pady=10)
clear_button.pack(side="bottom")


window.mainloop()