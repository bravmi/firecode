import collections as co

from firecode.utils import *

INF = float('inf')


def min_jumps(arr):
    dp = co.defaultdict(lambda: INF)
    dp[0] = 0

    for i, jump in enumerate(arr):
        if jump == 0:
            continue
        for j in range(1, jump + 1):
            dp[i + j] = min(dp[i] + 1, dp[i + j])
    end = len(arr) - 1
    return 0 if dp[end] == INF else dp[end]


if __name__ == '__main__':
    assert min_jumps([2, 5, 7, 8, 9, 12]) == 2
