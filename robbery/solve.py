from ..utils import *


def robbery(amounts):
    prev = cur = 0
    for val in amounts:
        # either we use val or we don't
        prev, cur = cur, max(prev + val, cur)
    return cur


if __name__ == '__main__':
    print(robbery([40, 25, 25, 30]))
