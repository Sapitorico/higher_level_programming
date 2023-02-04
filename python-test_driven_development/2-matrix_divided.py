#!/usr/bin/python3
""" function that divide elements to matrix """


def matrix_divided(matrix, div):
    """ matrix must be a list of lists of integers or floats, """
    if not all(isinstance(matrix, list) for index in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(j, (int, float)) for row in matrix for j in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    """ Each row of the matrix must be of the same size """
    if len(matrix[0]) != div:
        raise ValueError("Each row of the matrix must have the same size")
    """ return All elements of the matrix should be divided by div, rounded to 2 decimal places """
    return [[round(num/div, 2) for num in row] for row in matrix]
