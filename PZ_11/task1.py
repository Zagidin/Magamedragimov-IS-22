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
 
list_one = [randint(-10, 10) for _ in range(10)] 
list_two = [randint(-10, 10) for _ in range(10)]
 
with open('PZ_11/fail_1.txt', 'w') as fail_1: 
    fail_1.write(f"Первый список:  {str(list_one)}")

with open('PZ_11/fail_2.txt', 'w') as fail_2:
    fail_2.write(f"Второй список:  {str(list_two)}")
    
    
with open('PZ_11/all_file.txt', 'w') as all_file:
    negative_list = []
    positive_list = []
    
    for el in list_one:
        if el < 0:
            negative_list.append(el)
        else:
            continue
    for el in list_two:
        if el > 0:
            positive_list.append(el)
        else:
            continue
    
    all_file.write(
        f"Содержимое первого файла: {list_one}\n"
        f"Отрицательные элементы: {negative_list}\n"
        f"Количество отрицательных элементов: {len(negative_list)}\n"
        f"Среднее арифметическое: {sum(list_one) / len(list_one)}\n\n"
        f"Содержимое второго файла: {list_two}\n"
        f"Положительные элементы: {positive_list}\n"
        f"Количество положитльных элементов: {len(positive_list)}\n"
        f"Сумма положительных элементов: {sum(positive_list)}"
    )