from .solve import *


def test1():
    assert rotate_left([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]


def test2():
    assert rotate_left([1, 2, 3, 4, 5, 6, 7, 8, 9], 10) == [
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        1,
    ]


def test3():
    assert rotate_left([1], 7) == [1]


def test4():
    assert rotate_left([1, 2, 3, 4, 5, 6, 7, 8, 9], 2) == [
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        1,
        2,
    ]


def test5():
    assert rotate_left([1, 2, 3, 4, 5, 6, 7, 8, 9], 14) == [
        6,
        7,
        8,
        9,
        1,
        2,
        3,
        4,
        5,
    ]


def test6():
    assert rotate_left([1, 2, 3, 4, 5, 6, 7, 8, 9], 4) == [
        5,
        6,
        7,
        8,
        9,
        1,
        2,
        3,
        4,
    ]
