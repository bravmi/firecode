from ..utils import *


def min_triangle_depth(tri):
    """
    O(n^2) time, O(n^2) space
    """
    n = len(tri)

    @cached
    def go(i, j):
        if i >= n or j >= n:
            return 0
        return tri[i][j] + min(go(i + 1, j), go(i + 1, j + 1))

    return go(0, 0)


if __name__ == '__main__':
    tri = [
        [1],
        [2, 3],
        [4, 5, 6],
        [7, 8, 9, 10],
    ]
    assert min_triangle_depth(tri) == 14
