from firecode.utils import *


def bubble_sort(a):
    """ O(n^2) time, inplace """
    m = len(a)
    if m <= 1:
        return a

    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(m - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                is_sorted = False
        m -= 1
    return a


if __name__ == '__main__':
    pass
