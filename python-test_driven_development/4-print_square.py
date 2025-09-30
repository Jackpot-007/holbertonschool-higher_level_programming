#!/usr/bin/python3
"""Define a function that prints a square with the character #."""


def print_square(size):
    """Prints a square"""
    if not isinstance(size, int):
        raise TypeError(message)

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError(message)

    for i in range(size):
        print("#" * size)
