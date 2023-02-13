#!/usr/bin/python3
""" Write the class Rectangle that inherits from Base: """
from models.base import Base


class Rectangle(Base):
    """ Class constructor: """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """ Private instance attributes,\
        each with its own public getter and setter: """
    """ getter """
    @property
    def width(self):
        return self.__width

    """ setter """
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    """ getter """
    @property
    def height(self):
        return self.__height

    """ setter """
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """ getter """
    @property
    def x(self):
        return self.__x

    """ setter """
    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """ getter """
    @property
    def y(self):
        return self.__y

    """ setter """
    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """ public methods: """
    def area(self):
        """ return a area """
        return self.width * self.height

    """ public method  """
    def display(self):
        """ t prints in stdout the Rectangle """
        for i in range(self.y):
            print()
        for j in range(self.height):
            print(' ' * self.x + '#' * self.width)

    """ method  """
    def __str__(self):
        """  method so that it returns """
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} \
- {self.width}/{self.height}")

    """ public method """
    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute whit args"""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
        for key, value in kwargs.items():
            setattr(self, key, value)
