from .solve import *


def test1():
    assert are_isomorphic('css', 'dll') is True


def test2():
    assert are_isomorphic('css', 'dle') is False


def test3():
    assert are_isomorphic('', '') is True


def test4():
    assert are_isomorphic('a', 'b') is True


def test5():
    assert are_isomorphic('foo', 'bar') is False


def test6():
    assert are_isomorphic('add', 'egg') is True


def test7():
    assert are_isomorphic(None, None) is False


def test8():
    assert are_isomorphic('abcd', 'aabb') is False
