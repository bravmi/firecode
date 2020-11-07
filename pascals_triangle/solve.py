from ..utils import *


def generate_pascal_triangle(num_rows):
    if not num_rows:
        return []
    rows = [[1]]
    for _ in range(num_rows - 1):
        prev = rows[-1]
        rows.append([1] + [a + b for a, b in zip(prev, prev[1:])] + [1])
    return rows


if __name__ == '__main__':
    assert generate_pascal_triangle(4) == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
    ]
