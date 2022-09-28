#!/usr/bin/python3
"""
This module is designed to create an object
using a JSON file
"""
import json


def load_from_json_file(filename):
    """ Function to create object """
    with open(filename, 'r', encoding="utf-8") as f:
              return json.load(f)
