# Напишите функцию для транспонирования матрицы

matrix_1 = [[1, 2], [4, 5]]

def matrix_transgoration(matrix):
    transposed_matrix = [[0 for i in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix

print(matrix_1)
print(matrix_transgoration(matrix_1))