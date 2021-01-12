#!/usr/bin/python3
"""Module that provides a class 'LockedClass' with no class or object attribute
"""


class LockedClass:
    """'LockedClass' prevents the user from dynamically creating new instance
    attributes, except if the instance attribute 'first_name' is called"""
    __slots__ = ['first_name']
