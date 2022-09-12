#!/usr/bin/python3


def max_integer(my_list=[]):
    list_len = len(my_list)
    if list_len == 0:
        return None

    largest_num = my_list[0]
    for value in my_list:
        if value > largest_num:
            largest_num = value

    return largest_num
