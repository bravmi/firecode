from .solve import *


def test1():
    assert couple_sum([1, 2, 3], 5) == [2, 3]


def test2():
    assert couple_sum([1, 2, 3, 4, 5], 3) == [1, 2]


def test3():
    assert couple_sum([1, 2, 9, 11, 20], 20) == [3, 4]


def test4():
    assert couple_sum([1, 2, 3, 4, 5], 9) == [4, 5]


def test5():
    assert couple_sum([1, 2, 5, 5, 9, 10], 10) == [3, 4]


def test6():
    assert couple_sum([1, 2, 3, 4, 9, 10], 10) == [1, 5]
