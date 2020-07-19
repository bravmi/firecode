from .solve import *


def test1():
    board = [
        ['A', 'O', 'L'],
        ['D', 'E', 'L'],
        ['G', 'H', 'I'],
    ]
    assert boggle_search(board, 'HELLO') == True


def test2():
    board = [
        ['A', 'F', 'A', 'J'],
        ['S', 'I', 'V', 'A'],
        ['E', 'R', 'O', 'C'],
        ['C', 'X', 'E', 'K'],
        ['O', 'D', 'F', 'S'],
        ['D', 'E', 'E', 'E'],
    ]
    assert boggle_search(board, 'FIRECODE') == True
    assert boggle_search(board, 'JACKET') == False
    assert boggle_search(board, 'JACK') == True
    assert boggle_search(board, 'PREP') == False
    assert boggle_search(board, 'FIRES') == True
    assert boggle_search(board, 'DFS') == True
    assert boggle_search(board, 'ROCKS') == True
    assert boggle_search(board, 'ROCK') == True
    assert boggle_search(board, 'AXE') == False
    assert boggle_search(board, 'SEE') == True
