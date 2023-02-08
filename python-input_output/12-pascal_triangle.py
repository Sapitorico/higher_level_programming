#!/usr/bin/python3
""" Create a function def pascal_triangle """


def pascal_triangle(n):
    """ Create a function def pascal_triangle """
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    res = [[1]]
    for i in range(2, n + 1):
        temp = [1]
        for j in range(1, i - 1):
            temp.append(res[i - 2][j - 1] + res[i - 2][j])
        temp.append(1)
        res.append(temp)
    return res
