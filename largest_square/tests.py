from .solve import *
from .solve_alt import find_largest_square as find_largest_square_alt


def test1():
    A = [
        [1, 1, 0, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
    ]
    assert find_largest_square(A) == 4 == find_largest_square_alt(A)


def test2():
    A = [
        [0, 0],
        [0, 0],
    ]
    assert find_largest_square(A) == 0 == find_largest_square_alt(A)


def test3():
    A = [
        [1, 1],
        [1, 1],
    ]
    assert find_largest_square(A) == 4 == find_largest_square_alt(A)


def test4():
    A = [
        [1, 0],
        [0, 1],
    ]
    assert find_largest_square(A) == 1 == find_largest_square_alt(A)


def test5():
    A = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]
    assert find_largest_square(A) == 9 == find_largest_square_alt(A)


def test6():
    A = [
        [1, 0, 1],
        [1, 0, 1],
    ]
    assert find_largest_square(A) == 1 == find_largest_square_alt(A)
