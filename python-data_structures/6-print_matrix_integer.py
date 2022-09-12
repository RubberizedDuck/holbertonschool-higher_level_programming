#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    print('\n'.join([' '.join(['{:d}'.format(element) for element in row])
                     for row in matrix]))
