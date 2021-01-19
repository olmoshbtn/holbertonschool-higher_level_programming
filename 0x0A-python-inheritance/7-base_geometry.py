#!/usr/bin/python3
"""Module with BaseGeometry class"""


class BaseGeometry():
    """Class with atribute public area"""
    def area(self):
        """Raise an exception when is called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that 'value' is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
