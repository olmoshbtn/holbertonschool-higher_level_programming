#!/usr/bin/python3
"""Module function read_file"""


def read_file(filename=""):
    """Read a text file (UTF-8) and prints it in stdout"""
    with open(filename,'r', 'utf-8') as seb:
        print(seb_pep8.read(), end='')
