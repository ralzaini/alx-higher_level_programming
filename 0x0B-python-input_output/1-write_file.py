#!/usr/bin/python3
"""Print text in stdout Module"""


def write_file(filename="", text=""):
    """reads filename with UTF-8"""
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
