#!/usr/bin/python3
"""Module provides a
function 'add_integer'
that performs
integer
addition"""


def add_integer(a, b=98):
    """Function that
    return the sum of two
    integers or floats"""
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
