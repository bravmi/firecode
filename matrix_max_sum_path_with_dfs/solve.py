from ..utils import *


def matrix_max_sum_dfs(grid):
    n = len(grid)
    m = len(grid[0])

    @cached
    def go(i, j):
        if i >= n or j >= m:
            return 0
        return grid[i][j] + max(go(i + 1, j), go(i, j + 1))

    return go(0, 0)


if __name__ == '__main__':
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    assert matrix_max_sum_dfs(grid) == 29
