#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for index1 in range(len(matrix)):
        for index2 in range(len(matrix[index1])):
            print("{:d}".format(matrix[index1][index2]), end=" ")
        print("")
