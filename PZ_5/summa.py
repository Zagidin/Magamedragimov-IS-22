# Создать функцию, которая выполнит суммирование числового ряда.

def summ_nambers(number1, number2):

    contener = 0
    for i in range(number1, number2+1):
        contener += i

    return contener

number1 = int(input('Введите начало числового ряда: '))
number2 = int(input('Введите конец числового ряда: '))

print(f'Результат суммирования числового ряда: {summ_nambers(number1, number2)}')
