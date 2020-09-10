#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix[:]
    for i in range(len(new_matrix)):
            new_matrix[i] = list(map(square_value, new_matrix[i]))
    return new_matrix


def square_value(row):
    return row ** 2
