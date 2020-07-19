from .solve import *


def test1():
    assert better_fibonacci(0) == 0


def test2():
    assert better_fibonacci(3) == 2


def test3():
    assert better_fibonacci(9) == 34
