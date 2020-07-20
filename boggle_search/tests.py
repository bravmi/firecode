from .solve import *


def test1():
    board = [
        ['A', 'O', 'L'],
        ['D', 'E', 'L'],
        ['G', 'H', 'I'],
    ]
    assert boggle_search(board, 'HELLO') is True


def test2():
    board = [
        ['A', 'F', 'A', 'J'],
        ['S', 'I', 'V', 'A'],
        ['E', 'R', 'O', 'C'],
        ['C', 'X', 'E', 'K'],
        ['O', 'D', 'F', 'S'],
        ['D', 'E', 'E', 'E'],
    ]
    assert boggle_search(board, 'FIRECODE') is True
    assert boggle_search(board, 'JACKET') is False
    assert boggle_search(board, 'JACK') is True
    assert boggle_search(board, 'PREP') is False
    assert boggle_search(board, 'FIRES') is True
    assert boggle_search(board, 'DFS') is True
    assert boggle_search(board, 'ROCKS') is True
    assert boggle_search(board, 'ROCK') is True
    assert boggle_search(board, 'AXE') is False
    assert boggle_search(board, 'SEE') is True
