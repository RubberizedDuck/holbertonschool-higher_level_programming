#!/usr/bin/python3

import sys
if __name__ == "__main__":
    argc = len(sys.argv) - 1
    sum_of = 0

    if argc == 0:
        print("{}".format(sum_of))
        exit()

    count = 0
    for args in sys.argv:
        if count != 0:
            sum_of += int(args)
        else:
            count += 1
    print("{}".format(sum_of))
