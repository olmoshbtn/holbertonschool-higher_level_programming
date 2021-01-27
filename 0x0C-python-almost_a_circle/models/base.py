#!/usr/bin/python3
"""Module with the 'Base' class"""

import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns a JSON string that represent a list of dictionaries"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a JSON representation of list_objs to <class-name>.json"""
        with open("{}.json".format(cls.__name__), 'w') as l_o_file:
                if list_objs:
                    l_o_file.write(cls.to_json_string(
                        [obj.to_dictionary() for obj in list_objs]))
                else:
                    l_o_file.write("[]")

    @classmethod
    def create(cls, **dictionary):
        """Returns a new instance of 'class' with its attributes set"""
        if dictionary and dictionary != {}:
            if cls.__name__ is "Rectangle":
                dummy = cls(1, 1)
            elif cls.__name__ is "Square":
                dummy = cls(1)
            cls.update(dummy, **dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Load the objects defined in the JSON file <class-name>.json"""
        try:
            with open("{}.json".format(cls.__name__), 'r') as ifile:
                return [cls.create(**obj)
                        for obj in cls.from_json_string(ifile.read())]
        except FileNotFoundError:
            return []
