from firecode.utils import *


def transpose_matrix_hack(A):
    A[:] = [list(row) for row in zip(*A)]
    return A


def transpose_matrix(A):
    n = len(A)
    for i in range(n):
        for j in range(i):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    return A


if __name__ == '__main__':
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    print(transpose_matrix(A))
