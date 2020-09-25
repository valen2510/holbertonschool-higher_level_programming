#!/usr/bin/python3
"""Function to divide the elements
    of a matrix, elements of the matrix
    must be integers or floats
"""


def matrix_divided(matrix, div):
    """Divide each and all the elements in a matrix
    wih div. The elements and div should be int or
    float type.
    return new matrix with the results of the division"""
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    for i in range(len(matrix)):
        if type(matrix[i]) is not list or len(matrix[i]) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        if len(matrix[0]) is not len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
