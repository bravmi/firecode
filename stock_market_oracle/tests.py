from .solve import *


def test1():
    assert max_profit([50, 100, 20, 80, 20]) == 110


def test2():
    assert max_profit([50, 100]) == 50


def test3():
    assert max_profit([50, 100, 50, 100, 50]) == 100


def test4():
    assert max_profit([0, 100, 0, 100, 0, 100]) == 300


def test5():
    assert max_profit([100, 40, 20, 10]) == 0


def test6():
    assert max_profit([0, 50, 10, 100, 30]) == 140


def test7():
    assert max_profit([100, 100, 80, 20]) == 0


def test8():
    assert max_profit([1, 1]) == 0
