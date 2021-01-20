#!/usr/bin/python3
"""Module function append_write"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
    and returns the number of characters added"""
    with open(filename, "a", encoding="utf-8") as a_w:
        return a_w.write(text)
