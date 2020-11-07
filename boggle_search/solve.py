from ..utils import *


def neighbors(x, y):
    yield x - 1, y - 1
    yield x - 1, y
    yield x - 1, y + 1
    yield x, y - 1
    yield x, y + 1
    yield x + 1, y - 1
    yield x + 1, y
    yield x + 1, y + 1


def boggle_search(board, word):
    n = len(board)
    m = len(board[0])
    l = len(word)

    def go(x, y, k):
        """Recursive search from all the cells

        x, y are current coordinates
        k is the word's index we're looking at right now
        """
        if k == l:
            return True
        if not (0 <= x < n) or not (0 <= y < m):
            return False
        if board[x][y] != word[k]:
            return False
        return any(go(i, j, k + 1) for i, j in neighbors(x, y))

    return any(go(i, j, 0) for i in range(n) for j in range(m))


if __name__ == '__main__':
    pass
