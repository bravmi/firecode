from firecode.utils import *


def find_spiral(A):
    n, m = len(A), len(A[0])
    if not n or not m:
        return []

    spiral = []
    min_i, max_i, min_j, max_j = 0, n - 1, 0, m - 1
    while True:
        # right
        for j in range(min_j, max_j + 1):
            spiral.append(A[min_i][j])
        min_i += 1
        if min_i > max_i:
            break
        # down
        for i in range(min_i, max_i + 1):
            spiral.append(A[i][max_j])
        max_j -= 1
        if max_j < min_j:
            break
        # left
        for j in range(max_j, min_j - 1, -1):
            spiral.append(A[max_i][j])
        max_i -= 1
        if max_i < min_i:
            break
        # up
        for i in range(max_i, min_i - 1, -1):
            spiral.append(A[i][min_j])
        min_j += 1
        if min_j > max_j:
            break

    return spiral


if __name__ == '__main__':
    A = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    print('[find spiral]: {}'.format(find_spiral(A)))
