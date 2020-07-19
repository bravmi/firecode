from firecode.utils import *


def selection_sort(a):
    """
    O(n^2) time, inplace
    """
    n = len(a)
    if n <= 1:
        return a

    for i in reversed(range(n)):
        biggest = max(range(i + 1), key=lambda j: a[j])
        if a[biggest] > a[i]:
            a[i], a[biggest] = a[biggest], a[i]
    return a


if __name__ == '__main__':
    pass
