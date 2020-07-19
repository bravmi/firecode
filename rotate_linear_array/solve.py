from firecode.utils import *


def reverse(a, start, stop):
    i = start
    j = stop - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1


def rotate_left(a, k):
    """ O(n) time, inplace """
    n = len(a)
    k = k % n
    reverse(a, 0, n)
    reverse(a, 0, n - k)
    reverse(a, n - k, n)
    return a


if __name__ == '__main__':
    pass
