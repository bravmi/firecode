from .solve import *


def test1():
    assert unique_routes(4, 5) == 35


def test2():
    assert unique_routes(7, 7) == 924


def test3():
    assert unique_routes(1, 2) == 1


def test4():
    assert unique_routes(5, 2) == 5


def test5():
    assert unique_routes(1, 1) == 1
