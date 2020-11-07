from ..utils import *


def range_format(r):
    if r.lower_bound == r.upper_bound:
        return str(r.lower_bound)
    return '{}-{}'.format(r.lower_bound, r.upper_bound)


def find_partitions(input_list):
    a = input_list
    if not a:
        return []

    res = [Range(a[0], a[0])]
    for x, y in zip(a, a[1:]):
        if x + 1 == y:
            res[-1].upper_bound = y
        else:
            res.append(Range(y, y))
    return [range_format(r) for r in res]


if __name__ == '__main__':
    a = [1, 2, 3, 6, 7, 8, 10, 11]
    print(find_partitions(a))
