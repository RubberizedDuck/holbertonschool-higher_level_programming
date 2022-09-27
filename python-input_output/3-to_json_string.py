#!/usr/bin/python3
"""
module imports json and returns json rep of
python object
"""
import json


def to_json_string(my_obj):
    """
    Function to return json object
    """
    return json.dumps(my_obj)
