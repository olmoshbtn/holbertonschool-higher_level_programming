#!/usr/bin/python3
"""Module with BaseGeometry class"""


class BaseGeometry():
    """Class with atribute public area"""
    pass
    """Raise an exception when is called"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that 'value' is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """"Representation of a rectangule"""
    def __init__(self, width, height):
        """Instantiation of a rectangle"""
        self.integer_validator("with", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Print and return rectangle description"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
