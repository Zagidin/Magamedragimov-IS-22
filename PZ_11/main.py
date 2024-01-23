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

negative_elements = [-1, -2, -3, -4, -5]

with open('./PZ_11/sample.txt', 'w') as file_1:
    file_1.write(str(negative_elements))
    
with open('./PZ_11/sample.txt', 'r') as file_1:
    len_content_number = file_1.readline()
    
len_content_number = len_content_number.split()
len_content_number = len_content_number.replace('[', '')

for i in range(len(len_content_number)):
    len_content_number[i] = int(len_content_number[i])

# quantity_negative = 0
# for i in range(len(len_content_number)):
#     if len_content_number[i] < 0:
#         quantity_negative += 1

print(len_content_number)
