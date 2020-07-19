import sys

from firecode.utils import *


def max_gain(input_list):
    min_elem = sys.maxsize
    ans = -sys.maxsize
    for elem in input_list:
        min_elem = min(elem, min_elem)
        ans = max(elem - min_elem, ans)
    return ans


if __name__ == '__main__':
    pass
