from firecode.utils import *


def print_paths(board):
    m = len(board)
    n = len(board[0])

    @cached
    def paths(i, j):
        if i >= m or j >= n:
            return []
        cell = board[i][j]
        if i == m - 1 and j == n - 1:
            return [cell]

        down = paths(i + 1, j)
        right = paths(i, j + 1)
        return [cell + path for path in right + down]

    return sorted(paths(0, 0))


if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'D'],
        ['E', 'F', 'G', 'H'],
        ['I', 'J', 'K', 'L'],
        ['M', 'N', 'O', 'P'],
    ]
    print(print_paths(board))
