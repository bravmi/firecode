import re

from ..utils import *


def decimal(n, d, prec=28):
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
    Sort of works ;)
    """
    f = decimal(numer, denom)
    s = ''.join(f)
    for i in range(len(s)):
        m = re.search(r'^(.+?)(?P<suf>[1-9]+)(?P=suf)$', s[:i])
        if m:
            return '%s[%s]' % (m.group(1), m.group(2))
    return s


if __name__ == '__main__':
    print(divide(-8, 7))
