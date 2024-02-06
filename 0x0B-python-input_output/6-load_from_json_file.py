#!/usr/bin/python3
"""Json string Module"""


import json


def load_from_json_file(filename):
    """creates ann object from json file """
    with open(filename, "r", encoding='utf-8') as f:
        return json.load(f)
