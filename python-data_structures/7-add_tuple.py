#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    for elem in range(2):
        if elem >= len(tuple_a):
            val_a = 0
        else:
            val_a = tuple_a[elem]

        if elem >= len(tuple_b):
            val_b = 0
        else:
            val_b = tuple_b[elem]

        if elem == 0:
            new_tuple = (val_a + val_b)
        else:
            new_tuple = (new_tuple, (val_a + val_b))

    return new_tuple
