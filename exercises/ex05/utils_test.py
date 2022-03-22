"""Tests for functions."""

__author__ = "730394353"


from utils import only_evens, sub, concat


def test_only_evens_list() -> None:
    """Test to get only evens out of a list."""
    xs: list[int] = [4, 3, 6]
    assert only_evens(xs) == [4, 6]


def test_only_evens_lists() -> None:
    """Test to get only evens out of a list."""
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(xs) == [2, 4, 6]


def test_edge_case_evens() -> None:
    """Edge case for only_evens."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_sub_list() -> None:
    """To generate a List which is a subset of the given list."""
    xs: list[int] = [1, 2, 3, 4, 5]
    a: int = 1
    b: int = 4
    assert sub(xs, a, b) == [2, 3, 4]


def test_sub_lists() -> None:
    """To generate a List which is a subset of the given list."""
    xs: list[int] = [10, 20, 30, 40, 50]
    a: int = 1
    b: int = 3
    assert sub(xs, a, b) == [20, 30]


def test_edge_case_sub() -> None:
    """Edge case for sub."""
    xs: list[int] = []
    a: int = 0
    b: int = 1
    assert sub(xs, a, b) == []


def test_concat_list() -> None:
    """Combination of two lists."""
    xs: list[int] = [1, 2, 3]
    ys: list[int] = [1, 2, 3]
    assert concat(xs, ys) == [1, 2, 3, 1, 2, 3]


def test_concat_lists() -> None:
    """Combination of two lists."""
    xs: list[int] = [10, 11, 12, 13]
    ys: list[int] = [14, 15, 16]
    assert concat(xs, ys) == [10, 11, 12, 13, 14, 15, 16]


def test_edge_case_concat() -> None:
    """Edge case for concat."""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []
