#!/usr/bin/python3
"""Base class Module"""
import json
import os
import csv


class Base:
    """
    Class Base

    Parameters:
        id (int): instance attribute integer
        nb_objects (int): class attribute integer
    """

    __nb_objects = 0


    def __init__(self, id=None):
        """base function"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @classmethod
    def set_nb_objects(cls):
        """Class method to set the value of nb_objest to zero"""
        Base.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = "{:s}.json".format(cls.__name__)
        if list_objs is None:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(Base.to_json_string([]))
        else:
            list_dict = [obj.to_dictionary() for obj in list_objs]
            with open(filename, "w", encoding="utf-8") as file:
                file.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Parse a JSON string to a list of dictionaries."""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        from models.rectangle import Rectangle
        from models.square import Square

        name = cls.__name__
        if name == "Rectangle":
            obj = Rectangle(1, 1)
        else:
            obj = Square(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Load a list of instances from a JSON file."""
        from models.rectangle import Rectangle
        from models.square import Square

        name = cls.__name__
        filename = "{:s}.json".format(name)
        obj_list = []
        if os.path.isfile(filename):
            with open(filename, "r", encoding="utf-8") as f:
                json_string = f.read()
                list_dict_objs = Base.from_json_string(json_string)
                for obj in list_dict_objs:
                    if name == "Rectangle":
                        obj_list.append(Rectangle.create(**obj))
                    else:
                        obj_list.append(Square.create(**obj))
                return obj_list
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of instances to a CSV file."""
        from models.rectangle import Rectangle
        from models.square import Square

        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            for obj in list_objs:
                if isinstance(obj, Rectangle):
                    writer.writerow([obj.id,
                                    obj.width,
                                    obj.height,
                                    obj.x,
                                    obj.y])
                elif isinstance(obj, Square):
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Load a list of instances from a CSV file."""
        from models.rectangle import Rectangle
        from models.square import Square

        filename = f"{cls.__name__}.csv"
        if not os.path.exists(filename):
            return []

        objs_list = []
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    objs_list.append(Rectangle(*row))
                elif cls.__name__ == "Square":
                    objs_list.append(Square(*row))
        return objs_list
