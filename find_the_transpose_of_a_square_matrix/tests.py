from .solve import *

# transpose_matrix = transpose_matrix_hack


def test1():
    A = [
        [1, 0],
        [1, 0],
    ]
    B = [
        [1, 1],
        [0, 0],
    ]
    assert transpose_matrix(A) == B


def test2():
    A = [[1, 0, 1], [1, 0, 1], [1, 0, 1]]
    B = [[1, 1, 1], [0, 0, 0], [1, 1, 1]]
    assert transpose_matrix(A) == B


def test3():
    A = [[1]]
    B = [[1]]
    assert transpose_matrix(A) == B


def test4():
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    assert transpose_matrix(A) == B
