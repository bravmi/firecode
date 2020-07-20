from .solve_alt import *


def test1():
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    assert find_spiral(A) == [1, 2, 3, 6, 9, 8, 7, 4, 5]


def test2():
    A = [
        [1, 2],
        [3, 4],
    ]
    assert find_spiral(A) == [1, 2, 4, 3]


def test3():
    A = [
        [1, 0],
        [0, 1],
    ]
    assert find_spiral(A) == [1, 0, 1, 0]


def test4():
    A = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    assert find_spiral(A) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
