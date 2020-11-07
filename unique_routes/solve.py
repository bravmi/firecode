from ..utils import *


def unique_routes(rows, cols):
    n = rows
    m = cols

    @cached
    def go(i, j):
        if i == 0 or j == 0:
            return 1
        return go(i - 1, j) + go(i, j - 1)

    return go(n - 1, m - 1)


if __name__ == '__main__':
    pass
