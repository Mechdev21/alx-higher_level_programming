#!/usr/bin/python3
"""
A function that divides all element of a matrix
"""


def matrix_divided(matrix, div):
    """a function that divides a matrix
    Args:
        Matrix: given matrix to be divide
        div: number that divides a matrix
    Returns:
        list of matrix
    """
    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if len(i) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    ma_row = []
    for row in matrix:
        ma_row.append(len(row))
    if not all(value == ma_row[0] for value in ma_row):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError('division by zero')

    result = [[round(x / div, 2) for x in row] for row in matrix]
    return (result)

