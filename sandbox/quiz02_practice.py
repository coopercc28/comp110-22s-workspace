"""Practice."""


def odd_and_even(xs: list[int]) -> list[int]:
    """Return odd numbers on even idexes."""
    i: int = 0
    ys: list[int] = []
    while i < len(xs):
        if xs[i] % 2 == 1 and i % 2 == 0:
            ys.append(xs[i])
        i += 1
    return ys


def vowels_and_threes(a: str = "") -> str:
    """vowel or letter at multiple of 3."""
    i: int = 0
    v: int = 0
    vowels: list[str] = ["a", "e", "i", "o", "u"]
    b: str = ""
    while i < len(a):
        
        