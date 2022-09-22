#!/usr/bin/python3
"""
Module matrix_divided
Divides each element of a matrix of numbers by a number
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix (list of list)
    with the result of the division of matrix by div
    rounded to 2 decimal places.
    """

    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if len(row) == 0:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for num in row:
            if type(num) is not int and type(num) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    row_length = []
    for row in matrix:
        row_length.append(len(row))
    if not all(element == row_length[0] for element in row_length):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
