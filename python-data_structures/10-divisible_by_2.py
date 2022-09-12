#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    new_list = []
    for value in my_list:
        if value % 2 == 0:
            new_list.insert(value, True)
        else:
            new_list.insert(value, False)
    return new_list
