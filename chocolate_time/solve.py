"""
Non-brute version taken form hackerrank editorial:
https://www.hackerrank.com/challenges/candies/editorial
"""

from sys import maxsize as INF

from ..utils import *


def distributeChocolateBrute(points):
    """ O(n^2) time, O(n) space """
    n = len(points)
    points = [INF] + points + [INF]
    chocolates = [0] + [1] * n + [0]

    is_done = False
    while not is_done:
        is_done = True
        for i in range(1, n + 1):
            if (
                points[i] > points[i - 1]
                and chocolates[i] <= chocolates[i - 1]
            ):
                chocolates[i] = chocolates[i - 1] + 1
                is_done = False
            if (
                points[i] > points[i + 1]
                and chocolates[i] <= chocolates[i + 1]
            ):
                chocolates[i] = chocolates[i + 1] + 1
                is_done = False
    return sum(chocolates[1 : n + 1])


def distributeChocolate(points):
    """ O(n) time, O(n) space"""
    n = len(points)

    # add sentinels
    points = [INF] + points + [INF]

    chocolates = [0] * (n + 2)
    # populate 'valleys'
    for i in range(1, n + 1):
        if points[i - 1] >= points[i] <= points[i + 1]:
            chocolates[i] = 1

    # populate 'rises'
    for i in range(1, n + 1):
        if points[i - 1] < points[i] <= points[i + 1]:
            chocolates[i] = chocolates[i - 1] + 1

    # populate 'falls'
    for i in range(n, 0, -1):
        if points[i - 1] >= points[i] > points[i + 1]:
            chocolates[i] = chocolates[i + 1] + 1

    # populate 'peaks'
    for i in range(1, n + 1):
        if points[i - 1] < points[i] > points[i + 1]:
            chocolates[i] = max(chocolates[i - 1], chocolates[i + 1]) + 1

    # total number of chocolates
    return sum(chocolates)


if __name__ == '__main__':
    print(distributeChocolateBrute([2, 3, 3, 2, 1, 5, 2]))
    print(distributeChocolate([2, 3, 3, 2, 1, 5, 2]))
