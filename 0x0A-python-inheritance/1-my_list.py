#!/usr/bin/python3
"""Module MyList class with all the elements of the list of type int"""


class MyList(list):
    """subclass of list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the list in ascending order"""
        print(sorted(self))
