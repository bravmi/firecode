from .solve import *


def test1():
    assert min_jumps([2, 5, 7, 8, 9, 12]) == 2


def test2():
    assert min_jumps([2, 1, 1, 1, 1, 1]) == 4


def test3():
    assert min_jumps([2, 1, 1, 5, 2, 12]) == 3


def test4():
    assert min_jumps([4, 1, 2, 0, 2, 12]) == 2


def test5():
    assert min_jumps([2, 1, 0, 5, 2, 12]) == 0


def test6():
    assert min_jumps([2]) == 0


def test7():
    assert min_jumps([2, 1, 1, 1, 1, 12, 15]) == 5
