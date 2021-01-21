#!/usr/bin/python3
"""Module function pascal_triangle"""


def pascal_triangle(n):
    """Representation of pascal triangle 'n'"""
    triangle = []
    if n > 0:
        triangle.append([1])
        if n > 1:
            for i in range(1, n):
                row = [1]
                for j in range(1, i):
                    row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
                row.append(1)
                triangle.append(row)
    return triangle
