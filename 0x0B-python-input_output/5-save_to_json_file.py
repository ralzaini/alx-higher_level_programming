#!/usr/bin/python3
"""Json string Module"""


import json


def save_to_json_file(my_obj, filename):
    """writes an object to textfile"""
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(my_obj, f)
