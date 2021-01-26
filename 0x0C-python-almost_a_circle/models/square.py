#!/usr/bin/python3
"""Module that contains 'Square(Rectangle)' class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Representation of a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializates the square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get private instance of 'size'"""
        return self.width

    @size.setter
    def size(self, value):
        """Set private instance of attribute 'size'"""
        self.width = value
        self.height = value

    def __str__(self):
        """Representation of a square by a data string"""
        return "[{type}] ({id}) {x}/{y} - {size}".format(
            type=self.__class__.__name__,
            id=self.id,
            x=self.x,
            y=self.y,
            size=self.width
        )

    def update(self, *args, **kwargs):
        """Public method that assigns a key/value argument to attributes"""
        if len(args):
            for index, value in enumerate(args):
                if index == 0:
                    self.id = value
                elif index == 1:
                    self.size = value
                elif index == 2:
                    self.x = value
                elif index == 3:
                    self.y = value
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Dictionary representation of a Square"""
        dic_square = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return dic_square
