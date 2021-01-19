#!/usr/bin/python3
"""Module function inherits_from"""


def inherits_from(obj, a_class):
    """Returns True if obj is a subclass of a_class, otherwise False"""
    return (isinstance(obj, a_class) and type(obj) != a_class)
