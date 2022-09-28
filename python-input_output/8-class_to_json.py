#!/usr/bin/python3
"""
This module is designed to convert a class
to a JSON dict
"""
import json


def class_to_json(obj):
    """
    Functions returns json dictonary of a class object
    """
    return json.dumps(obj.__dict__)
