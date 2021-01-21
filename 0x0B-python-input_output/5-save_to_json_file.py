#!/usr/bin/python3
""""Module function save_to_json_file"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, 'w', encoding='utf-8') as s_t_j_f:
        json.dump(my_obj, s_t_j_f)
