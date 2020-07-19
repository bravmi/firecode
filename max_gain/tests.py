from .solve import *


def test1():
    assert max_gain([100, 40, 20, 10]) == 0


def test2():
    assert max_gain([0, 50, 10, 100, 30]) == 100
