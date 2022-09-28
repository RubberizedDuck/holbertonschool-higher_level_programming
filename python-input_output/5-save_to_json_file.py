#!/usr/bin/python3
"""
This module is designed to write an object
to a text file using JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function to write to file with JSON rep
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return json.dump(my_obj, f)
