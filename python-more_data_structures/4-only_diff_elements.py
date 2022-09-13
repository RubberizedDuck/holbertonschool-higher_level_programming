#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    result = [
        element for element in (
            set_1 | set_2
        )
        if element in set_1 and element not in set_2
        or element in set_2 and element not in set_1
    ]

    return result
