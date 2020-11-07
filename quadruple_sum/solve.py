from ..utils import *


def quadruple_sum(nums, target):
    """
    O(n^2) time and O(n^2) space time with caching I think
    """
    n = len(nums)

    @cached
    def go(i, target, d):
        if target == 0 and d == 0:
            return [()]
        if i >= n:
            return []
        if d <= 0:
            return []

        x = nums[i]
        with_ = go(i + 1, target - x, d - 1)
        without = go(i + 1, target, d)
        with_ = [(x,) + a for a in with_]
        return with_ + without

    return go(0, target, 4)


if __name__ == '__main__':
    ans = quadruple_sum([1, 2, 3, 4, 5, 6, 7], 20)
    assert ans == [(2, 5, 6, 7), (3, 4, 6, 7)]
