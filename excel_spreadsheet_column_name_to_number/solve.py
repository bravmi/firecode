from ..utils import *


def char2number(c):
    return ord(c) - ord('A') + 1


def excel_column_name_to_number(column_title):
    return sum(
        char2number(c) * 26 ** i for i, c in enumerate(reversed(column_title))
    )


if __name__ == '__main__':
    pass
