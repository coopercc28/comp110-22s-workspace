"""Utility functions exercise."""

__author__ = "730394353"


def only_evens(xs: list[int] = list()) -> list[int]:
    """Returns a list of only even numbers."""
    i: int = 0
    new_list: list[int] = []
    while i < len(xs):
        if xs[i] % 2 == 0:
            new_list.append(xs[i])
        i += 1
    return new_list


def sub(xs: list[int], a: int, b: int) -> list[int]:
    """To generate a List which is a subset of the given list."""
    i: int = 0 
    new_list: list[int] = []
    while len(xs) > i and i < b:
        if i >= a:
            new_list.append(xs[i])
        i += 1
    return new_list


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Generate a list containing elements ffrom the first list followed by the second."""
    new_list: list[int] = []
    i: int = 0
    c: int = 0
    while i < len(xs):
        new_list.append(xs[i])
        i += 1
    while c < len(ys):
        new_list.append(ys[c])
        c += 1
    return new_list
