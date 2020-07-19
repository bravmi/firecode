from firecode.utils import *


def merge_ranges(ranges):
    if len(ranges) <= 1:
        return ranges

    res = [ranges[0]]
    for b in ranges[1:]:
        a = res[-1]
        if b.lower_bound <= a.upper_bound:
            a.upper_bound = max(b.upper_bound, a.upper_bound)
        else:
            res.append(b)
    return res


def insert_range(ranges, new_range):
    res = []
    for a in ranges:
        if new_range.lower_bound <= a.lower_bound:
            res.append(new_range)
        res.append(a)
    if len(res) == len(ranges):
        res.append(new_range)
    return res


def insert_and_merge(ranges, new_range):
    ranges = insert_range(ranges, new_range)
    ranges = merge_ranges(ranges)
    return ranges


if __name__ == '__main__':
    ranges = [[1, 10], [5, 8], [8, 15]]
    ranges = [Range(*a) for a in ranges]
    ranges = insert_and_merge(ranges, Range(9, 20))
    assert [a.to_list() for a in ranges] == [[1, 20]]
