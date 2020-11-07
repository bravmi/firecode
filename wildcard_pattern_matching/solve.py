from ..utils import *


def match(first, second):
    a, b = first, second
    if not a and not b:
        return True
    if a in '?*' and not b:
        return True
    if a and not b or b and not a:
        return False

    if a[0] == b[0]:
        return match(a[1:], b[1:])
    elif a[0] == '?':
        return match(a[1:], b) or match(a[1:], b[1:])
    elif a[0] == '*':
        return match(a[1:], b) or match(a[1:], b[1:]) or match(a, b[1:])
    return False


def match_iter(first, second):
    """
    not mine
    """
    l, m = 0, 0
    starIdx, i = -1, -1
    while l < len(second):
        if m < len(first) and (first[m] == '?' or first[m] == second[l]):
            m += 1
            l += 1
        elif m < len(first) and first[m] == '*':
            i = l
            starIdx = m
            m += 1
        elif starIdx != -1:
            l = i + 1
            m = starIdx + 1
            i += 1
        else:
            return False
    while m < len(first) and first[m] == '*':
        m += 1
    return m == len(first)


# match = match_iter

if __name__ == '__main__':
    pass
