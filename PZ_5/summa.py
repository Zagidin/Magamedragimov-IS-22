# Создать функцию, которая выполнит суммирование числового ряда.
def summ_nambers(number1, number2):
    contenner = 0
    # цикл от числа1 до числа2
    for i in range(number1, number2+1):
        contenner += i
    # вернуть мой контенер собраный
    return contenner

number1 = int(input('Введите начало числового ряда: '))
number2 = int(input('Введите конец числового ряда: '))

print(f'Результат суммирования числового ряда: {summ_nambers(number1, number2)}')
