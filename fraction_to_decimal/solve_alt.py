import itertools as it

from ..utils import *


def decimal(n, d, prec=100):
    if n * d < 0:
        yield '-'
    n = abs(n)
    d = abs(d)

    q, r = divmod(n, d)
    yield str(q)
    if not r:
        return

    yield '.'
    for _ in range(prec):
        r *= 10
        q, r = divmod(r, d)
        yield str(q)
        if not r:
            return


def divide(numer, denom):
    """
    Don't know why it works exactly xD
    """
    dec = decimal(numer, denom)
    before = list(it.takewhile(lambda c: c != '.', dec))

    after = []
    hist = {}
    for c in dec:
        if c in hist:
            index = hist[c]
            recur = ''.join(after[index:])
            after = after[:index] + ['[{}]'.format(recur)]
            break
        else:
            after.append(c)
            hist[c] = len(after) - 1
    ans = before + ['.'] + after if after else before
    return ''.join(ans)


if __name__ == '__main__':
    print(divide(-8, 7))
