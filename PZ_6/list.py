"""
Дан список размера N и целые числа K и L (1 < K < L < N). Найти сумму всех
элементов списка, кроме элементов с номерами от K до L включительно.
"""

len_list = int(input('Введите длину списка N: '))
k, l = int(input('Введите K: ')), int(input('Введите L: '))

if 1 < k < l < len_list:
    my_list = list()
    list_not_KL = list()

    for i in range(1, len_list+1):
        my_list.append(i)

        if k <= i <= l:
            continue

        list_not_KL.append(i)

    print(f'Ваш созданный список с целыми числами K({k}), L({l}) заданной длиной N({len_list}): {my_list}\nСумма вашего списка не учитывая числа K и L: {sum(list_not_KL)}')
else:
    print('Вы ввели что-то не по условию, удостоверьтесь что 1 < K < L < N или число длины целое положительное!)')
