"""
В квадратной матрице элементы на главной диагонали увеличить в 2 раза.
"""

matrix = [[j + 1*i for j in range(4)] for i in range(4)]

print("\nКвадратная матрица:")

for row in matrix:
    print('  ', *row)

# for matrix_diagonal in range(len(matrix)):
#     matrix[matrix_diagonal][matrix_diagonal] *= 2

matrix2 = [[matrix[x_diagonal][y_diagonal] * 2 if x_diagonal == y_diagonal else matrix[x_diagonal][y_diagonal] for x_diagonal in range(len(matrix))] for y_diagonal in range(len(matrix))]

print("\nУвеличили элементы по диагонали в 2 раза:")

for two_matrix_diagonal in matrix2:
    print('  ', *two_matrix_diagonal)
