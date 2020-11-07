import itertools as it

from ..utils import *


def nth(gen, n):
    return next(it.islice(gen, n, None))


def seq():
    yield None
    s = '1'
    while True:
        yield s
        l = lambda g: len(list(g))
        s = ''.join('{}{}'.format(l(g), c) for c, g in it.groupby(s))


def look_and_say(n):
    x = nth(seq(), n)
    return int(x) if x else x


if __name__ == '__main__':
    print(list(it.islice(seq(), 0, 10)))
    assert look_and_say(1) == 1
