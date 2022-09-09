#!/usr/bin/python3


for alphabet in range(ord('z'), ord('a') - 1, -1):
    if alphabet % 2 == 1:
        alphabet -= 32

    print("{:c}".format(alphabet), end ="")
