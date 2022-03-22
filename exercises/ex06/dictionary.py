"""ex06 dictionary."""

__author__ = "730394353"


def invert(my_dict: dict[str, str] = {}) -> dict[str, str]:
    """To return a dict that is the inverse of the original."""
    result: dict[str, str] = {}
    for key in my_dict:
        result[my_dict[key]] = key
    if len(result) != len(my_dict):
        raise KeyError("KeyError")
    return result


def favorite_color(my_dict: dict[str, str]) -> str:
    """To return the color that appears the most."""
    result: str = ""
    new_dict: dict[str, int] = {}
    counter: int = 0
    for person in my_dict:
        if my_dict[person] in new_dict:
            new_dict[my_dict[person]] += 1 
        else:
            new_dict[my_dict[person]] = 1
    for color in new_dict:
        if new_dict[color] > counter:
            counter = new_dict[color]
            result = color
    return result


def count(xs: list[str] = list()) -> dict[str, int]:
    """Return a dict with a key and value that is associated to the occurance of the key."""
    my_dict: dict[str, int] = {}
    for x in xs:
        if x in my_dict:
            my_dict[x] += 1
        else:
            my_dict[x] = 1
    return my_dict
