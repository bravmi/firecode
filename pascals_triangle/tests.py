from .solve import *


def test0():
    assert generate_pascal_triangle(0) == []


def test1():
    assert generate_pascal_triangle(1) == [[1]]


def test2():
    assert generate_pascal_triangle(2) == [
        [1],
        [1, 1],
    ]


def test3():
    assert generate_pascal_triangle(3) == [
        [1],
        [1, 1],
        [1, 2, 1],
    ]


def test4():
    assert generate_pascal_triangle(4) == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
    ]
