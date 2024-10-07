#!/usr/bin/python3
"""contains `generate_pascal_triangle` function"""


def pascal_triangle(n):
    """algorithm for pascal's triangle"""
    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        triangle.append(row)
    return triangle
