#!/usr/bin/python3
"""Print text in stdout Module"""


def read_file(filename=""):
    """reads filename with Utf-8"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
