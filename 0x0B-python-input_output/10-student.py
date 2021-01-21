#!/usr/bin/python3
"""Module Class Student"""


class Student:
    """Definition of student"""
    def __init__(self, first_name, last_name, age):
        """Initializes of student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for at in attrs:
            try:
                new_dict[at] = self.__dict__[at]
            except:
                pass
        return new_dict
