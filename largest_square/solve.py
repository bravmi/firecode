import itertools as it

from firecode.utils import *


def find_largest_square(A):
    """
    O(n*m) time, O(n*m) space
    Space could be optimized to O(m) by remembering only the previous row.
    """
    n = len(A)
    m = len(A[0])
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if A[i][j] == 1:
                dp[i][j] = (
                    min(dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j]) + 1
                )
    return max(size for size in it.chain.from_iterable(dp)) ** 2


if __name__ == '__main__':
    A = [
        [1, 1, 0, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
    ]
    assert find_largest_square(A) == 4
