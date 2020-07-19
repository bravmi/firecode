import itertools as it
import string

from firecode.utils import *


def decode_string(msg):
    """
    O(n) time, O(n) space
    """
    n = len(msg)
    dec = {str(a): b for a, b in zip(it.count(1), string.ascii_uppercase)}

    @cached
    def go(i):
        if i == n:
            return 1
        elif i > n:
            return 0
        one = go(i + 1) if dec.get(msg[i]) else 0
        two = go(i + 2) if dec.get(msg[i : i + 2]) else 0
        return one + two

    return go(0)


if __name__ == '__main__':
    pass
