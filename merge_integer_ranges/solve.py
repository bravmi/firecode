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


if __name__ == '__main__':
    pass
