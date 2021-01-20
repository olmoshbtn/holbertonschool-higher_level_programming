#!/usr/bin/python3
"""Module function write_file"""


def write_file(filename="", text=""):
    """Writes a string text file (UTF8) and returns number of char written"""
    with open(filename, "w", encoding="utf-8") as w_f:
        return w_f.write(text)
