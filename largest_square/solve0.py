from firecode.utils import *


def square_elems(A, x, y, k):
    n = len(A)
    m = len(A[0])
    for i in range(x, min(x + k, n)):
        for j in range(y, min(y + k, m)):
            yield A[i][j]


def max_square_sum(A, x, y):
    """
    x is the first coordinate, y is the second
    """
    n = len(A)
    m = len(A[0])
    res = 0
    for k in range(1, min(n, m) + 1):
        elems = list(square_elems(A, x, y, k))
        if all(a == 1 for a in elems) and len(elems) == k ** 2:
            res = max(sum(elems), res)
    return res


def find_largest_square(A):
    n = len(A)
    m = len(A[0])
    return max(max_square_sum(A, i, j) for i in range(n) for j in range(m))


if __name__ == '__main__':
    A = [
        [1, 0, 1],
        [1, 0, 1],
    ]
    assert find_largest_square(A) == 1
