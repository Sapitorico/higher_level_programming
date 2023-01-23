#!/usr/bin/python3


def multiple_returns(sentence):
    if not sentence:
        tuple_1 = (0, None)
        return tuple_1
    tuple_1 = (len(sentence), sentence[0])
    return tuple_1
