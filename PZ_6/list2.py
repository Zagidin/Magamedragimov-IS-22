"""
Дан целочисленный список размера N. Если он является перестановкой, то есть
содержит все числа от 1 до N, то вывести 0; в противном случае вывести номер
первого недопустимого элемента.
"""

len_list = int(input('Введите размер списка N: '))

my_list_equally = list()
my_list = list()
for i in range(1, len_list+1):
    num = int(input(f'Введите {i} число списка: '))
    my_list.append(num)
    my_list_equally.append(i)

if my_list_equally == my_list:
    print(0)
else:
    counter = ''
    for i in range(len_list):
        if my_list[i] != my_list_equally[i]:
            counter += str(my_list[i]) + ' '

    # Числа преобразуем в список
    new_list = [int(num) for num in counter.split()]
    
    print(f'\nОтличающийся элемент из вашего списка {my_list} --> {counter}\n\t\t   Она не совпадает с {my_list_equally}\n\nПервый недопустимый элемент --> {new_list[0]}\n')
