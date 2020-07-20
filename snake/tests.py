from .solve import *
from .solve_alt import find_spiral as find_spiral_alt


def test1():
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    assert find_spiral(A) == [1, 2, 3, 6, 9, 8, 7, 4, 5] == find_spiral_alt(A)


def test2():
    A = [
        [1, 2],
        [3, 4],
    ]
    assert find_spiral(A) == [1, 2, 4, 3] == find_spiral_alt(A)


def test3():
    A = [
        [1, 0],
        [0, 1],
    ]
    assert find_spiral(A) == [1, 0, 1, 0] == find_spiral_alt(A)


def test4():
    A = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    assert (
        find_spiral(A)
        == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        == find_spiral_alt(A)
    )
