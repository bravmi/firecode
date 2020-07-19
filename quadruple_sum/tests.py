from .solve import *


def test1():
    assert quadruple_sum([1, 2, 3, 4, 5, 6, 7, 8], 10) == [(1, 2, 3, 4)]


def test2():
    assert quadruple_sum([1, 2, 3, 4, 5, 6, 7], 20) == [
        (2, 5, 6, 7),
        (3, 4, 6, 7),
    ]


def test3():
    assert quadruple_sum([1, 2, 3, 4, 5, 6, 7, 8], 20) == [
        (1, 4, 7, 8),
        (1, 5, 6, 8),
        (2, 3, 7, 8),
        (2, 4, 6, 8),
        (2, 5, 6, 7),
        (3, 4, 5, 8),
        (3, 4, 6, 7),
    ]


def test4():
    assert quadruple_sum([-2, -1, 0, 0, 1, 2], 0) == [
        (-2, -1, 1, 2),
        (-2, 0, 0, 2),
        (-1, 0, 0, 1),
    ]


def test5():
    assert quadruple_sum([1, 1, 1, 1], 4) == [(1, 1, 1, 1)]
