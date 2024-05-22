"""
 Дано целое число (N > 0). Если оно является степенью числа 3, то вывести TRUE,
 если не является — вывести FALSE.
"""


def delitel_three(num):
    if num <= 0:
        return False
    while num % 3 == 0:
        num /= 3
    return num == 1


print(delitel_three(int(input("Введите число: "))))
