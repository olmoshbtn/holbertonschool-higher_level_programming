#!/usr/bin/python3
"""Module that contains 'Rectangle(Base)' class"""


from models.base import Base


class Rectangle(Base):
    """Representation of a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get private instance of attribute 'width'"""
        return self.__width

    @property
    def height(self):
        """Get private instance of attribute 'height'"""
        return self.__height

    @property
    def x(self):
        """Get private instance of attribute 'x"""
        return self.__x

    @property
    def y(self):
        """Get private instance of attribute 'y'"""
        return self.__y

    @width.setter
    def width(self, width):
        """Set private instance of attribute 'width'"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """Set private instance of attribute 'height'"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """Set private instance of attribute 'x'"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """Set private instance of attribute 'y'"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """Print a visual representation of a rectangle with char '#'"""
        print("\n" * self.__y, end="")
        print("\n".join([" " * self.__x + "#" * self.__width] * self.__height))

    def __str__(self):
        """Representation of a rectangle by a data string"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.__x,
            self.__y,
            self.__width,
            self.__height
        )

    def update(self, *args, **kwargs):
        """Public method that assigns a key/value argument to attributes"""
        if len(args):
            for index, value in enumerate(args):
                if index == 0:
                    self.id = value
                elif index == 1:
                    self.width = value
                elif index == 2:
                    self.height = value
                elif index == 3:
                    self.x = value
                elif index == 4:
                    self.y = value
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Dictionary representation of a Rectangle"""
        dic_rect = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
        return dic_rect
