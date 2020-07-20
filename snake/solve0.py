import itertools as it

from firecode.utils import *


def find_spiral(A):
    n, m = len(A), len(A[0])
    if not n or not m:
        return []
    directions = it.cycle([[0, 1], [1, 0], [0, -1], [-1, 0]])

    i, j = 0, 0
    spiral = [A[0][0]]
    A[0][0] = None
    di, dj = next(directions)
    cells = 1
    while cells < n * m:
        if not (0 <= i + di <= n - 1) or not (0 <= j + dj <= m - 1):
            di, dj = next(directions)
            continue
        if A[i + di][j + dj] is None:
            di, dj = next(directions)
            continue
        i += di
        j += dj
        spiral.append(A[i][j])
        A[i][j] = None
        cells += 1
    return spiral


if __name__ == '__main__':
    A = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    print('[find spiral]: {}'.format(find_spiral(A)))
