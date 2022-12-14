#!/usr/bin/python3
"""
This module contains the Base class
"""
import json


class Base:
    """
    Class Documentation will go here. Will add later
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ instansiation of class Base """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns a json string of a dictionary """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string rep of list_objs to a file """
        filename = cls.__name__ + ".json"
        file_list = []
        if list_objs is not None:
            for item in list_objs:
                file_list.append(item.to_dictionary())
        with open(filename, 'w', encoding="UTF-8") as f:
            f.write(cls.to_json_string(file_list))

    @classmethod
    def create(cls, **dictionary):
        """ creates an instance of the subclass """
        if cls.__name__ == "Rectangle":
            dummy_class = cls(1, 1)
        if cls.__name__ == "Square":
            dummy_class = cls(1)
        dummy_class.update(**dictionary)
        return dummy_class

    @classmethod
    def load_from_file(cls):
        """ will return a list of instances from a file """
        filename = cls.__name__ + ".json"
        new_list = []
        try:
            with open(filename, 'r') as f:
                new_list = cls.from_json_string(f.read())
            for i, string in enumerate(new_list):
                new_list[i] = cls.create(**new_list[i])
        except Exception:
            pass
        return new_list
