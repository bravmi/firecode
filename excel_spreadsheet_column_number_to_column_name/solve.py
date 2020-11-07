import string

from ..utils import *

DIGITS = string.ascii_uppercase


def excel_column_number_to_name(x):
    base = 26

    digits = []
    while x:
        q, r = divmod(x - 1, base)
        digits.append(DIGITS[r])
        x = q
    digits.reverse()

    return ''.join(digits)


if __name__ == '__main__':
    for x in [1, 26, 27, 52]:
        print('{:>2} -> {:>2}'.format(x, excel_column_number_to_name(x)))
