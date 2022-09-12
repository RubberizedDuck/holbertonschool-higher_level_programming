#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    count = len(my_list)
    if idx < 0 or idx >= count:
        return my_list

    new_list[idx] = element
    return new_list
