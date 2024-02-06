#!/usr/bin/python3
"""Student class Module"""


class Student:
    """Student Class"""
    def __init__(self, first_name, last_name, age):
        """Initialization of the student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """from class to json"""
        if attrs is None:
            return self.__dict__
        all_str = all(isinstance(element, str) for element in attrs)
        if not all_str:
            return self.__dict__
        dictionary = {}
        for key in attrs:
            if key in self.__dict__:
                dictionary[key] = self.__dict__[key]
        return dictionary
