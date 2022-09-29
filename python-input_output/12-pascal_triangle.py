#!/usr/bin/python3
"""
This module is the pascal challenge
"""


def pascal_triangle(n):
    """ function to return a pascal triangle """
    pascal_list = []
    if n <= 0:
        return pascal_list

    for row in range(n):
        if row == 0 or row == 1:
            pascal_list.append([1 for c in range(0, row + 1)])
        else:
            line = []
            for column in range(0, len(pascal_list[row - 1]) + 1):
                if column == 0 or column == len(pascal_list[row - 1]):
                    line.append(1)
                else:
                    line.append(pascal_list[row - 1][column - 1] +
                                pascal_list[row - 1][column])
            pascal_list.append(line)

    return pascal_list
