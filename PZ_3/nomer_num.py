try:
    num1, num2 = int(input('Введите первое число: ')), int(input('Введите второе число: '))

    if num1 < num2:
        print(f'Меньшее число: {num1}')
    elif num1 > num2:
        print(f'Меньшее число: {num2}')
    else:
        print(f'Числа {num1} и {num2} равны!')
        
except:
    print('Что-то пошло не так!')    