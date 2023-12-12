len_list = int(input('Введите длину списка N: '))
[k, l] = int(input('Введите K: ')), int(input('Введите L: '))

if 1 < k < l < len_list:

    my_list = list()
    list_not_KL = list()
    for i in range(1, len_list+1):
        my_list.append(i)

        if i == k or i == l:
            continue

        list_not_KL.append(i)

    print(f'Ваш созданный список с целыми числами K({k}), L({l}) заданной длиной N({len_list}): {my_list}\nСумма вашего списка не учитывая числа K и L: {list_not_KL}')
else:
    print('Вы ввели что-то не по условию, удостоверьтесь что 1<K<L<N или число длины целое положительное!)')
