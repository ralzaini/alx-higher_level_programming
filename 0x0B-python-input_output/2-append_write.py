#!/usr/bin/python3
"""Append Module"""


def append_write(filename="", text=""):
    """reads filename with UTF-8"""
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
