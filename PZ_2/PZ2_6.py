# Дано L растояние в сантиметрах. Используя операцию деления нацело, найти количество метров
try:

    L = int(input("Введите, сколько сантиметров --> "))
    print("\tДелаем деление --> ", L, ':100', sep='')
    res = L // 100
    if L >= 0:
        print("\t Ответ => ", res, " метров", sep='')
    else:
        print("Вы написали отрицательное число! Попробуйте ещё раз.")

except:
    print("Вы ввели что-то непонятное, попробуйте написать положительное число!)")
