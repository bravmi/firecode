from firecode.utils import *


def long_common_prefix(items):
    """
    O(n*m)
    """
    same = []
    rows = items
    for col in zip(*rows):
        if len(set(col)) == 1:
            same.append(col[0])
        else:
            break
    return ''.join(same)


if __name__ == '__main__':
    items = ['firecode', 'fireacb', 'fireac']
    assert long_common_prefix(items) == 'fire'
