import collections as co

from ..utils import *


def are_isomorphic(s1, s2):
    if s1 is None or s2 is None:
        return False
    c1 = co.Counter(s1)
    c2 = co.Counter(s2)
    return sorted(c1.values()) == sorted(c2.values())


if __name__ == '__main__':
    pass
