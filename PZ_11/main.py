"""
Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
последовательности из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:

Содержимое первого файла:
Отрицательные элементы.
Количество отрицательных элементов.
Среднее арифметическое.

Содержимое второго файла:
Положительные элементы.
Количество положительных элементов.
Сумма положительных элементов.
"""

from random import randint 
 
numbers = [] 
 
for i in range(10): 
    i = randint(-10, 10) 
    numbers.append(i) 
 
with open('PZ_11/fail_1.txt', 'w') as fail_1: 
     
    num_negative = [] 
 
    for el in numbers: 
        if el < 0: 
            num_negative.append(el) 
        else: 
            continue 
 
    quantity_negative_digit = len(num_negative) 
     
    fail_1.write(f'Negative elements: {str(num_negative)}\nThe number of negative numbers: {quantity_negative_digit}\nthe average value of the numbers: {sum(num_negative) / quantity_negative_digit}') 
 
with open('PZ_11/fail_2.txt', 'w') as fail_2: 
 
    num_positive = [] 
 
    for j in numbers: 
        if j > 0: 
            num_positive.append(j) 
        else: 
            continue 
 
    quantity_positive_digit = len(num_positive) 
     
    fail_2.write(f'Positive elements: {str(num_positive)}\nThe number of positive numbers: {quantity_positive_digit}\nThe sum of positive numbers: {sum(num_positive)}') 
 
print(f"\nВаш список: {numbers}\n")