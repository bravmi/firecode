from .solve import *


def test1():
    a = [5, 4, 3]
    assert bubble_sort(a) == [3, 4, 5]


def test2():
    a = [3]
    assert bubble_sort(a) == [3]


def test3():
    a = []
    assert bubble_sort(a) == []


def test4():
    a = [-8, -2, -1, 0]
    assert bubble_sort(a) == [-8, -2, -1, 0]


def test5():
    a = [1, 1, 1, 2, 2, 2]
    assert bubble_sort(a) == [1, 1, 1, 2, 2, 2]


def test6():
    a = [0, 1, 2, 4, 5]
    assert bubble_sort(a) == [0, 1, 2, 4, 5]


def test7():
    a = [1, 1]
    assert bubble_sort(a) == [1, 1]
