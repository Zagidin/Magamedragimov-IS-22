"""
 Дано целое число (N > 0). Если оно является степенью числа 3, то вывести TRUE,
 если не является — вывести FALSE.
"""

from tkinter import *


def is_power_of_three(num):
    if num <= 0:
        return False
    while num % 3 == 0:
        num /= 3
    return num == 1


def check_power_of_three():
    num = int(entry.get())
    result = is_power_of_three(num)
    if result:      
        label_print.config(text="TRUE")
    else:
        label_print.config(text="FALSE")


root = Tk()
root.title("Практическая работа № 4")

label1 = Label(root, text="Канкулятор вычисления:\nЯвляется ли число степенью числа 3")
label1.pack(pady=10)

entry = Entry(root, width=10)
entry.pack(pady=10)

check_button = Button(root, text="Проверить", command=check_power_of_three)
check_button.pack(pady=5)

label_print = Label(root, text="")
label_print.pack(pady=10)

root.mainloop()
