"""
В матрице найти минимальный элемент в предпоследней строке.
"""

matrix = [
    [i for i in range(4)],
    [i for i in range(1, 5)],
    [i for i in range(2, 6)],
    [i for i in range(3, 7)]
]

print("\nМатрица 4х4:")

for matrix_num in matrix:
    print(" ", *matrix_num)

print(f"Минимальное число из предпоследней строки: {min(matrix[2])}")
