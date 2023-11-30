#!/usr/bin/python3
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    if a < b:
        d = add(a, b)
        for y in range(4, 6):
            d = add(d, y)
        return (d)
    else:
        return sub(a, b)
