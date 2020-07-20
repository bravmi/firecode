from .solve import *
from .solve_alt import divide as divide_alt


def test1():
    assert divide(2, 5) == '0.4' == divide_alt(2, 5)


def test2():
    assert divide(-8, 7) == '-1.[142857]' == divide_alt(-8, 7)


def test3():
    assert divide(1, 14) == '0.0[714285]' == divide_alt(1, 14)


def test4():
    assert divide(0, 100) == '0' == divide_alt(0, 100)


def test5():
    assert divide(20, 5) == '4' == divide_alt(20, 5)


def test6():
    assert divide(-50, 6) == '-8.[3]' == divide_alt(-50, 6)


def test7():
    assert divide(5, 7) == '0.[714285]' == divide_alt(5, 7)
