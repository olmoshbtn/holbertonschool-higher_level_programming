#!/usr/bin/python3
"""Module with BaseGeometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """"Representation of a rectangule"""
    def __init__(self, width, height):
        """Instantiation of a rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
