#!/usr/bin/python3
"""Define a class Square that inherits\
from Rectangle (9-rectangle.py):
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """Create a square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculates the area of a square"""
        return self.__size ** 2
