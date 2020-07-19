from .solve import *


def test1():
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert matrix_max_sum_dfs(grid) == 29


def test2():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    assert matrix_max_sum_dfs(grid) == 16


def test3():
    grid = [
        [1, 2],
        [3, 4],
    ]
    assert matrix_max_sum_dfs(grid) == 8


def test4():
    grid = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]
    assert matrix_max_sum_dfs(grid) == 5


def test5():
    grid = [
        [0, 0],
        [0, 0],
    ]
    assert matrix_max_sum_dfs(grid) == 0
