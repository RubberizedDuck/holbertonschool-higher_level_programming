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
