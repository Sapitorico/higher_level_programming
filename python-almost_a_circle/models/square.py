#!/usr/bin/python3
""" Write the class Square that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class constructor """
    def __init__(self, size, x=0, y=0, id=None):
        """ validation must inherit from Rectangle """
        super().__init__(size, size, x, y, id)
        self.x = x
        self.y = y
        self.id = id

    def __str__(self):
        """ The overloading """
        return "[Square] ({}) {}/{} - {}"\
.format(self.id, self.x, self.y, self.size)

    """ getter """
    @property
    def size(self):
        """ dqwdqw """
        return self.width

    """ setter """
    @size.setter
    def size(self, value):
        """ sdwqdqw """
        self.width = value
        self.height = value

    """ method """
    def update(self, *args, **kwargs):
        """ dwdqwd """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        for key, value in kwargs.items():
            setattr(self, key, value)
