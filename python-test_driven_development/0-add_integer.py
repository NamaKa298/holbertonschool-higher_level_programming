#!/usr/bin/python3
'''0. Integers addition'''


def add_integer(a, b=98):
    '''Function that adds two integers'''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    return int(a + b)
