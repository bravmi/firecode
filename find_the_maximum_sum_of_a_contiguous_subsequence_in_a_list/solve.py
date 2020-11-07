from ..utils import *


def largestContinuousSum(arr):
    if not arr:
        return None
    best = curr = float('-inf')
    for x in arr:
        curr = max(curr + x, x)
        best = max(best, curr)
    return best


if __name__ == '__main__':
    pass
