from .solve import *


def test1():
    board = [['A', 'X'], ['D', 'E']]
    assert sorted(print_paths(board)) == sorted(['ADE', 'AXE'])


def test2():
    board = [['A'], ['B'], ['C'], ['D']]
    assert sorted(print_paths(board)) == sorted(['ABCD'])


def test3():
    board = [[]]
    assert sorted(print_paths(board)) == sorted([])


def test4():
    board = [
        ['A', 'B', 'C', 'D'],
        ['E', 'F', 'G', 'H'],
        ['I', 'J', 'K', 'L'],
        ['M', 'N', 'O', 'P'],
    ]
    assert sorted(print_paths(board)) == sorted(
        [
            'ABCDHLP',
            'ABCGHLP',
            'ABCGKLP',
            'ABCGKOP',
            'ABFGHLP',
            'ABFGKLP',
            'ABFGKOP',
            'ABFJKLP',
            'ABFJKOP',
            'ABFJNOP',
            'AEFGHLP',
            'AEFGKLP',
            'AEFGKOP',
            'AEFJKLP',
            'AEFJKOP',
            'AEFJNOP',
            'AEIJKLP',
            'AEIJKOP',
            'AEIJNOP',
            'AEIMNOP',
        ]
    )


def test5():
    board = [['A']]
    assert sorted(print_paths(board)) == sorted(['A'])
