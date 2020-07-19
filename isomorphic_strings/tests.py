from .solve import *


def test1():
    assert are_isomorphic('css', 'dll') == True


def test2():
    assert are_isomorphic('css', 'dle') == False


def test3():
    assert are_isomorphic('', '') == True


def test4():
    assert are_isomorphic('a', 'b') == True


def test5():
    assert are_isomorphic('foo', 'bar') == False


def test6():
    assert are_isomorphic('add', 'egg') == True


def test7():
    assert are_isomorphic(None, None) == False


def test8():
    assert are_isomorphic('abcd', 'aabb') == False
