from firecode.utils import *

INF = float("inf")


def triple_sum(nums, target):
    """
    O(n^2)
    """
    res = []
    target3 = target
    for i, x in enumerate(nums):
        target2 = target3 - x
        nums[i] = INF
        couples = two_sum(nums, target2)
        for j, k in couples:
            if i < j < k:
                res.append((x, nums[j], nums[k]))
        nums[i] = x
    return sorted(set(res))


def two_sum(nums, target):
    """
    O(n)
    """
    hist = {}

    res = []
    for i, x in enumerate(nums):
        if target - x in hist:
            res.append((hist[target - x], i))
        hist[x] = i
    return res


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7]
    x = 10
    assert triple_sum(a, x) == [(1, 2, 7), (1, 3, 6), (1, 4, 5), (2, 3, 5)]
