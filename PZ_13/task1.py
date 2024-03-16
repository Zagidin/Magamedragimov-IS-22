"""
В матрице найти минимальный элемент в предпоследней строке.
"""

matrix = [[j + 1 * i for j in range(4)] for i in range(4)]

print("\nМатрица 4х4:")

for matrix_num in matrix:
    print(" ", *matrix_num)

print(f"Минимальное число из предпоследней строки: {min(matrix[len(matrix) - 2])}")
