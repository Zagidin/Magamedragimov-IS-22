def summ_namber(number1, number2):
    contenner = 0
    
    for i in range(number1, number2+1):
        contenner += i
    
    return contenner

number1 = int(input('Введите начало числового ряда: '))
number2 = int(input('Введите конец числового ряда: '))

print(f'Результат суммирования числового ряда: {summ_namber(number1, number2)}')