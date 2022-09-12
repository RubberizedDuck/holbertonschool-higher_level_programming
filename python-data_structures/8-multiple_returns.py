#!/usr/bin/python3


def multiple_returns(sentence):
    string_len = len(sentence)
    if string_len == 0:
        return (0, None)

    return (string_len, sentence[0])
