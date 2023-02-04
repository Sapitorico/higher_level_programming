#!/usr/bin/python3
""" function that divide elements to matrix """


def matrix_divided(matrix, div):
    """ matrix must be a list of lists of integers or floats, """
    if not all(isinstance(matrix, list) for index in matrix):
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    if not all(isinstance(j, (int, float)) for row in matrix for j in row):
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    """ Each row of the matrix must be of the same size """
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("Each row of the matrix must have the same size")
    """ div must be a number (integer or float) """
    if not isinstance(div, (int, float)):
        raise ValueError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    """ return All elements of the matrix should be \
        divided by div, rounded to 2 decimal places """
    return [[round(num/div, 2) for num in row] for row in matrix]
