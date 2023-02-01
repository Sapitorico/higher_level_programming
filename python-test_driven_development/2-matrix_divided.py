#!/usr/bin/python3



def matrix_divided(matrix, div):
    if not all([isinstance(row, list) for row in matrix]):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[0])):
    #         matrix[i][j] = round(matrix[i][j]/div, 2)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all([len(matrix[0]) == len(row) for row in matrix]):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(num/div, 2) for num in row] for row in matrix]
