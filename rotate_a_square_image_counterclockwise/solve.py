from firecode.utils import *


def rotate_square_image_ccw_hack(A):
    A[:] = [list(row) for row in zip(*A)][::-1]
    return A


def rotate_square_image_ccw(A):
    transpose_matrix(A)
    flip_vertical_axis(A)
    return A


def transpose_matrix(A):
    n = len(A)
    for i in range(n):
        for j in range(i):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    return A


def flip_vertical_axis(A):
    n = len(A)
    for i in range(n // 2):
        for j in range(n):
            A[i][j], A[-i - 1][j] = A[-i - 1][j], A[i][j]
    return A


def print_matrix(A):
    print('[')
    for row in A:
        print(f'    {row},')
    print(']')


if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [
        [3, 6, 9],
        [2, 5, 8],
        [1, 4, 7],
    ]

    print('[A]:')
    print_matrix(A)

    print()
    A = transpose_matrix(A)
    print('[A after transpose]:')
    print_matrix(A)

    print()
    A = flip_vertical_axis(A)
    print('[A after transpose and flip vert]:')
    print_matrix(A)

    assert A == B
