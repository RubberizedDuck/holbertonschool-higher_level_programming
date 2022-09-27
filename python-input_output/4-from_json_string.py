#!/usr/bin/python3
"""
This module is designed to convert a JSON
string to a python object
"""
import json


def from_json_string(my_str):
    """
    Function will return json string
    to a Python Object
    """
    return json.loads(my_str)
