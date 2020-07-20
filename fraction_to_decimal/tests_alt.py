from .solve_alt import *


def test1():
    assert divide(2, 5) == '0.4'


def test2():
    assert divide(-8, 7) == '-1.[142857]'


def test3():
    assert divide(1, 14) == '0.0[714285]'


def test4():
    assert divide(0, 100) == '0'


def test5():
    assert divide(20, 5) == '4'


def test6():
    assert divide(-50, 6) == '-8.[3]'


def test7():
    assert divide(5, 7) == '0.[714285]'
