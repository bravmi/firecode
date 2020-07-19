from firecode.utils import *


def binsearch(x, a, cmp):
    low, high = 0, len(a)

    while low < high:
        mid = (low + high) // 2
        if cmp(a[mid], x):
            low = mid + 1
        else:
            high = mid
    return low


def find_range(input_list, input_number):
    left = binsearch(input_number, input_list, lambda x, y: x < y)
    right = binsearch(input_number, input_list, lambda x, y: x <= y)
    return Range(left, right - 1)


if __name__ == '__main__':
    pass
