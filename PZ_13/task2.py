"""
В квадратной матрице элементы на главной диагонали увеличить в 2 раза.
"""

matrix = [
    [i for i in range(4)],
    [i for i in range(1, 5)],
    [i for i in range(2, 6)],
    [i for i in range(3, 7)]
]

print("\nКвадратная матрица:")

for row in matrix:
    print('  ', *row)

for matrix_diagonal in range(len(matrix)):
    matrix[matrix_diagonal][matrix_diagonal] *= 2

print("\nУвеличили элементы по диагонали в 2 раза:")

for two_matrix_diagonal in matrix:
    print('  ', *two_matrix_diagonal)

