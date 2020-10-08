#!/usr/bin/python3
""" script that adds all arguments
    to a Python list, and then save
    them to a file
"""


from sys import argv
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

try:
    obj = load_from_json_file("add_item.json")
except:
    obj = []

obj += argv[1:]
save_to_json_file(obj, "add_item.json")
