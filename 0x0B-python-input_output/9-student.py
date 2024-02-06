#!/usr/bin/python3
"""Student class Module"""


class Student:
    """Representation of a Student"""
    def __init__(self, first_name, last_name, age):
        """Initialization of each student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary representation of the student"""
        return self.__dict__
