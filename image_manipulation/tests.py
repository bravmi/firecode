from .solve import *


def test1():
    A = [[1, 0], [0, 1]]
    B = [[0, 1], [1, 0]]
    assert rotate_image(A) == B


def test2():
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]
    assert rotate_image(A) == B
