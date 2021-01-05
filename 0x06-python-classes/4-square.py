#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Class Square that defines a square
"""


class Square:
    """Definition of a Square
    """
    def __init__(self, size=0):
        """Instantiate a Square
        """
        self.size = size

    @property
    def size(self):
        """
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Current square area
        """
        return self.__size ** 2
