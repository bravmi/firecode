from .solve import *


def test1():
    a = [1, 2, 3, 4, 5, 6, 7]
    x = 15
    assert triple_sum(a, x) == [(2, 6, 7), (3, 5, 7), (4, 5, 6)]


def test2():
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    x = 20
    assert triple_sum(a, x) == [(5, 7, 8)]


def test3():
    a = [-2, -1, 0, 0, 1, 2]
    x = 0
    assert triple_sum(a, x) == [(-2, 0, 2), (-1, 0, 1)]


def test4():
    a = [1, 1, 1, 1]
    x = 3
    assert triple_sum(a, x) == [(1, 1, 1)]


def test5():
    a = [1, 2, 3, 4, 5, 6, 7]
    x = 10
    assert triple_sum(a, x) == [(1, 2, 7), (1, 3, 6), (1, 4, 5), (2, 3, 5)]
