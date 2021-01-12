#!/usr/bin/python3
"""Module that define a 'Rectangle' Class to represent a rectangle"""


class Rectangle:
    """Definition to represent the 'Rectangle' Class"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Instantiate a rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Prints a string message when the instace has been deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """'getter' for the width of the private instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """'setter' for the private instance attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """'getter' for the height of the private instance attibute"""
        return self.__height

    @height.setter
    def height(self, value):
        """'setter' for the private instance attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method that returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Public instance method that returns the rectangle perimeter"""
        if self.__width and self.__height:
            return 2 * (self.__width + self.__height)
        return 0

    def __str__(self):
        """Returns printable string representation of the rectangle"""
        if self.__height and self.__width:
            return '\n'.join(
                [str(self.print_symbol) * self.__width] * self.__height)
        return ""

    def __repr__(self):
        """Returns a string representation of the rectangle for reproduction"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
