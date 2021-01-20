#!/usr/bin/python3
"""Module function read_file"""


def read_file(filename=""):
    """Read a text file (UTF-8) and prints it in stdout"""
    with open(filename, "r", encoding="utf-8") as r_f:
        print(r_f.read(), end='')
