# Дано целое число N (>0). Если оно является степенью числа 3, то вывести TRUE,
# если не является — вывести FALSE.
from math import log

number = int(input('Введите целое число, больше 0: '))

if number <= 0:
    print(False, 'Так-как, вы ввели отрицательное число!')
else:
    number_ln = log(number, 3)

    num = int(str(number_ln).split('.')[1])

    if num == 0:
        print(True)
    else:
        print(False)
