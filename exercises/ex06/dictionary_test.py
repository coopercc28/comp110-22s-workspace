"""ex06 dictionary tests."""

__author__ = "730394353"


from dictionary import invert, favorite_color, count


def test_invert() -> None:
    """Test to get an inverted list."""
    my_dict: dict[str, str] = {'x': 'y', 'a': 'b', 'c': 'd'}
    assert invert(my_dict) == {'y': 'x', 'b': 'a', 'd': 'c'}


def test_invert_again() -> None:
    """Test to get an inverted list."""
    my_dict: dict[str, str] = {'baseball': 'football'}
    assert invert(my_dict) == {'football': 'baseball'}


def test_invert_edge_case() -> None:
    """Edge case for invert test."""
    my_dict: dict[str, str] = {}
    assert invert(my_dict) == {}


def test_favorite_color() -> None:
    """Test to return color that is there the most."""
    my_dict: dict[str, str] = {"Cooper": "yellow", "Andrew": "yellow", "Tucker": "blue"}
    assert favorite_color(my_dict) == "yellow"


def test_favorite_colors() -> None:
    """Test to return color that is there the most."""
    my_dict: dict[str, str] = {"Cooper": "green", "Andrew": "blue", "Tucker": "blue"}
    assert favorite_color(my_dict) == "blue"


def test_favorite_color_edge_case() -> None:
    """Edge case for favorite color."""
    my_dict: dict[str, str] = {}
    assert favorite_color(my_dict) == ""


def test_count() -> None:
    """Test for the count function."""
    xs: list[str] = ['UNC', 'UNC', 'Dook']
    assert count(xs) == {'UNC': 2, 'Dook': 1}


def test_counts() -> None:
    """Test for the count function."""
    xs: list[str] = ['UNC', 'UNC']
    assert count(xs) == {'UNC': 2}


def test_count_edge_case() -> None:
    """Edge case for count function."""
    xs: list[str] = []
    assert count(xs) == {}