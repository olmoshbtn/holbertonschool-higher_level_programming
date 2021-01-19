#!/usr/bin/python3
"""Takes information about the methods and attributes of the objects"""


def lookup(obj):
        """returns a list of available attributes and methods of an object"""
        return dir(obj)
