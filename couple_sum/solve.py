from firecode.utils import *


def couple_sum(nums, target):
    """
    O(n)
    """
    hist = {}

    for i, x in enumerate(nums, 1):
        if target - x in hist:
            return [hist[target - x], i]
        hist[x] = i
    return []


if __name__ == '__main__':
    pass
