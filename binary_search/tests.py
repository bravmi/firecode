from .solve import *


def test1():
    assert binary_search([2, 5, 7, 8, 9], 9)


def test2():
    assert not binary_search([2, 8, 9, 12], 6)


def test3():
    assert not binary_search([2], 4)


def test4():
    assert not binary_search([], 9)
