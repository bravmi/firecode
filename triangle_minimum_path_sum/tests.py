from .solve import *


def test1():
    tri = [
        [1],
        [2, 3],
        [4, 5, 6],
        [7, 8, 9, 10],
    ]
    assert min_triangle_depth(tri) == 14


def test2():
    tri = [
        [1],
        [2, 3],
        [4, 5, 6],
    ]
    assert min_triangle_depth(tri) == 7


def test3():
    tri = [
        [1],
        [2, 3],
    ]
    assert min_triangle_depth(tri) == 3


def test4():
    tri = [
        [1],
        [1, 0],
        [1, 2, 3],
        [7, 2, 3, 1],
    ]
    assert min_triangle_depth(tri) == 5


def test5():
    tri = [
        [1],
    ]
    assert min_triangle_depth(tri) == 1
