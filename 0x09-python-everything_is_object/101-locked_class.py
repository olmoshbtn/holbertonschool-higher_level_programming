#!/usr/bin/python3


class LockedClass:
    """'LockedClass' prevents the user from dynamically creating new instance
        attributes, except if the instance attribute 'first_name' is called"""
    __slots__ = ['first_name']
