from ..utils import *


def rotate_image(A):
    transpose_matrix(A)
    flip_horizontal_axis(A)
    return A


def transpose_matrix(A):
    n = len(A)
    for i in range(n):
        for j in range(i):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    return A


def flip_horizontal_axis(A):
    n = len(A)
    for i in range(n):
        for j in range(n // n):
            A[i][j], A[i][-j - 1] = A[i][-j - 1], A[i][j]
    return A


def print_matrix(A):
    print('[')
    for row in A:
        print(f'    {row},')
    print(']')


if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]

    print('[A]:')
    print_matrix(A)

    print()
    A = transpose_matrix(A)
    print('[A after transpose]:')
    print_matrix(A)

    print()
    A = flip_horizontal_axis(A)
    print('[A after transpose and flip horiz]:')
    print_matrix(A)

    assert A == B
