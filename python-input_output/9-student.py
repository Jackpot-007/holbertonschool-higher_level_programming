#!/usr/bin/python3
"""Module defining the class Student"""


class Student:
    """Class that defines properties of student."""
    def __init__(self, first_name, last_name, age):
        """Creates new instance of student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrives a dictionary representation of a Student instance."""
        return self.__dict__
