#!/usr/bin/python3
"""
This script imports functions to add all args
when it is executed to a list stored in file add_item.json
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    json_list = load_from_json_file(filename)
except FileNotFoundError:
    json_list = []

for i in range(len(sys.argv)):
    if i == 0:
        continue
    json_list.append(sys.argv[i])

save_to_json_file(json_list, filename)
