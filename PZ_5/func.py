"""
Описать функцию Powerl(A, B) вещественного типа, находящую величину AB по
формуле AB=exp(B*ln(A)) (параметры A и B -- вещественные). В случае нулевого
или отрицательного параметра A фунция возращает 0. С помощью этой функции
найти степени A^P, B^P, C^P, если даны числа P, A, B, C

"""
from math import exp, log


def powerl(a, b):

    if a <= 0:
        return 0
    else:
        return exp(b * log(a))


num1, num2, num3 = float(input('Введите число A: ')), float(input('Введите число B: ')), int(input('Введите число С: '))
stepen = int(input('Введите степень(P): '))
print(f'Результат первого условия: {powerl(num1, num2)}\n\nРезультат второго условия:\n\t{powerl(num1, stepen)}\n\t{powerl(num2, stepen)}\n\t{powerl(num3, stepen)}')
