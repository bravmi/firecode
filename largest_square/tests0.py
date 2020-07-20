from .solve0 import *


def test1():
    A = [
        [1, 1, 0, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
    ]
    assert find_largest_square(A) == 4


def test2():
    A = [
        [0, 0],
        [0, 0],
    ]
    assert find_largest_square(A) == 0


def test3():
    A = [
        [1, 1],
        [1, 1],
    ]
    assert find_largest_square(A) == 4


def test4():
    A = [
        [1, 0],
        [0, 1],
    ]
    assert find_largest_square(A) == 1


def test5():
    A = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]
    assert find_largest_square(A) == 9


def test6():
    A = [
        [1, 0, 1],
        [1, 0, 1],
    ]
    assert find_largest_square(A) == 1
