#!/usr/bin/python3
"""Module function is_same_class"""


def is_same_class(obj, a_class):
    """Return True if the obj is the exact class a_class, oteherwise False"""
    return (type(obj) == a_class)
