from firecode.utils import *


def insert_star_between_pairs0(s):
    if not s:
        return s
    if len(s) <= 1:
        return s

    if s[0] == s[1]:
        return '{}*{}'.format(s[0], insert_star_between_pairs(s[1:]))
    else:
        return '{}{}'.format(s[0], insert_star_between_pairs(s[1:]))


def _insert_star_between_pairs(s):
    if len(s) <= 1:
        yield s
        return

    yield s[0]
    if s[0] == s[1]:
        yield '*'
    # yield from insert_star_between_pairs(s[1:])
    for c in insert_star_between_pairs(s[1:]):
        yield c


def insert_star_between_pairs(s):
    if not s:
        return s

    return ''.join(_insert_star_between_pairs(s))


if __name__ == '__main__':
    assert insert_star_between_pairs('abba') == 'ab*ba'
