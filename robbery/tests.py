from .solve import *


def test1():
    assert robbery([60, 50, 20, 32, 20, 50]) == 142


def test2():
    assert robbery([40, 25, 25, 30]) == 70


def test3():
    assert robbery([15, 40, 25, 25, 30, 45]) == 110


def test4():
    assert robbery([20, 25, 50, 62, 12, 20, 20]) == 107
